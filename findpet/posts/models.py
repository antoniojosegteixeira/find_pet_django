from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    age = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=20, null=True, blank=True)
    species = models.CharField(max_length=20)
    breed = models.CharField(max_length=30, null=True, blank=True)
    color = models.CharField(max_length=30)
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    post_type = models.CharField(
        max_length=20,)
    is_resolved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="posts", null=True)

    def __str__(self) -> str:
        return self.name


class PostImage(models.Model):
    image = models.ImageField(upload_to="images", null=True, blank=True)
    post = models.ForeignKey(
        "posts.Post", on_delete=models.CASCADE, related_name="images", null=True)

    def __str__(self) -> str:
        return str(self.id)
