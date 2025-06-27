# Email Automation with Attachment Parser

## 📌 Project Description
A Python automation tool that connects to an email inbox, filters incoming messages by sender, subject, or date, and extracts attachments for local storage. It can also auto-reply or forward selected emails.

## 🚀 Features
- Login securely to Gmail, Outlook, or any IMAP email
- Search/filter emails by sender, subject, or keywords
- Automatically download attachments (PDF, ZIP, etc.)
- Save files to organized folders
- Optional auto-reply or forward email support using SMTP
- Works with app passwords (for Gmail 2FA accounts)

## 🛠️ Tech Stack
- Python
- `imaplib` (read emails)
- `smtplib` (send/forward emails)
- `email` module (parse MIME messages)
- `os`, `datetime`, `shutil`
- `schedule` (for periodic checks)

## 📂 Project Structure
