# Generated by Django 4.2.3 on 2023-08-04 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0005_alter_job_experience_level_alter_job_job_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='application_instructions',
        ),
        migrations.RemoveField(
            model_name='job',
            name='benefits',
        ),
        migrations.AlterField(
            model_name='job',
            name='experience_level',
            field=models.CharField(choices=[('Mid Level', 'Mid Level'), ('Senior Level', 'Senior Level'), ('Entry Level', 'Entry Level')], default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('Contract', 'Contract'), ('Part-Time', 'Part-Time'), ('Temporary', 'Temporary'), ('Full-Time', 'Full-Time')], default=0, max_length=50),
        ),
    ]