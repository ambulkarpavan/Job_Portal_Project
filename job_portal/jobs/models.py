from django.db import models
from users.models import User

class Job(models.Model):
    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'recruiter'}
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills = models.TextField(help_text="Comma separated skills")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
