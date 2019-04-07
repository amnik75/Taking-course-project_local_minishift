# Generated by Django 2.1.3 on 2018-12-28 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chooseClass', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ManyToManyField(blank=True, to='chooseClass.Class')),
                ('student', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='login.Student')),
            ],
        ),
    ]
