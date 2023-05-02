#encoding:utf-8

'''
Python 发送邮件步骤：
    1.导入必须库
    2.准备邮件服务信息
    3.设置邮件内容信息
    4.模拟登陆邮箱服务
    5.发送邮件
'''
# 1.导入必须库
import smtplib                                      # 发送邮件
from email.header import Header                     # 写邮件 主题
from email.mime.multipart import MIMEMultipart      # 写邮件 主体
from email.mime.text import MIMEText                # 写邮件 主体正文内容：文本

# 2.准备邮件服务信息
hostid = 'smtp.163.com'                             # 服务器地址
email_username = ''       # 账号（发件人地址）
email_password = ''                 # 密码
email_to = ''             # 收件人地址（可以和发件人地址一样）

# 3.设置邮件内容信息
# 构建邮件主体
email_body = MIMEMultipart('related')
# 3.1 完善邮件内容
email_body['From'] = email_username
email_body['To'] = email_to
email_body['Subject'] = Header('快去查看', 'utf-8')
# 3.2 完善邮件正文
email_content = '点击查看👉'
html = '''
<html>
    <head></head>
    <body>
        <p>
            <a href="#">👉点击查看</a>
        </p>
    </body>
</html>
'''
email_html = MIMEText(html, 'html', 'utf-8')       # 创建邮件正文      # 创建邮件正文
email_body.attach(email_html)                                # 将 邮件正文 绑定至 邮件主体
# 4.模拟登陆邮箱服务
# 创建邮箱服务器连接对象
smtp_Obj = smtplib.SMTP_SSL(hostid, 465)        # 465 是服务器端口号
# 登录邮箱
smtp_Obj.login(email_username, email_password)

# 5.发送邮件
# 发送邮件
smtp_Obj.sendmail(email_username, email_to, email_body.as_string())
# 关闭连接
smtp_Obj.quit()


