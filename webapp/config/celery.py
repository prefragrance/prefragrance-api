import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

app = Celery('config',
             backend='rpc://',
             inlcude=['review.tasks'])

app.config_from_object("django.conf:settings", namespace="CELERY")

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
 	'add-every-3-hours-contrab': {
		'task': 'tasks.find_medal_standard','schedule':crontab(minute='*/60')
		# 'schedule': crontab(minute=0, hour='*/12'), #12시간마다 실행하기
	},
}

if __name__ == '__main__':
    app.start()

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
