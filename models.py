from django.db import models

# Question Model

class Question(models.Model):

    text = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.text

# Choice Model

class Choice(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    text = models.CharField(max_length=255)

    is_correct = models.BooleanField(default=False)

    def __str__(self):

        return self.text

# Submission Model

class Submission(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    submitted_at = models.DateTimeField(auto_now_add=True)
