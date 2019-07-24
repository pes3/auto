###basic example
##import pycron
'''explore cron jobs via python
'''
##import time
##
##while True:
##    if pycron.is_now('0 2 * * 0'):  # @ Sunday # 02:00
##        print('running backup')
##    time.sleep(5)
from crontab import CronTab
from datetime import datetime

cron = CronTab(tab="""* * * * * * command""")
job = cron.new(command='python hello.py')
job.minute.every(1)

cron.write()
## to be further updated
