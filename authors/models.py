from django.db import models


COUNTRY_CHOICES = (('EUA', 'USA'), 
                   ('BRA', 'Brazil'), 
                   ('FRANCE', 'France'), 
                   ('ISR', 'Israel'), 
                   ('CHI', 'China'), 
                   ('SKR','South Korea'), 
                   ('ITA','Italy'), 
                   ('CAN','Canada'), 
                   ('AUS','Australia'), 
                   ('UK','UK'),
                   ('POL', 'Poland'),
                   ('JPN', 'Japan'),
                   ('SAF', 'South Africa'),)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    bio = models.CharField(max_length=500, blank=True, null=True)


    def __str__(self):
        return self.name