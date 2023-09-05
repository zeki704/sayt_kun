from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=128)
    is_menu = models.BooleanField()


    def __str__(self):
        return self.name

class News(models.Model):

    objects = None
    title = models.CharField(max_length=256)
    short_desc = models.TextField()
    desc = models.TextField()
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    view = models.IntegerField(default=0)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    ism = models.CharField(max_length=128)
    tel = models.CharField(max_length=50)
    massage = models.TextField()
    is_trash = models.BooleanField(default=False)
    is_view = models.BooleanField(default=False)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f"Name: {self.ism}"

class Comments(models.Model):
    user = models.CharField(max_length=128)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    trash = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.trash} | {self.comment}"