from django.db import models
from users.models import User
from jobs.models import Job

class Application(models.Model):
    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'candidate'}
    )
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    match_percentage = models.FloatField(null=True, blank=True)  # for matching score
    missing_skills = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"
