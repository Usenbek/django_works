from django.db import models

# Create your models here.
"""
create table thing (
    id integer primary key,
    name string,
    )
"""
class Thing(models.Model):
  Title = models.CharField(max_length=100)
  description = models.TextField()
  value = models.IntegerField(default=0)
  posted_at = models.DateTimeField(auto_now_add=True, null = True)
  updated_at = models.DateTimeField(auto_now=True, null = True)
  
  def __str__(self):
      return f"{self.Title}"