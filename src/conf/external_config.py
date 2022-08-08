global_conf = {
}

component_conf = {
    'celery_conf': {
        'redis_url': 'redis:6379',
        'processor_conf_dict': {
            'etl_task_example': {
                'schedule': {'hour': '0', 'minute': '0', 'day_of_month': '6', 'month_of_year': '12'},
                'kwargs': {'start': "2021-01-01 00:00:00", 'end': "2021-10-01 00:00:00", 'has_run': False},
            },
        }
    }
}