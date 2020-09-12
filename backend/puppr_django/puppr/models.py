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


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    post = models.CharField(max_length=280)

    def __str__(self):
        return self.post


# class UserPosts(models.Model):
#     def with_counts(self):
#         from django.db import connection
#         with connection.cursor() as cursor:
#             cursor.execute("""
#             SELECT * FROM puppr_post JOIN puppr_user ON puppr_post.user_id = puppr_user.id    
#             """)
#         result_list = []
