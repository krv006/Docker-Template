import subprocess
import os
from datetime import datetime


def get_input(prompt):
    return input(prompt)


def run_backup(source_db, user, password):
    backup_dir = "/backups/"
    timestamp = datetime.now().strftime("%d-%m-%Y-%I-%M-%S")
    file_name = os.path.join(backup_dir, f"{timestamp}.tar")

    command = [
        "pg_dump",
        "-U", user,
        "-h", "localhost",
        "-d", source_db,
        "-F", "tar",
        "-f", file_name
    ]

    env = os.environ.copy()
    env["PGPASSWORD"] = password

    try:
        subprocess.run(command, env=env, check=True)
        print("Zaxira muvaffaqiyatli amalga oshirildi:", file_name)
    except subprocess.CalledProcessError as e:
        print(f"Xatolik yuz berdi: {e}")


def main():
    source_db = get_input("Source database nomini kiriting: ")
    user = get_input("PostgreSQL foydalanuvchi nomini kiriting: ")
    password = get_input("Foydalanuvchi parolini kiriting: ")

    run_backup(source_db, user, password)


if __name__ == "__main__":
    main()
