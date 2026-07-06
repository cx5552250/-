# 🚀 GitHub Actions部署完整指南（无需Git命令行）

## 📋 前置准备

在开始之前，请确保您已准备好：
- ✅ GitHub账号（如没有，访问 https://github.com/join 注册）
- ✅ 企业微信Webhook URL（如何获取见下文）

---

## 第一步：获取企业微信Webhook URL（2分钟）

### 操作步骤：

1. **打开企业微信**
   - 如果没有，访问 https://work.weixin.qq.com/ 注册个人版

2. **创建群聊**
   - 在企业微信中创建一个新群（可以只拉自己一个人）

3. **添加机器人**
   - 点击群右上角的「...」或「群详情」
   - 找到「添加群机器人」或「群机器人」
   - 点击「新建机器人」

4. **配置机器人**
   - 设置名称：`低空资讯助手`（可自定义）
   - 点击「添加」

5. **复制Webhook地址**
   - 系统会生成一个Webhook URL
   - 格式类似：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=abcdef123456-xxxxx`
   - **复制并保存这个地址**（后续需要用到）

✅ **测试机器人是否正常工作：**
- 在群聊中可以@机器人发送测试消息
- 或记下Webhook URL，稍后在GitHub中配置

---

## 第二步：在GitHub创建仓库（3分钟）

### 操作步骤：

1. **登录GitHub**
   - 访问：https://github.com
   - 登录您的账号

2. **创建新仓库**
   - 点击右上角「+」→ 「New repository」
   - 或直接访问：https://github.com/new

3. **填写仓库信息**
   ```
   Repository name: low-altitude-news（或您喜欢的名称）
   Description: 低空行业每日资讯推送系统
   Public/Private: Public（公开）或 Private（私有）均可
   ✅ Initialize this repository with a README: 不勾选
   ```
   - 点击「Create repository」

4. **记录仓库地址**
   - 创建成功后，页面会显示仓库URL
   - 格式：`https://github.com/您的用户名/low-altitude-news.git`
   - **记下这个地址**

---

## 第三步：上传代码到GitHub（5分钟）

由于本地没有Git，我们使用GitHub网页界面直接上传文件。

### 方法A：使用GitHub Desktop（推荐，图形化操作）

1. **下载GitHub Desktop**
   - 访问：https://desktop.github.com/
   - 下载并安装

2. **克隆仓库到本地**
   - 打开GitHub Desktop
   - File → Clone repository
   - 选择刚才创建的仓库
   - 选择本地保存路径

3. **复制项目文件**
   - 将 `c:\Users\31477\Documents\QoderCN\2026-07-05\chat-1` 文件夹中的所有文件
   - 复制到GitHub Desktop克隆的文件夹中

4. **提交并推送**
   - 在GitHub Desktop中可以看到所有变更
   - 在Summary中输入：`Initial commit: 低空资讯推送系统`
   - 点击「Commit to main」
   - 点击「Push origin」

### 方法B：直接在GitHub网页上传（最简单）

1. **进入仓库页面**
   - 访问您刚创建的仓库
   - 例如：https://github.com/您的用户名/low-altitude-news

2. **上传文件**
   - 点击「Add file」→ 「Upload files」
   - 或者直接拖拽文件到页面

3. **逐个上传以下文件**
   ```
   ✓ main.py
   ✓ crawler.py
   ✓ processor.py
   ✓ wechat_bot.py
   ✓ config.py
   ✓ requirements.txt
   ✓ .gitignore
   ```

4. **创建目录结构**
   - 点击「Add file」→ 「Create new file」
   - 文件名输入：`.github/workflows/daily_news_push.yml`
   - 粘贴 `.github/workflows/daily_news_push.yml` 的内容
   - 点击「Commit changes」

5. **提交所有文件**
   - Commit message: `Initial commit: 低空资讯推送系统`
   - 点击「Commit changes」

### 方法C：使用VS Code（如果您有安装）

1. 用VS Code打开项目文件夹
2. 左侧源代码管理面板
3. 初始化仓库 → 暂存所有更改 → 提交
4. 发布到GitHub

---

## 第四步：配置企业微信Webhook密钥（2分钟）

### 操作步骤：

1. **进入仓库设置**
   - 在您的GitHub仓库页面
   - 点击顶部的「Settings」标签

2. **找到Secrets配置**
   - 左侧菜单找到「Secrets and variables」
   - 展开后点击「Actions」

3. **添加新密钥**
   - 点击「New repository secret」按钮

4. **填写密钥信息**
   ```
   Name: WECHAT_WEBHOOK_URL
   Secret: 粘贴您第一步复制的企业微信Webhook URL
   ```
   - 点击「Add secret」

5. **验证配置**
   - 应该能看到列表中有一个名为 `WECHAT_WEBHOOK_URL` 的密钥
   - 值被隐藏显示为 `••••••••`

✅ **完成！密钥已安全存储**

---

## 第五步：手动触发测试（3分钟）

