from django.db import models

# Create your models here.

class department(models.Model):
	#dept_id=models.AutoField(primary_key=True,default=0)
	dept_name=models.CharField(max_length=100)

	def __str__(self):
		return self.dept_name

class employee(models.Model):
	#emp_id=models.AutoField(primary_key=True,default=0)
	emp_dept=models.ForeignKey('department',on_delete=models.CASCADE,)
	emp_name=models.CharField(max_length=100,unique=True)
	emp_age=models.IntegerField(unique=True)
	

	def __str__(self):
		return self.emp_name
