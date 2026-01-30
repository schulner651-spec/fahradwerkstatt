import imaplib
import email
import smtplib
from email.message import EmailMessage
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(EMAIL, PASSWORD)
imap.select("INBOX")

status, messages = imap.search(None, "UNSEEN")

for num in messages[0].split():
    _, data = imap.fetch(num, "(RFC822)")
    msg = email.message_from_bytes(data[0][1])
    sender = msg["From"].lower()

    if "no-reply" in sender or "noreply" in sender:
        continue
    if "@google." in sender or "@microsoft." in sender:
        continue

    reply = EmailMessage()
    reply["From"] = EMAIL
    reply["To"] = msg["From"]
    reply["Subject"] = "Re: " + msg["Subject"]
    reply.set_content(
        "Hallo!\n\nDanke für deine Nachricht. "
        "Wir melden uns bald.\n\n🚲 Fahrradwerkstatt"
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(reply)

imap.logout()
