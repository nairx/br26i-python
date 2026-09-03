from apscheduler.schedulers.blocking import BlockingScheduler
def backup_database():
    print("Database backup started")
scheduler = BlockingScheduler()
# scheduler.add_job(backup_database,"interval",seconds=5)
scheduler.add_job(backup_database,"cron",day_of_week="mon,wed,fri",hour=9,minute=0)
scheduler.start()

#taskschd.msc