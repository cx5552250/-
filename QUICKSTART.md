# ⚡ 5分钟快速配置指南

## 第一步：获取企业微信Webhook（2分钟）

1. **下载企业微信**
   - 访问 https://work.weixin.qq.com/
   - 注册并登录（个人也可使用）

2. **创建群机器人**
   - 在企业微信中创建一个群聊（可以只拉自己）
   - 点击群右上角「...」→「添加群机器人」
   - 点击「新建机器人」
   - 设置名称：`低空资讯助手`
   - **复制Webhook地址**（重要！）
   
   Webhook格式示例：
   ```
   https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=abcdef123456-xxxxx
   ```

## 第二步：部署到GitHub（3分钟）

### 方式A：直接使用模板（推荐）

1. **Fork本仓库**
   - 点击GitHub页面右上角的「Fork」按钮
   - 等待复制完成

2. **配置Secrets**
   - 进入您的仓库 → Settings → Secrets and variables → Actions
   - 点击「New repository secret」
   - Name: `WECHAT_WEBHOOK_URL`
   - Secret: 粘贴刚才复制的Webhook地址
   - 点击「Add secret」

3. **测试运行**
   - 点击仓库顶部的「Actions」标签
   - 选择左侧「低空行业每日资讯推送」
   - 点击右上角「Run workflow」→「Run workflow」
   - 等待1-2分钟
   - 查看企业微信是否收到消息 ✅

### 方式B：本地测试（可选）

如果您想先在本地测试：

```bash
# 1. 克隆仓库
git clone <your-repo-url>
cd chat-1

# 2. 安装依赖
pip install -r requirements.txt

# 3. 编辑config.py，填入Webhook URL
# 将 WECHAT_WEBHOOK_URL 改为您复制的地址

# 4. 运行测试
python main.py
```

## 第三步：验证成功

✅ **成功的标志：**
- GitHub Actions显示绿色对勾 ✓
- 企业微信收到一条包含10条资讯的消息
- 消息格式美观，带有链接和相关度评分

❌ **如果失败：**
1. 检查GitHub Actions日志中的错误信息
2. 确认Webhook URL正确无误
3. 确认企业微信机器人正常工作（可在群里手动@机器人测试）

## 第四步：自定义（可选）

### 修改推送时间

编辑 `.github/workflows/daily_news_push.yml`：

```yaml
schedule:
  # cron表达式：分 时 日 月 周（UTC时间）
  - cron: '0 1 * * *'  # 改为UTC 1点 = 北京时间9点
```

常用时间参考：
- `0 0 * * *` = 北京时间8:00
- `0 1 * * *` = 北京时间9:00
- `0 2 * * *` = 北京时间10:00

### 添加更多资讯源

编辑 `config.py`：

```python
NEWS_SOURCES = [
    {
        "name": "您的资讯源名称",
        "url": "https://example.com/",
        "type": "web"
    },
    # 继续添加...
]
```

### 调整关键词

编辑 `config.py` 中的 `KEYWORDS` 列表，添加您特别关注的词汇。

## 🎉 完成！

现在系统会每天自动为您推送低空行业资讯，无需任何操作！

---

**需要帮助？**
- 查看完整的 README.md 文档
- 提交GitHub Issue
- 检查GitHub Actions执行日志
