# 企业微信机器人配置
WECHAT_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY_HERE

# 资讯源配置（可根据需要添加或删除）
NEWS_SOURCES = [
    {
        "name": "中国民航网",
        "url": "https://www.caacnews.com.cn/",
        "type": "web"
    },
    {
        "name": "低空经济观察",
        "url": "https://www.lowaltitude.com/",
        "type": "web"
    },
    {
        "name": "无人机世界",
        "url": "https://www.uavworlds.com/",
        "type": "web"
    }
]

# 低空行业关键词（用于筛选和排序）
KEYWORDS = [
    "低空经济", "无人机", "eVTOL", "电动垂直起降", "通用航空",
    "飞行汽车", "空中交通", "低空物流", "城市空运", "UAM",
    "适航认证", "空域管理", "低空监管", "通航机场", "直升机",
    "无人驾驶航空器", "低空基础设施", " vertiport", "AAM"
]

# 最大推送条数
MAX_NEWS_COUNT = 10

# 是否启用调试模式
DEBUG = False
