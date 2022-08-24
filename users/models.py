from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # i.e. if user is deleted delete the profile, but if profile is deleted don't delete user
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
    # self as an argument means the instance 
        return f'{self.user.username} Profile'
    
    def save(self):
        super().save()
        img=Image.open(self.image.path)
        # opens image of current instance
        if img.height>300 or img.width>300:
                output_size=(300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        # check amount of pixels in image, if greater than some threshold, resize
# Create your models here.
