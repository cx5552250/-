# Python未安装 - 本地测试指南

## ❌ 当前状态
系统检测到您的Windows环境中尚未安装Python，无法直接运行本地测试。

## ✅ 解决方案

### 第一步：安装Python（5分钟）

#### 选项A：官方安装包（推荐）

1. **下载安装包**
   - 访问：https://www.python.org/downloads/windows/
   - 下载 **Python 3.10.x** 或更高版本的 Windows installer (64-bit)

2. **运行安装程序**
   ```
   ⚠️ 重要提示：
   ✅ 务必勾选 "Add Python to PATH" 选项
   ✅ 选择 "Install Now" 或自定义安装路径
   ```

3. **验证安装**
   打开新的PowerShell窗口，运行：
   ```powershell
   python --version
   ```
   应显示类似：`Python 3.10.11`

#### 选项B：Microsoft Store安装

1. 打开Microsoft Store应用
2. 搜索 "Python 3.12" 或 "Python 3.11"
3. 点击"获取"或"安装"
4. 安装完成后重启终端

---

### 第二步：安装项目依赖（2分钟）

安装Python后，在项目目录中运行：

```powershell
# 进入项目目录
cd "c:\Users\31477\Documents\QoderCN\2026-07-05\chat-1"

# 安装依赖包
pip install -r requirements.txt
```

预期输出：
```
Successfully installed beautifulsoup4-4.12.2 feedparser-6.0.10 lxml-4.9.3 python-dateutil-2.8.2 requests-2.31.0
```

---

### 第三步：配置企业微信Webhook

编辑 `config.py` 文件，将第2行的Webhook URL替换为您的实际地址：

```python
# 修改前
WECHAT_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY_HERE

# 修改后（示例）
WECHAT_WEBHOOK_URL=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=abcdef123456-xxxxx
```

**如何获取Webhook URL：**
1. 打开企业微信
2. 进入群聊 → 右上角"..." → 添加群机器人
3. 新建机器人，复制Webhook地址

---

### 第四步：运行本地测试

```powershell
# 运行主程序
python main.py
```

**预期输出：**
```
============================================================
🚁 低空行业每日资讯推送系统
============================================================

【步骤1】初始化模块...
✓ 模块初始化完成

【步骤2】开始抓取新闻...
正在抓取: 中国民航网...
成功从 [中国民航网] 抓取 XX 条新闻
...
总共抓取到 XX 条原始新闻

【步骤3】进行去重处理...
去重前: XX 条, 去重后: XX 条

【步骤4】筛选低空相关新闻并排序...
筛选出 XX 条低空行业相关新闻

【步骤5】格式化资讯内容...
✓ 格式化完成

【步骤6】推送到企业微信...
✅ 消息发送成功！

============================================================
✅ 今日资讯推送完成！
============================================================
```

---

### 第五步：验证结果

✅ **成功的标志：**
1. 控制台显示上述成功信息
2. 企业微信收到包含10条资讯的消息
3. 消息格式美观，带有标题、链接和相关度评分

❌ **如果失败：**
- 检查错误信息
- 确认Webhook URL正确
- 查看网络连接是否正常

---

## 🚀 快速命令汇总

```powershell
# 1. 检查Python版本
python --version

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行测试
python main.py

# 4. 仅测试微信推送
python wechat_bot.py
```

---

## 💡 常见问题

### Q1: 安装Python后仍然提示"Python was not found"？
**解决：** 
- 重启PowerShell或CMD窗口
- 检查环境变量PATH中是否包含Python路径
- 重新安装Python并确保勾选"Add to PATH"

### Q2: pip命令找不到？
**解决：**
```powershell
# 尝试使用
py -m pip install -r requirements.txt
# 或
python -m pip install -r requirements.txt
```

### Q3: 安装依赖时出错？
**解决：**
```powershell
# 升级pip
python -m pip install --upgrade pip

# 重新安装
pip install -r requirements.txt
```

### Q4: 不想安装Python，只想测试GitHub Actions？
**解决：**
可以直接将代码推送到GitHub，通过Actions进行云端测试，无需本地Python环境。

---

## 🎯 下一步

安装Python并完成本地测试后，您可以：

1. **调整配置**
   - 修改资讯源（config.py）
   - 调整关键词列表
   - 更改推送数量

2. **部署到GitHub**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

3. **配置定时任务**
   - 在GitHub仓库Settings中添加Secrets
   - 启用GitHub Actions自动执行

---

**需要帮助？**
- 查看 README.md 完整文档
- 查看 QUICKSTART.md 快速开始指南
- 随时向我提问！
