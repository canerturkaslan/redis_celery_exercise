from __future__ import absolute_import, unicode_literals
from celery import shared_task

@shared_task(name = "print_msg_with_name")
def print_message(name, *args, **kwargs):
  print("Celery is working!! {} have implemented it correctly.".format(name))

@shared_task(name = "add_2_numbers")
def add(x, y):
  print("Add function has been called!! with params {}, {}".format(x, y))
  return x+y