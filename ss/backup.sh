BACKUP_DIR="/home/rv/PycharmProjects/p28/backups"
FILE_NAME=$BACKUP_DIR`date +%d-%m-%Y-%I-%M-%S`.tar
PGPASSWORD='1' pg_dump -U postgres -h localhost -d p26 -F tar -f $FILE_NAME
