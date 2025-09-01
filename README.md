# 🗂️ Backup Script

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-green)

A simple and powerful **Python script** to backup your folders, upload them to Google Drive, and receive **email notifications** automatically.  

---

## 🚀 Features

- 📦 Compress any folder into a **timestamped ZIP**  
- ☁️ Upload backups to a **specific Google Drive folder**  
- ✉️ Send email notifications for **success or failure**  
- 📝 Log all operations in `backup.log`  
- 🔐 Easy configuration using a `.env` file  

---

## ⚡ Requirements

- Python 3.11+  
- Dependencies in `requirements.txt`:
```bash
python-dotenv
pydrive2
```

- Gmail account for notifications (SMTP)  
- Google Drive folder to store backups  

---

## ⚙️ Setup

1. **Clone the repository**:

```bash
git clone https://github.com/cmartingu/backup_drive.git
cd backup_drive
```

2. **Create and activate a virtual environment**:
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Go to the /src folder and place configuration files**:
In /src, you must have:
- backup.py (the main script)
- backup_utils.py (utils for the main script)
- .env (environment variables)
- client_secrets.json (Google OAuth credentials file)

5. **Configure your .env**:
```src/.env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_smtp_app_password
DRIVE_FOLDER_ID=your_google_drive_folder_id
```

## 🏃 Usage
Run the script:
```bash
cd src
python backup.py
```

- Enter the path of the folder you want to backup.
- The script will:
    - Compress it into a ZIP file
    - Upload it to Google Drive
    - Log the process in backup.log
    - Send an email notification

## 📂 Logging
All operations are logged in src/backup.log for easy monitoring and troubleshooting.

## 💡 Notes
Every run requires Google Drive authentication via browser.

Make sure DRIVE_FOLDER_ID corresponds to the folder in your Google Drive where backups will be stored.

## 📝 License
This project is MIT licensed.