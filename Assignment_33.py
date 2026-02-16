import os
import psutil
import sys
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# --- Configuration (Update these or use environment variables) ---
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password" # Use Google App Password

def MailSender(filename, receiver_email, summary_data):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        msg['Subject'] = f"System Report: {time.ctime()}"

        # Email Body (Summary)
        body = f"""
        Marvellous Platform Surveillance Report
        --------------------------------------
        Total Processes: {summary_data['total']}
        Top CPU Process: {summary_data['cpu'][0]} ({summary_data['cpu'][1]}%)
        Top Memory Process: {summary_data['mem'][0]} ({summary_data['mem'][1]}%)
        Top Thread Process: {summary_data['thread'][0]} ({summary_data['thread'][1]})
        Top File Process: {summary_data['files'][0]} ({summary_data['files'][1]})
        
        Please find the detailed log attached.
        """
        msg.attach(MIMEText(body, 'plain'))

        # Attachment
        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(filename)}")
            msg.attach(part)

        # SMTP Server Setup
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def CreateLog(FolderName, receiver_email):
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName, f"Marvellous_{timestamp}.log")
    
    Data = ProcessScan()
    
    # Writing detailed log
    with open(FileName, "w") as fobj:
        fobj.write("-" * 50 + "\nDetailed Process Log\n" + "-" * 50 + "\n")
        for info in Data:
            fobj.write(f"PID: {info['pid']} | Name: {info['name']} | CPU: {info['cpu_percent']}%\n")

    # Generating Summary for Email Body
    # Requirement: Top processes for CPU, Mem, Threads, Files
    summary = {
        "total": len(Data),
        "cpu": max([(p['name'], p['cpu_percent']) for p in Data], key=lambda x: x[1]),
        "mem": max([(p['name'], p['memory_percent']) for p in Data], key=lambda x: x[1]),
        "thread": max([(p['name'], p['num_threads']) for p in Data], key=lambda x: x[1]),
        "files": max([(p['name'], p['open_files'] if isinstance(p['open_files'], int) else 0) for p in Data], key=lambda x: x[1])
    }

    # Send the email
    MailSender(FileName, receiver_email, summary)

def ProcessScan():
    listprocess = []
    for proc in psutil.process_iter(attrs=["pid", "name", "username", "status", "num_threads"]):
        try:
            info = proc.info
            info["cpu_percent"] = proc.cpu_percent(interval=None)
            info["memory_percent"] = proc.memory_percent()
            try:
                files = proc.open_files()
                info["open_files"] = len(files) if files else 0
            except:
                info["open_files"] = 0
            listprocess.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return listprocess

def main():
    # Usage: script.py [Folder] [Email] [Interval]
    if len(sys.argv) == 4:
        folder = sys.argv[1]
        receiver = sys.argv[2]
        interval = int(sys.argv[3])

        print(f"Surveillance active. Sending reports to {receiver} every {interval} mins.")
        
        schedule.every(interval).minutes.do(CreateLog, folder, receiver)
        CreateLog(folder, receiver) # Initial run

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Usage: PlatformSurveillance.py [LogFolder] [ReceiverEmail] [IntervalMinutes]")

if __name__ == "__main__":
    main()