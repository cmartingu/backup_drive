from backup_utils import create_zip, upload_to_drive, send_email, logging

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
