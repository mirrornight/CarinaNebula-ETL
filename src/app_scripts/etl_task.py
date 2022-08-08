from src.celery_app import app


@app.task
def etl_task_example(start=None, end=None, has_run=True):
    pass