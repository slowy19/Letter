# from io import BytesIO
# from PIL import Image

# from django.core.files import File
# from django.db import models


# class CustomUser(models.Model):
    
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(null=True, max_length=150, blank=True)
#     last_name = models.CharField(null=True, max_length=150, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
#     thumbnail = models.ImageField(upload_to='avatars/', null=True, blank=True)
    
#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
    
#     class Meta:
#         db_table = 'auth_user'
        
#     def __str__(self):
#         return self.username
    
#     def get_image(self):
#         if self.avatar:
#             return 'http://127.0.0.1:8000' + self.avatar.url
#         return ''
    
#     def get_thumbnail(self):
#         if self.thumbnail:
#             return 'http://127.0.0.1:8000' + self.thumbnail.url
#         else:
#             if self.avatar:
#                 self.thumbnail = self.make_thumbnail(self.avatar)
#                 self.save()

#                 return 'http://127.0.0.1:8000' + self.thumbnail.url
#             else:
#                 return ''
            
#     def make_thumbnail(self, avatar, size=(60, 60)):
#         img = Image.open(avatar)
#         img.convert('RGB')
#         img.thumbnail(size)

#         thumb_io = BytesIO()
#         img.save(thumb_io, 'JPEG', quality=85)

#         thumbnail = File(thumb_io, name=avatar.name)

#         return thumbnail