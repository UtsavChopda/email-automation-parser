import imaplib
import email
from config import EMAIL, PASSWORD, IMAP_SERVER

def read_emails():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    status, messages = mail.search(None, "ALL")
    for num in messages[0].split()[:5]:
        typ, msg_data = mail.fetch(num, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                print("From:", msg["from"])
                print("Subject:", msg["subject"])
                print("-" * 50)
    mail.logout()

if __name__ == "__main__":
    read_emails()
