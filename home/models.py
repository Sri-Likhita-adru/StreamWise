from django.db import models

# Create your models here.

class AnalysisResult(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(null=True,max_length=100)
    school=models.CharField(null=True,max_length=100)
    field = models.CharField(max_length=255, null=True, blank=True)
    subjects = models.CharField(max_length=255, null=True, blank=True)
    Technology = models.CharField(max_length=255, null=True, blank=True)
    projects = models.CharField(max_length=255, null=True, blank=True)
    hobby =models.CharField(max_length=255, null=True, blank=True)
    goal = models.CharField(max_length=255, null=True, blank=True)
    questionnaire_summary = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    recommendations=models.CharField(max_length=1000, null=True, blank=True)
    general_report=models.CharField(max_length=1000, null=True, blank=True)
    personality_report= models.CharField(max_length=1000, null=True, blank=True)
    overall_report= models.CharField(max_length=1000, null=True, blank=True)
   

class TelegramAnalysis(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(null=True,max_length=100)
    school=models.CharField(null=True,max_length=100)
    field = models.CharField(max_length=255, null=True, blank=True)
    subjects = models.CharField(max_length=255, null=True, blank=True)
    Technology = models.CharField(max_length=255, null=True, blank=True)
    projects = models.CharField(max_length=255, null=True, blank=True)
    hobby =models.CharField(max_length=255, null=True, blank=True)
    goal = models.CharField(max_length=255, null=True, blank=True)
    questionnaire_summary = models.CharField(max_length=255, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    recommendations=models.CharField(max_length=1000, null=True, blank=True)
    general_report=models.CharField(max_length=1000, null=True, blank=True)
    personality_report= models.CharField(max_length=1000, null=True, blank=True)
    overall_report= models.CharField(max_length=1000, null=True, blank=True)

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
