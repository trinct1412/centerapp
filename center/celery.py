from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from page import kaa

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'center.settings')

include_tasks = [
]

# set the default Django settings module for the 'celery' program.
app = Celery('center', enable_utc=False, include=include_tasks)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.timezone = 'Asia/Ho_Chi_Minh'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # SYSTEM TASK
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )


@app.task
def test(arg):
    print(arg)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


if __name__ == '__main__':
    app.start()
