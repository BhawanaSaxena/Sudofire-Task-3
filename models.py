from django.db import models





class Company(models.Model):
    primary_id = models.AutoField(primary_key=True) #id is auto set to True
    name= models.CharField(max_length=55)
    location=models.CharField(max_length=55)
    type = models.CharField(max_length=100,choices=(("rural","rural/remote"),
                                                    ("urban","small town/big city"),
                                                    ("Others","Others")))
    date_of_entry = models.DateField(auto_now=True)
    active_id = models.BooleanField(default=True)

    #added user model ,related : onetoone related to company

    user = models.OneToOneField(user,on_delete=models.CASCADE)
