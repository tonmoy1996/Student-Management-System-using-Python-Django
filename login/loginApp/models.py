from django.db import models  


class Employee(models.Model):  
    
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15) 


    class Meta:  
        db_table = "employee"  