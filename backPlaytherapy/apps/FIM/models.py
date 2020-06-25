from django.db import models
from apps.patients.models import *

class FunctionalIndependenceMeasure(models.Model):

    date = models.DateField()
    goal = models.BooleanField(default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    
    #selfcare
    eat =  models.IntegerField()
    personal_clean =  models.IntegerField()
    bath =  models.IntegerField()
    dress_undress_sup =  models.IntegerField()
    dress_undress_inf =  models.IntegerField()
    bathUse =  models.IntegerField()
    
    #potty training
    control_dregs =  models.IntegerField()
    control_urine =  models.IntegerField()
    
    #move
    tras_bed_chair = models.IntegerField()
    tras_bath = models.IntegerField()
    tras_shower = models.IntegerField()
    
    #move 
    run_crawl_chair = models.IntegerField()
    steps = models.IntegerField()
    
    #comunication
    compresion = models.IntegerField()
    expresion = models.IntegerField()
    
    #social cognition
    social_inter = models.IntegerField()
    problem_solve = models.IntegerField()
    memory =  models.IntegerField()
    
    def total(self):
        total = self.eat + self.personal_clean + self.bath + self.dress_undress_sup + self.dress_undress_inf + self.bathUse + self.control_dregs + self.control_urine
        total += self.tras_bed_chair + self.tras_bath + self.tras_shower + self.run_crawl_chair + self.steps + self.compresion
        total += self.expresion + self. social_inter + self.problem_solve + self.memory
        
        return total
        
    def __unicode__(self):
        return self.patient.id_num + ' ' + str(self.date)
    