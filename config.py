import os

# 企业微信机器人配置
# 优先从环境变量读取（GitHub Actions通过secrets注入），否则使用默认值
WECHAT_WEBHOOK_URL = os.environ.get(
    "WECHAT_WEBHOOK_URL",
    "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY_HERE"
)

# 资讯源配置（使用国际可访问的RSS和搜索源，兼容GitHub Actions海外服务器）
NEWS_SOURCES = [
    {
        "name": "Google新闻-低空经济",
        "url": "https://news.google.com/rss/search?q=低空经济+OR+无人机+OR+eVTOL&hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
        "type": "rss"
    },
    {
        "name": "Google新闻-通用航空",
        "url": "https://news.google.com/rss/search?q=通用航空+OR+低空物流+OR+城市空中交通&hl=zh-CN&gl=CN&ceid=CN:zh-Hans",
        "type": "rss"
    },
    {
        "name": "Bing新闻-无人机",
        "url": "https://www.bing.com/news/search?q=drone+OR+eVTOL+OR+UAV&format=rss",
        "type": "rss"
    },
    {
        "name": "DroneDJ",
        "url": "https://dronedj.com/feed/",
        "type": "rss"
    },
    {
        "name": "sUAS News",
        "url": "https://www.suasnews.com/feed",
        "type": "rss"
    }
]

# 低空行业关键词（用于筛选和排序）
KEYWORDS = [
    "低空经济", "无人机", "eVTOL", "电动垂直起降", "通用航空",
    "飞行汽车", "空中交通", "低空物流", "城市空运", "UAM",
    "适航认证", "空域管理", "低空监管", "通航机场", "直升机",
    "无人驾驶航空器", "低空基础设施", "vertiport", "AAM",
    # 英文关键词（匹配国际资讯源）
    "drone", "UAV", "urban air mobility", "advanced air mobility",
    "electric vertical takeoff", "drone delivery", "autonomous aircraft",
    "general aviation", "airspace management", "vertiport"
]

# 最大推送条数
MAX_NEWS_COUNT = 10

# 是否启用调试模式
DEBUG = False
