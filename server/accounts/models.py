from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
    def __str__(self):
        return self.username
    
    def get_image(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.avatar:
                self.thumbnail = self.make_thumbnail(self.avatar)
                self.save()

                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
            
    def make_thumbnail(self, avatar, size=(60, 60)):
        img = Image.open(avatar)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=avatar.name)

        return thumbnail