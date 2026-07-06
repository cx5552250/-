# ✅ 部署前检查清单

在将项目推送到GitHub之前，请完成以下检查：

## 📋 必须完成的配置

### 1. 企业微信Webhook配置 ✓

- [ ] 已注册企业微信账号
- [ ] 已创建群聊并添加机器人
- [ ] 已复制Webhook URL（格式：`https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx`）
- [ ] 已在GitHub Secrets中配置 `WECHAT_WEBHOOK_URL`

**验证方法：**
```bash
# 本地测试（可选）
python wechat_bot.py
```

### 2. GitHub仓库设置 ✓

- [ ] 已将代码推送到GitHub（或Fork本仓库）
- [ ] 已确认 `.github/workflows/daily_news_push.yml` 存在
- [ ] 已在Settings → Secrets中配置Webhook URL
- [ ] 已手动触发一次工作流测试

**验证步骤：**
1. 进入仓库 → Actions标签
2. 点击 "Run workflow"
3. 等待执行完成（绿色✓）
4. 检查企业微信是否收到消息

### 3. 资讯源配置（可选调整）

当前配置的资讯源：
- [x] 中国民航网 (caacnews.com.cn)
- [x] 低空经济观察 (lowaltitude.com)
- [x] 无人机世界 (uavworlds.com)

**如需添加更多资讯源：**
- [ ] 编辑 `config.py` 中的 `NEWS_SOURCES` 列表
- [ ] 在 `crawler.py` 中添加对应的解析方法

### 4. 关键词配置（建议检查）

当前关键词列表包含：
- 低空经济、无人机、eVTOL、电动垂直起降
- 通用航空、飞行汽车、空中交通
- 低空物流、城市空运、UAM
- 适航认证、空域管理、低空监管等

**如需调整：**
- [ ] 编辑 `config.py` 中的 `KEYWORDS` 列表
- [ ] 添加您特别关注的细分领域词汇

## 🔍 功能测试清单

### 本地测试（推荐先做）

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置Webhook（编辑config.py）
# WECHAT_WEBHOOK_URL = "您的webhook地址"

# 3. 运行主程序
python main.py

# 预期结果：
# ✓ 控制台显示抓取进度
# ✓ 企业微信收到10条资讯
# ✓ 消息格式美观，包含标题和链接
```

### GitHub Actions测试

- [ ] 手动触发工作流
- [ ] 查看执行日志无错误
- [ ] 企业微信收到推送
- [ ] 推送时间符合预期

## ⚙️ 配置项检查

### config.py

```python
# 检查以下配置是否正确
WECHAT_WEBHOOK_URL = "..."  # ✓ 已配置（通过Secrets）
NEWS_SOURCES = [...]        # ✓ 至少3个资讯源
KEYWORDS = [...]            # ✓ 包含核心关键词
MAX_NEWS_COUNT = 10         # ✓ 推送10条
DEBUG = False               # ✓ 生产环境设为False
```

### .github/workflows/daily_news_push.yml

```yaml
# 检查定时配置
schedule:
  - cron: '0 0 * * *'  # ✓ 每天UTC 0点（北京时间8点）
  
# 检查Secrets引用
env:
  WECHAT_WEBHOOK_URL: ${{ secrets.WECHAT_WEBHOOK_URL }}  # ✓ 正确引用
```

## 🐛 常见问题自查

### 如果收不到消息

- [ ] Webhook URL是否正确？（检查Secrets）
- [ ] 企业微信机器人是否正常？（在群里@机器人测试）
- [ ] GitHub Actions是否执行成功？（查看日志）
- [ ] 网络连接是否正常？

### 如果抓取的新闻不准确

- [ ] 关键词列表是否覆盖全面？
- [ ] 资讯源是否有足够的低空行业内容？
- [ ] 评分算法是否需要调整？

### 如果GitHub Actions失败

- [ ] 查看Actions标签页的错误日志
- [ ] 确认requirements.txt中的依赖都可安装
- [ ] 检查Python版本兼容性（需要3.8+）

## 📊 性能基准

正常执行情况：
- 总执行时间：30-60秒
- 抓取资讯源：3个
- 原始新闻量：50-200条
- 筛选后相关：20-50条
- 最终推送：10条

## ✨ 上线后的维护

### 每周检查
- [ ] 查看过去7天的推送记录
- [ ] 确认资讯质量和相关性
- [ ] 检查是否有失败的执行

### 每月优化
- [ ] 根据阅读反馈调整关键词
- [ ] 添加新的优质资讯源
- [ ] 移除低质量或失效的资讯源
- [ ] 更新过时的解析规则

### 每季度回顾
- [ ] 评估系统整体效果
- [ ] 考虑添加新功能（如AI摘要）
- [ ] 优化评分算法
- [ ] 扩展推送渠道（如邮件备份）

## 🎯 成功标准

系统正常运行的标志：

✅ 每天准时收到推送（北京时间8点）
✅ 每条资讯都与低空行业相关
✅ 资讯热度排序合理（最重要的在前）
✅ 消息格式清晰美观
✅ 链接可正常访问
✅ 无重复内容
✅ GitHub Actions全部执行成功

---

## 🚀 开始使用

完成以上检查后，您就可以：

1. **提交代码到GitHub**
   ```bash
   git add .
   git commit -m "Initial commit: 低空行业资讯推送系统"
   git push origin main
   ```

2. **配置GitHub Secrets**
   - Settings → Secrets and variables → Actions
   - 添加 `WECHAT_WEBHOOK_URL`

3. **首次测试**
   - Actions → Run workflow
   - 等待执行完成
   - 检查企业微信消息

4. **确认定时任务**
   - 第二天早上8点检查是否自动推送
   - 如未收到，查看Actions日志排查

---

**祝您使用愉快！如有问题，请查阅README.md或ARCHITECTURE.md文档。** 🚁
