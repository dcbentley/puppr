from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(('email'), null=True, blank=True, max_length=254)
    pup_name = models.CharField(max_length=100)
    profile_img_url = models.TextField()

    def __str__(self):
        return self.email


class UserPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User')
    post = models.CharField(max_length=280)

    def __str__(self):
        return self.post
