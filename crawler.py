"""
低空行业资讯爬虫模块
负责从多个资讯源（RSS/网页）抓取最新行业信息
"""

import requests
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil import parser as dateutil_parser
import config
import re


class NewsCrawler:
    """新闻资讯爬虫类"""

    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def fetch_news_from_source(self, source):
        """
        从指定资讯源抓取新闻

        Args:
            source: 资讯源配置字典

        Returns:
            list: 新闻列表，每个元素为dict包含title, url, summary, publish_time, source
        """
        try:
            source_type = source.get('type', 'web')
            if source_type == 'rss':
                return self._fetch_rss_news(source)
            elif source_type == 'web':
                return self._fetch_web_news(source)
            else:
                print(f"不支持的资讯源类型: {source_type}")
                return []
        except Exception as e:
            print(f"抓取资讯源 [{source['name']}] 失败: {str(e)}")
            return []

    def _fetch_rss_news(self, source):
        """
        从RSS源抓取新闻

        Args:
            source: 资讯源配置

        Returns:
            list: 新闻列表
        """
        news_list = []
        url = source['url']
        source_name = source['name']

        try:
            response = self.session.get(url, timeout=15)
            feed = feedparser.parse(response.content)

            for entry in feed.entries[:30]:
                title = entry.get('title', '').strip()
                link = entry.get('link', '')

                if not title or len(title) < 5:
                    continue

                # 解析发布时间
                publish_time = datetime.now()
                pub_date_str = entry.get('published') or entry.get('updated', '')
                if pub_date_str:
                    try:
                        publish_time = dateutil_parser.parse(pub_date_str, ignoretz=True)
                    except Exception:
                        pass

                # 提取摘要（去除HTML标签）
                summary = ''
                if entry.get('summary'):
                    summary = BeautifulSoup(entry['summary'], 'lxml').get_text(strip=True)[:200]

                news_list.append({
                    'title': title,
                    'url': link,
                    'summary': summary,
                    'publish_time': publish_time,
                    'source': source_name
                })

            print(f"成功从 [{source_name}] 抓取 {len(news_list)} 条新闻")
            return news_list

        except Exception as e:
            print(f"解析RSS [{source_name}] 失败: {str(e)}")
            return []

    def _fetch_web_news(self, source):
        """
        从网页抓取新闻（通用方法）
        
        Args:
            source: 资讯源配置
            
        Returns:
            list: 新闻列表
        """
        news_list = []
        url = source['url']
        source_name = source['name']
        
        try:
            response = self.session.get(url, timeout=10)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'lxml')
            
            # 根据不同网站定制解析规则
            if 'caacnews.com.cn' in url:
                news_list = self._parse_caacnews(soup, source_name)
            elif 'lowaltitude.com' in url:
                news_list = self._parse_lowaltitude(soup, source_name)
            elif 'uavworlds.com' in url:
                news_list = self._parse_uavworlds(soup, source_name)
            else:
                # 通用解析规则
                news_list = self._parse_generic(soup, source_name, url)
            
            print(f"成功从 [{source_name}] 抓取 {len(news_list)} 条新闻")
            return news_list
            
        except Exception as e:
            print(f"解析 [{source_name}] 失败: {str(e)}")
            return []
    
    def _parse_caacnews(self, soup, source_name):
        """解析中国民航网"""
        news_list = []
        
        # 查找新闻链接（根据实际网站结构调整选择器）
        articles = soup.find_all('a', href=re.compile(r'/\d{4}/\d{2}/\d{2}/'))
        
        for article in articles[:20]:  # 限制处理数量
            title = article.get_text(strip=True)
            url = article.get('href', '')
            
            if not title or len(title) < 5:
                continue
            
            # 补全URL
            if url.startswith('/'):
                url = 'https://www.caacnews.com.cn' + url
            elif not url.startswith('http'):
                url = 'https://www.caacnews.com.cn' + url
            
            news_list.append({
                'title': title,
                'url': url,
                'summary': '',
                'publish_time': datetime.now(),
                'source': source_name
            })
        
        return news_list
    
    def _parse_lowaltitude(self, soup, source_name):
        """解析低空经济观察网站"""
        news_list = []
        
        # 查找文章标题
        articles = soup.find_all(['h2', 'h3', 'a'], class_=re.compile(r'title|article|news'))
        
        for article in articles[:20]:
            title = article.get_text(strip=True)
            url = article.get('href', '')
            
            if not title or len(title) < 5:
                continue
            
            if not url.startswith('http'):
                base_url = 'https://www.lowaltitude.com'
                url = base_url + url if url.startswith('/') else base_url + '/' + url
            
            news_list.append({
                'title': title,
                'url': url,
                'summary': '',
                'publish_time': datetime.now(),
                'source': source_name
            })
        
        return news_list
    
    def _parse_uavworlds(self, soup, source_name):
        """解析无人机世界网站"""
        news_list = []
        
        # 查找新闻条目
        articles = soup.find_all('div', class_=re.compile(r'post|article|news-item'))
        
        for article in articles[:20]:
            title_elem = article.find(['h2', 'h3', 'a'])
            if not title_elem:
                continue
            
            title = title_elem.get_text(strip=True)
            url = title_elem.get('href', '')
            
            if not title or len(title) < 5:
                continue
            
            if not url.startswith('http'):
                base_url = 'https://www.uavworlds.com'
                url = base_url + url if url.startswith('/') else base_url + '/' + url
            
            news_list.append({
                'title': title,
                'url': url,
                'summary': '',
                'publish_time': datetime.now(),
                'source': source_name
            })
        
        return news_list
    
    def _parse_generic(self, soup, source_name, base_url):
        """通用网页解析方法"""
        news_list = []
        
        # 尝试查找所有链接
        links = soup.find_all('a', href=True)
        
        for link in links[:30]:
            title = link.get_text(strip=True)
            url = link['href']
            
            # 过滤无效链接
            if not title or len(title) < 5 or len(title) > 100:
                continue
            
            # 跳过非新闻链接
            skip_keywords = ['登录', '注册', '关于', '联系', '广告', '隐私']
            if any(keyword in title for keyword in skip_keywords):
                continue
            
            # 补全URL
            if url.startswith('//'):
                url = 'https:' + url
            elif url.startswith('/'):
                url = base_url.rstrip('/') + url
            elif not url.startswith('http'):
                url = base_url.rstrip('/') + '/' + url
            
            news_list.append({
                'title': title,
                'url': url,
                'summary': '',
                'publish_time': datetime.now(),
                'source': source_name
            })
        
        return news_list
    
    def fetch_article_summary(self, url, target_chars=100):
        """
        访问文章页面，提取约target_chars字的内容提要

        Args:
            url: 文章URL
            target_chars: 目标字符数（中文）

        Returns:
            str: 内容提要
        """
        try:
            response = self.session.get(url, timeout=10)
            response.encoding = response.apparent_encoding
            soup = BeautifulSoup(response.text, 'lxml')

            # 移除无关元素
            for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer', 'aside']):
                tag.decompose()

            # 优先从article、main标签或常见正文class中提取
            content_elem = (
                soup.find('article')
                or soup.find('main')
                or soup.find('div', class_=re.compile(r'content|article-body|post-body|entry-content'))
                or soup.find('div', id=re.compile(r'content|article'))
                or soup.find('body')
            )

            if not content_elem:
                return ''

            # 提取所有段落文本
            paragraphs = content_elem.find_all('p')
            text_parts = []
            for p in paragraphs:
                t = p.get_text(strip=True)
                if len(t) > 20:  # 跳过过短的段落（如广告文字）
                    text_parts.append(t)

            if not text_parts:
                # 如果没找到段落，尝试获取整体文本
                full_text = content_elem.get_text(separator=' ', strip=True)
            else:
                full_text = ' '.join(text_parts)

            # 清理多余空白
            full_text = re.sub(r'\s+', ' ', full_text).strip()

            # 截取目标长度
            if len(full_text) > target_chars:
                full_text = full_text[:target_chars] + '...'

            return full_text

        except Exception as e:
            print(f"  提取文章摘要失败 ({url[:60]}...): {str(e)}")
            return ''

    def enrich_with_summaries(self, news_list, target_chars=100):
        """
        为新闻列表补充内容提要（逐篇访问原文页面）

        Args:
            news_list: 新闻列表
            target_chars: 每条提要的目标字符数
        """
        print("正在为精选资讯生成内容提要...")
        for news in news_list:
            existing_summary = news.get('summary', '')
            if not existing_summary or len(existing_summary) < 50:
                news['summary'] = self.fetch_article_summary(news['url'], target_chars)
            elif len(existing_summary) > target_chars:
                news['summary'] = existing_summary[:target_chars] + '...'
            print(f"  ✓ {news['title'][:40]}...")

    def fetch_all_news(self):
        """
        从所有配置的资讯源抓取新闻
        
        Returns:
            list: 所有新闻列表
        """
        all_news = []
        
        for source in config.NEWS_SOURCES:
            print(f"正在抓取: {source['name']}...")
            news = self.fetch_news_from_source(source)
            all_news.extend(news)
        
        print(f"\n总共抓取到 {len(all_news)} 条原始新闻")
        return all_news


if __name__ == '__main__':
    # 测试爬虫功能
    crawler = NewsCrawler()
    news_list = crawler.fetch_all_news()
    
    print("\n=== 前5条新闻预览 ===")
    for i, news in enumerate(news_list[:5], 1):
        print(f"{i}. [{news['source']}] {news['title']}")
        print(f"   URL: {news['url']}\n")
