from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    pass

    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.set_password(password)
        self.save()

    def new_note(self, data):
        note = Note()
        note.Message = data['note-text']
        note.User = self
        note.save()


class Note(models.Model):
    Message = models.TextField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
