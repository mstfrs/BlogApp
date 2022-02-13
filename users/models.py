from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# class Users(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
    
   
#     def __str__(self):
#         return self.username
    
# class Profile(models.Model):
#     user=models.OneToOneField(User ,on_delete=models.CASCADE)
#     image=models.ImageField(blank=True,upload_to='media/')
#     bio=models.TextField(blank=True, null=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_images')
    

    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path) # Open image
        
        # resize image
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size) # Resize image
        #     img.save(self.image.path) # Save it again and override the larger image
   
    