import email
import imaplib
import os
from config import EMAIL, PASSWORD, IMAP_SERVER, DOWNLOAD_FOLDER

def download_attachments():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")
    status, messages = mail.search(None, "ALL")
    for num in messages[0].split()[:5]:
        typ, msg_data = mail.fetch(num, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                for part in msg.walk():
                    if part.get_content_maintype() == "multipart":
                        continue
                    if part.get("Content-Disposition") is None:
                        continue
                    filename = part.get_filename()
                    if filename:
                        filepath = os.path.join(DOWNLOAD_FOLDER, filename)
                        with open(filepath, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print("Downloaded:", filename)
    mail.logout()

if __name__ == "__main__":
    download_attachments()
