# Generated by Django 4.2.4 on 2023-09-07 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_complaint_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('waiting', 'waiting'), ('approved', 'approved'), ('rejected', 'rejected')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
