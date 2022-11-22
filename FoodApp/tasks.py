# from __future__ import absolute_import, unicode_literals

# from celery import shared_task

# @shared_task
# def add(x, y):
#     return x + y


from celery import app
from _auth.models import CustomerProfile
import datetime
from django.conf import settings
from django.core.mail import send_mail

@app.task(name="send_notification")
def send_notification():
    try:
        customers = CustomerProfile.objects.all()

        for customer in customers:
            print(customer.user.email)
            subject = "subject"
            message = "message example"
            email_from = settings.EMAIL_HOST_USER
            reciption = "abdulrahman.fekrii@gmail.com"
            send_mail(subject, message, email_from, reciption)
    except Exception as e:
        print(e)
