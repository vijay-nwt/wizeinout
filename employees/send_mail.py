# views.py

from django.core.mail import send_mail
from django.http import HttpResponse
from postmark import PMMail


def send_test_email(request):
    subject = "Welcome to wizeinout. "
    message = "Thank you for joining NetworkWize. We're excited to have you on board!"
    sender_email ='developer@networkwize.com'
    recipient_list = ['vijay.malan@networkwize.com']

    try:
        print('Email IDs:',recipient_list)
        send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
        return HttpResponse("Test email sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send test email: {str(e)}")
    



def signup_email(request):
    subject = "Dear user you are successfully signedUp for wizeinout. "
    message = "Thank you for joining NetworkWize. We're excited to have you on board!"
    sender_email ='developer@networkwize.com'
    recipient_list = ['vijay.malan@networkwize.com']

    try:
        print('Email IDs:',recipient_list)
        send_mail(subject, message, sender_email, recipient_list, fail_silently=False)
        return HttpResponse("signed up mail sent successfully.")
    except Exception as e:
        return HttpResponse(f"Failed to send test email: {str(e)}")


