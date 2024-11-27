from django.db import models

# Create your models here.
course=[('BCA','BCA'),
('B.Voc','B.Voc'),
('MSc.Computer Science','MSc.Computer Science'),
('MSc.Data Analytics','MSc.Data Analytics')
]
batch=[('2020-2023','2020-2023'),
('2019-2022','2019-2022'),
('2018-2021','2018-2021'),
('2017-2020','2017-2020'),
]
class student(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone_no=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    admission_no=models.CharField(max_length=200,null=True)
    course=models.CharField(max_length=200,choices=course,default='NULL',null=True)
    batch=models.CharField(max_length=200,choices=batch,null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    
   
class facultyreg(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    phone_no=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    username=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)

class events(models.Model):
    eventsname=models.CharField(max_length=200,null=True)
    choose_date=models.DateField(null=True)
    image=models.ImageField(null=True,blank=True,upload_to="image")

class report(models.Model):
    event=models.CharField(max_length=200,null=True)
    report =models.ImageField(null=True,blank=True,upload_to ="images/")    