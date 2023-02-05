from celery import shared_task

@shared_task(bind = True)
def GetProdcutData(self):
    for i in range(100):
        print(i)
    return 'Done'