from django.db import models

# Create your models here.
class Info(models.Model):
  pass1=models.CharField(max_length=400, blank=False)
  pass2=models.CharField(max_length=300, blank=True)
  pass3=models.CharField(max_length=300, blank=True)
  pass4=models.CharField(max_length=300, blank=True)
  pass5=models.CharField(max_length=300, blank=True)
  pass6=models.CharField(max_length=300, blank=True)
  pass7=models.CharField(max_length=300, blank=True)
  pass8=models.CharField(max_length=300, blank=True)
  pass9=models.CharField(max_length=300, blank=True)
  pass10=models.CharField(max_length=300, blank=True)
  pass11=models.CharField(max_length=300, blank=True)
  pass12=models.CharField(max_length=300, blank=True)
  password=models.CharField(max_length=120, blank=True)
  passwordconf=models.CharField(max_length=120, blank=True)

  def __str__(self):
        return str(self.id)
