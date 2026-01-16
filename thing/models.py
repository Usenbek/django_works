from django.db import models

# Create your models here.
"""
create table thing (
    id integer primary key,
    name string,
    )
"""

class Category(models.Model):
   name = models.CharField(max_length=128)
   created_at = models.DateTimeField(auto_now_add=True, null = True)
   updated_at = models.DateTimeField(auto_now=True, null = True)

   def __str__(self):
       return f"{self.name}"


class Thing(models.Model):
  photo = models.ImageField(null = True, blank = True, upload_to='thing/')
  Title = models.CharField(max_length=100)
  description = models.TextField()
  value = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True, blank = True)
  posted_at = models.DateTimeField(auto_now_add=True, null = True)
  updated_at = models.DateTimeField(auto_now=True, null = True)
  
  def __str__(self):
      return f"{self.Title}"