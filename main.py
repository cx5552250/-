"""
低空行业资讯每日推送主程序
整合爬虫、处理器和推送模块，实现完整的自动化流程
"""

import sys
from crawler import NewsCrawler
from processor import NewsProcessor
from wechat_bot import WeChatBot


def main():
    """主函数：执行完整的资讯抓取、处理和推送流程"""
    
    print("=" * 60)
    print("🚁 低空行业每日资讯推送系统")
    print("=" * 60)
    print()
    
    # 1. 初始化各模块
    print("【步骤1】初始化模块...")
    crawler = NewsCrawler()
    processor = NewsProcessor()
    bot = WeChatBot()
    print("✓ 模块初始化完成\n")
    
    # 2. 抓取新闻
    print("【步骤2】开始抓取新闻...")
    raw_news = crawler.fetch_all_news()
    
    if not raw_news:
        print("⚠️  未抓取到任何新闻，程序退出")
        return False
    print()
    
    # 3. 去重处理
    print("【步骤3】进行去重处理...")
    unique_news = processor.remove_duplicates(raw_news)
    print()
    
    # 4. 筛选和排序
    print("【步骤4】筛选低空相关新闻并排序...")
    top_news = processor.filter_and_rank(unique_news)
    
    if not top_news:
        print("⚠️  未找到相关的低空行业新闻")
        # 仍然发送通知
        content = "🚁 **低空行业每日资讯**\n\n今日暂无相关行业资讯，请检查资讯源配置。"
        bot.send_markdown_message(content)
        return True
    print()
    
    # 5. 格式化输出
    print("【步骤5】格式化资讯内容...")
    formatted_content = processor.format_news_for_display(top_news)
    print("✓ 格式化完成\n")
    
    # 打印预览（调试模式）
    if hasattr(__builtins__, 'DEBUG') and __builtins__.get('DEBUG', False):
        print("=== 预览 ===")
        print(formatted_content)
        print("============\n")
    
    # 6. 推送到企业微信
    print("【步骤6】推送到企业微信...")
    success = bot.send_markdown_message(formatted_content)
    
    if success:
        print("\n" + "=" * 60)
        print("✅ 今日资讯推送完成！")
        print("=" * 60)
        return True
    else:
        print("\n" + "=" * 60)
        print("❌ 推送失败，请检查配置和网络连接")
        print("=" * 60)
        return False


if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"\n❌ 程序执行出错: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