### 操作步骤：

1. **进入Actions页面**
   - 在仓库页面顶部点击「Actions」标签
   - 首次进入可能需要几秒加载

2. **选择工作流**
   - 左侧应该能看到「低空行业每日资讯推送」
   - 点击进入

3. **手动运行**
   - 点击右上角的「Run workflow」按钮
   - 在下拉框中选择分支：`main`（或`master`）
   - 再次点击「Run workflow」

4. **查看执行状态**
   - 页面会显示正在运行的工作流
   - 点击具体的运行记录查看详细日志
   - 等待执行完成（通常30-60秒）

5. **检查结果**
   - ✅ 绿色对勾：执行成功
   - ❌ 红色叉号：执行失败（点击查看日志排查）

---

## 第六步：验证推送结果（1分钟）

### 检查清单：

✅ **成功的标志：**
1. GitHub Actions显示绿色对勾 ✓
2. 企业微信收到一条消息
3. 消息标题：「🚁 低空行业每日资讯 🚁」
4. 包含10条资讯，每条有标题和链接
5. 显示相关度评分（⭐⭐⭐⭐⭐）

❌ **如果未收到消息：**
1. 检查GitHub Actions日志中的错误信息
2. 确认Webhook URL配置正确
3. 确认企业微信机器人正常工作
4. 检查网络连接是否正常

---

## 🔧 常见问题排查

### 问题1：GitHub Actions执行失败

**可能原因：**
- Webhook URL配置错误
- Python依赖安装失败
- 代码文件缺失

**解决方法：**
1. 点击失败的运行记录
2. 查看具体哪一步出错
3. 根据错误信息修复

### 问题2：收不到企业微信消息

**检查步骤：**
```
1. 确认WECHAT_WEBHOOK_URL已正确配置在Secrets中
2. 在企业微信群中@机器人测试是否能发送消息
3. 检查Webhook URL是否完整（包含key参数）
4. 查看GitHub Actions日志中的推送步骤
```

### 问题3：抓取的资讯不准确

**优化方法：**
1. 编辑 `config.py` 中的 `KEYWORDS` 列表
2. 添加更多相关行业关键词
3. 提交更改到GitHub
4. 重新触发Actions测试

### 问题4：想修改推送时间

**修改方法：**
1. 编辑 `.github/workflows/daily_news_push.yml`
2. 修改 `cron` 表达式
3. 提交更改
4. 新的定时任务会自动生效

常用时间参考：
```yaml
# 北京时间8点
- cron: '0 0 * * *'

# 北京时间9点
- cron: '0 1 * * *'

# 北京时间10点
- cron: '0 2 * * *'
```

---

## 📊 预期效果示例

当系统成功运行时，您会在企业微信收到类似这样的消息：

```
🚁 低空行业每日资讯 🚁
📅 日期: 2026年07月06日
📊 共筛选出 10 条高热度资讯

1. 🔥 [中国民航网] 我国eVTOL适航认证取得重大突破，多家企业获颁型号合格证
   链接: https://www.caacnews.com.cn/xxx
   相关度: ⭐⭐⭐⭐⭐

2. 🔥 [无人机世界] 低空物流试点城市扩大至30个，配送效率提升50%
   链接: https://www.uavworlds.com/xxx
   相关度: ⭐⭐⭐⭐

3. 🔥 [低空经济观察] 某市开通首条城市空中交通航线，采用eVTOL飞行器
   链接: https://www.lowaltitude.com/xxx
   相关度: ⭐⭐⭐⭐

...（共10条）

---
💡 提示: 点击链接查看完整资讯
```

---

## 🎯 后续维护

### 每天自动执行
- 系统会每天北京时间8点自动运行
- 无需任何人工干预
- 您可以在Actions页面查看历史执行记录

### 定期检查建议
- 每周查看一次Actions执行历史
- 确认推送的资讯质量
- 根据需要调整关键词或资讯源

### 优化改进
- 根据阅读反馈调整关键词权重
- 添加新的优质资讯源
- 移除失效或低质量的资讯源

---

## 💡 快速参考

**重要链接：**
- GitHub仓库：https://github.com/您的用户名/仓库名
- Actions页面：https://github.com/您的用户名/仓库名/actions
- 企业微信：https://work.weixin.qq.com/

**关键配置：**
- Secrets名称：`WECHAT_WEBHOOK_URL`
- 工作流文件：`.github/workflows/daily_news_push.yml`
- 主程序：`main.py`

---

## 🆘 需要帮助？

如果在操作过程中遇到任何问题：

1. **查看错误日志**
   - GitHub Actions → 点击失败的运行 → 查看详细日志

2. **检查配置文件**
   - 确认所有文件都已上传
   - 确认目录结构正确

3. **联系我**
   - 随时告诉我您遇到的具体问题
   - 我会提供针对性的解决方案

---

**准备好了吗？让我们开始吧！** 🚀

从**第一步**开始，逐步完成每个步骤。有任何疑问都可以随时问我！
