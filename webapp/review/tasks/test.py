from config.celery import app

@app.task
def testMethod():
    print("test")
