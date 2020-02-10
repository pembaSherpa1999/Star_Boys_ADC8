# Generated by Django 3.0.2 on 2020-02-09 03:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=200)),
                ('doctorName', models.CharField(max_length=200)),
                ('Date', models.DateField(max_length=100)),
                ('Time', models.TimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BillNo', models.IntegerField()),
                ('PatientName', models.CharField(max_length=10)),
                ('Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depName', models.CharField(max_length=200)),
                ('doctorID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=20)),
                ('Contact', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('education', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Address', models.CharField(max_length=20)),
                ('Contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=20)),
                ('PhoneNo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=250)),
                ('patientAddress', models.CharField(max_length=20)),
                ('patientPhoneNo', models.IntegerField()),
                ('patientAge', models.IntegerField()),
                ('patientSex', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='patientPic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictureName', models.CharField(max_length=25)),
                ('profilePic', models.ImageField(upload_to='')),
                ('aboutPic', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.CharField(max_length=100)),
                ('types', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RoomNO', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Address', models.CharField(max_length=10)),
                ('Position', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TestOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientID', models.CharField(max_length=254)),
                ('PatientName', models.CharField(max_length=254)),
                ('prescribeMedicine', models.CharField(max_length=254)),
                ('prescribeTratment', models.CharField(max_length=200)),
                ('report', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StaffLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('Staffname', models.ManyToManyField(blank=True, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]