from django.db import models

"""Name,Email,Phone,Password,Confirm Password, ADD CARD, Card Number, Expiration Year, Expiration Month, CVV, Cardholder Name, submit"""

class Costumer_Data(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)  # Use o tipo de campo apropriado para números de telefone
    password = models.CharField(max_length=128)

class CreditCardInfo(models.Model):
    card_number = models.CharField(max_length=16)  
    expiration_year = models.IntegerField()  
    expiration_month = models.IntegerField() 
    cvv = models.CharField(max_length=4)  
    card_holder_name = models.CharField(max_length=255) 
