import os
import zipfile
import logging
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from dotenv import load_dotenv

# Cargar configuraciones
load_dotenv()
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
DRIVE_FOLDER_ID = os.getenv("DRIVE_FOLDER_ID")

# Logging
logging.basicConfig(
    filename="backup.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

def send_email(subject, message):
    try:
        msg = MIMEText(message)
        msg["From"] = EMAIL_USER
        msg["To"] = EMAIL_USER
        msg["Subject"] = subject

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def create_zip(folder):
    date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"backup_{date_str}.zip"
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for root, _, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                zipf.write(filepath, os.path.relpath(filepath, folder))
    return zip_name

def upload_to_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # primera vez, abre navegador
    drive = GoogleDrive(gauth)

    file_drive = drive.CreateFile({
        "title": os.path.basename(file_path),
        "parents": [{"id": DRIVE_FOLDER_ID}]
    })
    file_drive.SetContentFile(file_path)
    file_drive.Upload()
    return file_drive["id"]

def main():
    try:
        backup_folder = input("Enter the path to the folder you want to backup: ")
        zip_file = create_zip(backup_folder)
        file_id = upload_to_drive(zip_file)
        logging.info(f"Backup successful: {zip_file} -> Google Drive (ID: {file_id})")
        send_email("✅ Backup Successful", f"Backup uploaded: {zip_file} (ID: {file_id})")
    except Exception as e:
        logging.error(f"Backup failed: {e}")
        send_email("❌ Backup Failed", str(e))

if __name__ == "__main__":
    main()
