import os
import sys
import time
import schedule
import shutil
import hashlib
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuration for Email (Update with your credentials)
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "receiver_email@gmail.com"

# --- New Features Logic ---

def Send_Email(log_file, zip_file):
    """Sends email with log and zip attachments"""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"Backup Completion Report - {time.ctime()}"
        
        body = "The scheduled backup has been completed successfully. Please find the log and backup files attached."
        msg.attach(MIMEText(body, 'plain'))

        for file_path in [log_file, zip_file]:
            if os.path.exists(file_path):
                with open(file_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(file_path)}")
                    msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def Restore_Backup(zip_name, destination):
    """Extracts backup to a given directory"""
    try:
        if not os.path.exists(zip_name):
            print(f"Error: {zip_name} not found.")
            return
        
        with zipfile.ZipFile(zip_name, 'r') as zip_ref:
            zip_ref.extractall(destination)
        print(f"Backup restored successfully to: {destination}")
    except Exception as e:
        print(f"Restoration failed: {e}")

def Update_History(zip_name, file_count, zip_size):
    """Maintains a backup history tracker file"""
    history_file = "backup_history.txt"
    with open(history_file, "a") as h_obj:
        h_obj.write(f"Date: {time.ctime()} | Files: {file_count} | Size: {zip_size} bytes | File: {zip_name}\n")

def Display_History():
    """Displays history from the tracker file"""
    history_file = "backup_history.txt"
    if os.path.exists(history_file):
        with open(history_file, "r") as f:
            print(f.read())
    else:
        print("No history found.")

# --- Existing Logic with Enhancements ---

def make_zip(folder, exclude_ext):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(folder):
        for file in files:
            # Feature 4: Exclude files/folders
            if any(file.endswith(ext) for ext in exclude_ext):
                continue
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, folder)
            zobj.write(full_path, relative)
    zobj.close()
    return zip_name

def Calculate_Hash(path):
    hobj = hashlib.md5()
    with open(path, "rb") as fobj:
        while True:
            Data = fobj.read(1024)
            if not Data: break
            hobj.update(Data)
    return hobj.hexdigest()

def BackupFiles(Source, Destination, exclude_ext):
    copied_files = []
    os.makedirs(Destination, exist_ok=True)
    for root, dirs, files in os.walk(Source):
        for file in files:
            if any(file.endswith(ext) for ext in exclude_ext):
                continue
            src_path = os.path.join(root, file)
            relative = os.path.relpath(src_path, Source)
            dest_path = os.path.join(Destination, relative)
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            if (not os.path.exists(dest_path)) or (Calculate_Hash(src_path) != Calculate_Hash(dest_path)):
                shutil.copy2(src_path, dest_path)
                copied_files.append(relative)
    return copied_files

def MarvellousDataShieldStart(Source="Data"):
    start_time = time.ctime()
    log_dir = "Logs"
    os.makedirs(log_dir, exist_ok=True)
    log_name = os.path.join(log_dir, f"log_{time.strftime('%Y%m%d_%H%M%S')}.txt")
    
    exclude_ext = ['.tmp', '.log', '.exe'] # Standard exclusions
    
    try:
        BackupName = "Marvellous_Backup"
        files = BackupFiles(Source, BackupName, exclude_ext)
        zip_file = make_zip(BackupName, exclude_ext)
        zip_size = os.path.getsize(zip_file)

        # Feature 1: Logging System
        with open(log_name, "w") as l_obj:
            l_obj.write(f"Backup Start: {start_time}\nFiles Copied: {len(files)}\nZip Name: {zip_file}\n")
            l_obj.write("Errors: None\n")
        
        Update_History(zip_file, len(files), zip_size)
        
        # Feature 2: Email Notification
        Send_Email(log_name, zip_file)

        print(f"Backup completed. Log: {log_name}")
    except Exception as e:
        with open(log_name, "a") as l_obj:
            l_obj.write(f"Errors: {str(e)}\n")

def main():
    Border = "-" * 50
    print(f"\n{Border}\n----------Marvellous Data Shield System-----------\n{Border}")

    if len(sys.argv) < 2:
        print("Use --h for help.")
        return

    option = sys.argv[1].lower()

    if option == "--h":
        print("Options:\n--u : Usage\n--restore [ZipFile] [Dest] : Restore backup\n--history : Show history")
    elif option == "--u":
        print("Usage: Script.py [Interval] [SourceDir]")
    elif option == "--restore" and len(sys.argv) == 4:
        Restore_Backup(sys.argv[2], sys.argv[3])
    elif option == "--history":
        Display_History()
    elif len(sys.argv) == 3:
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])
        MarvellousDataShieldStart(sys.argv[2]) # Initial Run
        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid Arguments.")

if __name__ == "__main__":
    main()