from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField() #TextField는 길이제한 없음
    create_date=models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    content=models.TextField()
    create_date=models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null=True, blank=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)