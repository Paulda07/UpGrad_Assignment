from celery.task import Task
from celery.registry import tasks
from Todo_App.Celery import app
# app.tasks.register(MyTaskTask())
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

user = User.objects.get(username = 'Paul')
user_email = user.email

class SignUpTask(Task):
	def run (self):
		subject, from_mail, to = 'Welcome', 'paul.samps.ledala@gmail.com', user_email

		html_content = render_to_string('email.html' )
		text_content = text_content = strip_tags(html_content)
		msg = EmailMultiAlternatives(subject, text_content, from_mail, to)
		msg.attach_alternative(html_content, "text/html")
		msg.send()

tasks.register(SignUpTask)