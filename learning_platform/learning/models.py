from django.db import models
from django.contrib.auth.models import User


class Textbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='textbooks')
    title = models.CharField(max_length=200) 
    content = models.BinaryField()

    def __str__(self):
        return self.title

class Exercise(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE, related_name='exercises') 
    page_number = models.IntegerField()
    highlight_text = models.TextField()
    exercise_text = models.TextField()

    def __str__(self):
        return f"Exercise on page {self.page_number} of {self.textbook.title}"

class Answer(models.Model):
    ANSWER_TYPES = [
        ('markdown', 'Markdown'),
        ('python', 'Python'),
    ]
    answer_type = models.CharField(max_length=10, choices=ANSWER_TYPES)  
    answer = models.TextField()
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='answers')
    created = models.DateTimeField(auto_now=True)
    edit = models.DateTimeField(default=None)

    def __str__(self):
        return f"Answer for exercise on page {self.exercise.page_number}"

class Feedback(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='feedback')
    feedback = models.TextField()
    created = models.DateTimeField(auto_now=True)
    edit = models.DateTimeField(default=None)





