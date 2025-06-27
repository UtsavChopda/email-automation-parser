import smtplib
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT

def send_auto_reply(to_email, subject):
    msg = MIMEText("Thank you for your email. We will get back to you shortly.")
    msg["Subject"] = f"Re: {subject}"
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
        print("Auto-reply sent to", to_email)

if __name__ == "__main__":
    send_auto_reply("example@example.com", "Test Subject")
