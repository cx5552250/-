"""
企业微信机器人推送模块
负责将处理后的资讯推送到企业微信
"""

import requests
import json
import config


class WeChatBot:
    """企业微信机器人"""
    
    def __init__(self):
        self.webhook_url = config.WECHAT_WEBHOOK_URL
    
    def send_markdown_message(self, content):
        """
        发送Markdown格式消息
        
        Args:
            content: Markdown格式的文本内容
            
        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url or 'YOUR_KEY_HERE' in self.webhook_url:
            print("错误: 请先在config.py中配置企业微信机器人Webhook URL")
            return False
        
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": content
            }
        }
        
        try:
            response = requests.post(
                self.webhook_url,
                headers=headers,
                data=json.dumps(data),
                timeout=10
            )
            
            result = response.json()
            
            if result.get('errcode') == 0:
                print("✅ 消息发送成功！")
                return True
            else:
                print(f"❌ 消息发送失败: {result.get('errmsg', '未知错误')}")
                return False
                
        except Exception as e:
            print(f"❌ 发送消息时出错: {str(e)}")
            return False
    
    def send_text_message(self, content):
        """
        发送纯文本消息（备用方案）
        
        Args:
            content: 文本内容
            
        Returns:
            bool: 是否发送成功
        """
        if not self.webhook_url or 'YOUR_KEY_HERE' in self.webhook_url:
            print("错误: 请先在config.py中配置企业微信机器人Webhook URL")
            return False
        
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }
        
        data = {
            "msgtype": "text",
            "text": {
                "content": content
            }
        }
        
        try:
            response = requests.post(
                self.webhook_url,
                headers=headers,
                data=json.dumps(data),
                timeout=10
            )
            
            result = response.json()
            
            if result.get('errcode') == 0:
                print("✅ 消息发送成功！")
                return True
            else:
                print(f"❌ 消息发送失败: {result.get('errmsg', '未知错误')}")
                return False
                
        except Exception as e:
            print(f"❌ 发送消息时出错: {str(e)}")
            return False
    
    def test_connection(self):
        """
        测试与企业微信机器人的连接
        
        Returns:
            bool: 连接是否正常
        """
        test_message = "🔔 低空资讯推送系统连接测试\n\n如果您收到这条消息，说明配置成功！"
        return self.send_markdown_message(test_message)


if __name__ == '__main__':
    # 测试机器人
    bot = WeChatBot()
    
    print("正在测试企业微信机器人连接...")
    success = bot.test_connection()
    
    if success:
        print("\n✓ 测试通过！可以正常使用推送功能")
    else:
        print("\n✗ 测试失败！请检查config.py中的Webhook URL配置")
