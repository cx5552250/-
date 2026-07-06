# 🚁 低空行业每日资讯推送系统

一个自动化的低空行业资讯抓取和推送工具，每天为您搜集整理热度最高的10条行业资讯，并通过企业微信推送给您。

## ✨ 功能特性

- ✅ **智能爬虫**：从多个低空行业资讯源自动抓取最新新闻
- ✅ **智能筛选**：基于关键词匹配算法，精准识别低空行业相关资讯
- ✅ **热度排序**：根据相关度和时间新鲜度综合评分，优先推送高价值资讯
- ✅ **去重处理**：自动去除重复内容，确保每条资讯都是独特的
- ✅ **微信推送**：通过企业微信机器人实时推送到您的手机
- ✅ **定时执行**：GitHub Actions每天自动运行，无需人工干预
- ✅ **开源免费**：完全开源，可自由定制和扩展

## 📋 前置要求

1. **GitHub账号**：用于部署自动化任务
2. **企业微信**：用于接收消息推送（个人也可注册企业微信）
3. **基础Python知识**：如需自定义资讯源或调整参数

## 🚀 快速开始

### 第一步：创建企业微信机器人

1. 下载并登录[企业微信](https://work.weixin.qq.com/)
2. 创建一个新企业（或个人使用）
3. 在企业微信中创建一个群聊
4. 点击群聊右上角的"..." → 添加群机器人
5. 点击"新建机器人"，设置机器人名称（如"低空资讯助手"）
6. 复制生成的**Webhook地址**（格式：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx`）

> 💡 **提示**：如果还没有企业微信，可以免费注册一个个人版企业微信

### 第二步：Fork本项目到GitHub

1. 访问本项目的GitHub仓库
2. 点击右上角的"Fork"按钮
3. 等待Fork完成

### 第三步：配置Webhook密钥

1. 进入您Fork后的仓库
2. 点击 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 填写：
   - Name: `WECHAT_WEBHOOK_URL`
   - Secret: 粘贴您刚才复制的企业微信Webhook地址
5. 点击 **Add secret**

### 第四步：测试运行

1. 在您的仓库中，点击 **Actions** 标签页
2. 选择左侧的 **"低空行业每日资讯推送"** 工作流
3. 点击右侧的 **Run workflow** → **Run workflow**（手动触发）
4. 等待1-2分钟，查看执行结果
5. 检查企业微信是否收到测试消息

### 第五步：确认定时任务

- GitHub Actions已配置为**每天UTC时间0点**（北京时间早上8点）自动执行
- 您可以在`.github/workflows/daily_news_push.yml`中修改执行时间

## ⚙️ 自定义配置

### 修改资讯源

编辑 `config.py` 文件中的 `NEWS_SOURCES` 列表：

```python
NEWS_SOURCES = [
    {
        "name": "中国民航网",
        "url": "https://www.caacnews.com.cn/",
        "type": "web"
    },
    # 添加更多资讯源...
]
```

### 调整关键词

编辑 `config.py` 文件中的 `KEYWORDS` 列表，添加您关注的特定领域词汇：

```python
KEYWORDS = [
    "低空经济", "无人机", "eVTOL", 
    # 添加更多关键词...
]
```

### 修改推送数量

编辑 `config.py` 文件中的 `MAX_NEWS_COUNT`：

```python
MAX_NEWS_COUNT = 15  # 改为推送15条
```

### 修改执行时间

编辑 `.github/workflows/daily_news_push.yml`：

```yaml
schedule:
  # cron表达式：分 时 日 月 周
  - cron: '0 2 * * *'  # 改为每天UTC 2点（北京时间10点）
```

## 📂 项目结构

```
├── main.py                 # 主程序入口
├── crawler.py              # 新闻爬虫模块
├── processor.py            # 资讯处理模块（去重、排序）
├── wechat_bot.py           # 企业微信推送模块
├── config.py               # 配置文件
├── requirements.txt        # Python依赖包
├── .github/
│   └── workflows/
│       └── daily_news_push.yml  # GitHub Actions配置
└── README.md               # 说明文档
```

## 🔧 本地开发

如果您想在本地测试或开发：

```bash
# 1. 克隆项目
git clone <your-repo-url>
cd chat-1

# 2. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置Webhook
# 编辑 config.py，填入您的 WECHAT_WEBHOOK_URL

# 5. 运行程序
python main.py
```

## 🐛 常见问题

### Q1: 没有收到推送消息？

**检查清单：**
- ✅ Webhook URL是否正确配置在GitHub Secrets中
- ✅ 企业微信机器人是否正常工作（可在群聊中测试发送消息）
- ✅ 查看GitHub Actions的执行日志，确认是否有错误

### Q2: 抓取的新闻不够准确？

**解决方案：**
- 在 `config.py` 中添加更多相关的关键词
- 增加更多高质量的资讯源
- 调整 `processor.py` 中的评分算法

### Q3: 想推送给多个人？

**方法：**
- 在企业微信群中添加更多成员
- 或者创建多个机器人，分别推送

### Q4: GitHub Actions执行失败？

**排查步骤：**
1. 查看Actions标签页中的失败记录
2. 检查错误日志
3. 确认所有依赖包正确安装
4. 尝试手动触发一次工作流

## 📝 资讯源建议

推荐的低空行业资讯源：

- 中国民航网 (caacnews.com.cn)
- 低空经济观察
- 无人机世界 (uavworlds.com)
- 通航在线
- eVTOL行业媒体
- 各地民航管理局官网

您可以在 `crawler.py` 中添加针对特定网站的解析规则。

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

- 报告Bug或提出新功能建议
- 改进爬虫解析规则
- 优化推荐算法
- 添加新的资讯源支持

## 📄 许可证

本项目采用MIT许可证，您可以自由使用、修改和分发。

## 📮 联系方式

如有问题或建议，请通过以下方式联系：

- 提交GitHub Issue
- 发送邮件至：[您的邮箱]

---

**祝您每天都能第一时间掌握低空行业动态！** 🚁✨
