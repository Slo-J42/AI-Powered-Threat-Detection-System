import os, smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_alert_email(anomalies_df):
    sender = os.getenv('EMAIL_SENDER')
    password = os.getenv('EMAIL_PASSWORD')
    recipient = os.getenv('EMAIL_RECEIVER')
    if not sender or not password or not recipient:
        print('❌ Environment variables not loaded.')
        return
    msg = MIMEText(f'⚠️ AI Threat Detection Alert:\n\n{anomalies_df.to_string(index=False)}')
    msg['Subject'] = '🔐 ALERT: Anomalies Detected'
    msg['From'] = sender
    msg['To'] = recipient
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, [recipient], msg.as_string())
        print('📧 Email alert sent!')
    except Exception as e:
        print(f'❌ Email failed: {e}')