from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Movie
from django.core.mail import send_mail

@receiver(post_delete,sender=Movie)
def notify_admins(**kwargs):
    instance = kwargs.get('instance')
    print('The deleted movie {} '.format(instance))

# @receiver(post_save, sender=Movie)
# def my_handler(sender, instance, created, *args, **kwargs):
#     send_mail(
#             subject='New Movie Created Subject',
#             message='Dear user {} has been created'.format(instance.name),
#             from_email= 'hassan.tarek.hassan.ali@gmail.com',
#             recipient_list=['hassantarekha@gmail.com','sahar.mamdouh93@gmail.com'],
#             fail_silently=False
#             )  