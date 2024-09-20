from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student, Instructor
import logging

@receiver(post_save, sender=Student)
def student_post_save(sender, instance, created, **kwargs):
    if created:
        send_mail(subject='New Student Added')
        message=(f'A new student has been added to the course called {instance.coursename}!')

        recipient_list=['teacher@university.edu']
    else:
        print(f'New student has been saved to {sender.coursename}')


logger = logging.getLogger(__name__)

@receiver(post_save, sender=Instructor)
def log_a_new_instructor(sender, instance, created, **kwargs):
    if created:
        logger.info(f'New instructor added, {instance.instructorname}')   

@receiver(post_delete, sender=Instructor)
def delete_instructor(sender, instance, **kwargs):
    print(f'This instructor, {instance.instructorname}, has been removed')
    

