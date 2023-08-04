from django.db import models


CATEGORY_CHOICES = {
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
    ('Contract', 'Contract'),
    ('Temporary', 'Temporary'),
}

EXPERIENCE_LEVEL = {
    ('Entry Level', 'Entry Level'),
    ('Mid Level', 'Mid Level'),
    ('Senior Level', 'Senior Level'),
}

class Job(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # deadline = models.DateTimeField(auto_now_add=True)
    # job_type = models.CharField(choices= CATEGORY_CHOICES, max_length=2)
    job_type = models.CharField(max_length=50, choices=  CATEGORY_CHOICES)
    experience_level = models.CharField(max_length=50,choices= EXPERIENCE_LEVEL)

    # Custom Fields
    skills = models.CharField(max_length=200)
    contact_email = models.EmailField()

    def __str__(self):
        return self.title
