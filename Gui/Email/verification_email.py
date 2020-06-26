import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

"""
To read from an email list (for in loop) :
    email_list = [line.strip() for line in open('email.txt')]

SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.

IMPORTANT: Gmail only supports inline CSS

"""

aids_email = 'airbaseddeploymentsystem@gmail.com'
aids_password = 'sethes2aids'
from_email = aids_email
to_email = [""]  # recipient

try:

    smtp_conn = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_conn.ehlo()
    smtp_conn.starttls()
    smtp_conn.login(aids_email, aids_password)

    msg = MIMEMultipart("alternative")
    msg['Subject'] = "Reset your Password"
    msg['From'] = from_email
    msg['To'] = to_email[0]

    # Display AIDS logo
    fp = open('../Gui/Resources/aids_logo_2.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<aids_logo_2>')

    html = """\
    <html>
        <body>
            <div class="container" style="font-family:Helvetica; margin: auto 20%;"> 
                <img src="cid:aids_logo_2">
                <h1 style="text-align: center;">Password Change Request</h1>
                <div class="contents" style="font-size: 17px;">
                    <p>Hi (User),</p>
                    <p>You recently requested to reset your password for your AIDS account <u>(insert user ID)</u>
                    through your email address. Your verification code is:</p>
                    <!-- generated code -->
                    <p style="font-size: 40px; margin-bottom: 10px; font-weight: bold; text-align: center;">PSU92HT</p> 
                    <p style=" font-style: italic; padding-bottom: 20px; text-align: center;">
                    Verification code is only valid for 30 minutes after you receive this email.</p>
                    <p>If you did not request a password reset, you can safely ignore this email. Only a person with 
                    access to your email can reset your account password.</p>
                    <p style="padding-top: 20px; font-size: 15px; color: #808080;">AIDS Team</p>
                </div>
            </div>
        </body>
    </html>
    """
    html_msg = MIMEText(html, "html")

    msg.attach(msgImage)
    msg.attach(html_msg)

    smtp_conn.sendmail(from_email, to_email, msg.as_string())
    smtp_conn.quit()

except smtplib.SMTPException:

    print("Error sending message.")
