import shutil
import os
import datetime

def backup_file(source,destination):
    today=datetime.date.today()
    backup_file_name=os.path.join(destination, f"backup {today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz',''),'gztar',source)

source=r"D:\python_backup_services"
destination=r"D:\python_backup_services\backups"
backup_file(source,destination)
