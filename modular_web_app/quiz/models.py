from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return f"Question {self.id} for {self.topic.name}"
    
class QuizSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)
    date_taken = models.DateTimeField(default=now)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return f"QuizSession {self.id} for {self.user.username} - {self.topic.name}"




