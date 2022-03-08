from datetime import timedelta
from arike.celery import app
import time

# @app.on_after_finalize.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # call every 5 seconds
#     sender.add_periodic_task(5.0,myname.s('hero'), name="run every 5")

# app.conf.timezone = 'UTC'

@app.task
def heavyCalc(number):
    LIMIT = 500
    iterations = min(LIMIT,number)
    print(f"[STARTED] Process started for *{iterations}* iterations")
    for x in range(iterations):
        print(f'iteration: {x}')
        time.sleep(1)
    print(f"[Completed] Process completed *{iterations}* iterations")


# Task
@app.task
def myname(name):
    print("My name is: " + name)

# Alternate configure
app.conf.beat_schedule = {
    'run every 60 sec': {
        'task': 'app_admin.tasks.myname',
        'schedule': 60.0,
        'args':('ravinder',),
    },
}