# Generated by Django 5.0.2 on 2024-02-28 03:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_subject_subjectmarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmarks',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subjectmarks',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vege.subject'),
        ),
        migrations.AlterField(
            model_name='subjectmarks',
            name='student',
            field=models.ForeignKey(db_column='student_id', on_delete=django.db.models.deletion.CASCADE, related_name='studentmarks', to='vege.student'),
        ),
        migrations.AlterUniqueTogether(
            name='subjectmarks',
            unique_together={('student', 'subject')},
        ),
    ]