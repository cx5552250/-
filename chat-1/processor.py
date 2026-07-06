"""
资讯处理模块
负责去重、关键词匹配、热度排序等功能
"""

import config
from datetime import datetime
import hashlib


class NewsProcessor:
    """新闻处理器"""
    
    def __init__(self):
        self.keywords = config.KEYWORDS
    
    def calculate_relevance_score(self, news):
        """
        计算新闻与低空行业的相关度分数
        
        Args:
            news: 新闻字典
            
        Returns:
            float: 相关度分数（0-100）
        """
        title = news.get('title', '').lower()
        summary = news.get('summary', '').lower()
        content = title + ' ' + summary
        
        score = 0
        
        # 关键词匹配计分
        for keyword in self.keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in content:
                # 标题中出现权重更高
                if keyword_lower in title:
                    score += 15
                else:
                    score += 8
        
        # 时间新鲜度计分（24小时内+20分，48小时内+10分）
        publish_time = news.get('publish_time', datetime.now())
        if isinstance(publish_time, str):
            try:
                publish_time = datetime.fromisoformat(publish_time)
            except:
                publish_time = datetime.now()
        
        hours_diff = (datetime.now() - publish_time).total_seconds() / 3600
        if hours_diff < 24:
            score += 20
        elif hours_diff < 48:
            score += 10
        
        return min(score, 100)  # 最高100分
    
    def is_low_altitude_related(self, news):
        """
        判断新闻是否与低空行业相关
        
        Args:
            news: 新闻字典
            
        Returns:
            bool: 是否相关
        """
        title = news.get('title', '').lower()
        summary = news.get('summary', '').lower()
        content = title + ' ' + summary
        
        # 检查是否包含任一关键词
        for keyword in self.keywords:
            if keyword.lower() in content:
                return True
        
        return False
    
    def remove_duplicates(self, news_list):
        """
        去除重复新闻（基于标题相似度）
        
        Args:
            news_list: 新闻列表
            
        Returns:
            list: 去重后的新闻列表
        """
        seen_titles = set()
        unique_news = []
        
        for news in news_list:
            title = news.get('title', '')
            # 生成标题的标准化哈希值用于去重
            normalized_title = self._normalize_title(title)
            title_hash = hashlib.md5(normalized_title.encode('utf-8')).hexdigest()
            
            if title_hash not in seen_titles:
                seen_titles.add(title_hash)
                unique_news.append(news)
        
        print(f"去重前: {len(news_list)} 条, 去重后: {len(unique_news)} 条")
        return unique_news
    
    def _normalize_title(self, title):
        """
        标准化标题（去除标点、空格等）
        
        Args:
            title: 原始标题
            
        Returns:
            str: 标准化后的标题
        """
        # 转换为小写
        title = title.lower()
        # 去除常见标点符号
        for char in ['【', '】', '「', '」', '"', "'", '!', '?', '.', ',']:
            title = title.replace(char, '')
        # 去除多余空格
        title = ' '.join(title.split())
        return title
    
    def filter_and_rank(self, news_list):
        """
        筛选低空相关新闻并按热度排序
        
        Args:
            news_list: 新闻列表
            
        Returns:
            list: 排序后的相关新闻列表
        """
        # 1. 筛选相关度高的新闻
        related_news = []
        for news in news_list:
            if self.is_low_altitude_related(news):
                score = self.calculate_relevance_score(news)
                news['relevance_score'] = score
                related_news.append(news)
        
        print(f"筛选出 {len(related_news)} 条低空行业相关新闻")
        
        # 2. 按相关度分数降序排序
        ranked_news = sorted(related_news, key=lambda x: x.get('relevance_score', 0), reverse=True)
        
        # 3. 取前N条
        top_news = ranked_news[:config.MAX_NEWS_COUNT]
        
        return top_news
    
    def format_news_for_display(self, news_list):
        """
        格式化新闻用于展示
        
        Args:
            news_list: 新闻列表
            
        Returns:
            str: 格式化后的文本
        """
        if not news_list:
            return "今日暂无低空行业相关资讯"
        
        output = []
        output.append("🚁 **低空行业每日资讯** 🚁")
        output.append(f"📅 日期: {datetime.now().strftime('%Y年%m月%d日')}")
        output.append(f"📊 共筛选出 {len(news_list)} 条高热度资讯\n")
        
        for i, news in enumerate(news_list, 1):
            title = news.get('title', '无标题')
            url = news.get('url', '#')
            source = news.get('source', '未知来源')
            score = news.get('relevance_score', 0)
            
            # 限制标题长度
            if len(title) > 50:
                title = title[:47] + '...'
            
            output.append(f"{i}. 🔥 [{source}] {title}")
            output.append(f"   链接: {url}")
            output.append(f"   相关度: {'⭐' * min(int(score/20), 5)}\n")
        
        output.append("---")
        output.append("💡 提示: 点击链接查看完整资讯")
        
        return '\n'.join(output)


if __name__ == '__main__':
    # 测试处理器
    processor = NewsProcessor()
    
    # 示例新闻
    test_news = [
        {
            'title': '中国低空经济迎来爆发式增长，eVTOL企业获巨额融资',
            'url': 'https://example.com/news1',
            'source': '测试源',
            'publish_time': datetime.now(),
            'summary': ''
        },
        {
            'title': '无人机物流配送试点城市扩大至20个',
            'url': 'https://example.com/news2',
            'source': '测试源',
            'publish_time': datetime.now(),
            'summary': ''
        },
        {
            'title': '某明星演唱会门票开售',
            'url': 'https://example.com/news3',
            'source': '测试源',
            'publish_time': datetime.now(),
            'summary': ''
        }
    ]
    
    # 测试筛选和排序
    filtered = processor.filter_and_rank(test_news)
    print("\n=== 筛选结果 ===")
    for news in filtered:
        print(f"标题: {news['title']}")
        print(f"相关度: {news['relevance_score']}")
        print()
