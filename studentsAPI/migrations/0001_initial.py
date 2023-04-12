# Generated by Django 4.2 on 2023-04-12 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=50)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField(null=True)),
                ('mobile', models.IntegerField(null=True)),
                ('createdDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('modifiedDate', models.DateTimeField(auto_now=True, null=True)),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentsAPI.class')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='studentsAPI.country')),
            ],
        ),
    ]
