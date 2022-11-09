from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
import datetime

import random,string

from django.utils import timezone
#=====Consult model


#==generate a random trans_id=====



class Consultation(models.Model):
    name = models.CharField(max_length=12,default='callstruction')
    phone = models.CharField(max_length=10,null=False)
    category = models.CharField(max_length=20,default='building')
    created_on = models.DateTimeField(default=timezone.now)
    #phone field is supposed to be max 10 xters

    def __str__(self) -> str:
        return self.name - self.phone


class Booking(models.Model):
    name = models.CharField(max_length=12,default='callstruction')
    phone = models.CharField(max_length=10,null=False)
    description = models.CharField(max_length=10,default='construction')
    location = models.CharField(max_length=10,null=False,default='Nyanama')

    created_on = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.name - self.category

#===now a model to store the transactions made
#==phone should be that of person making the transaction

ACTION = (
    ('consult', ('Consult')),
    ('booking', ('Booking'))
)


class Transaction(models.Model):
    trans_id = models.CharField(max_length=8)
    phone = models.CharField(max_length=10,null=False)
    customer_name = models.CharField(max_length=20, default='customer')
    amount = models.BigIntegerField(default=0)
    action = models.CharField(max_length=20,choices=ACTION,default='consult')
    created_on = models.DateTimeField(default=timezone.now)
    total_collected = models.BigIntegerField(default=0)
    


    @property
    def real_trans_id(self):
        while not self.trans_id:
            real_trans_id = ''.join(
                random.choice(string.ascii_lowercase+string.digits) for i in range(8)
            )
            return real_trans_id

    #==get the final collection
    @property
    def final_collected(self):
        while self.amount:
            final_collected = self.total_collected + int(self.amount)
            return final_collected

    def __str__(self) -> str:
        return self.trans_id - self.customer_name


#== have a table to record the amount collected, in this in case a transaction was successful
#add it to the total collections and keep on adding it
#===how do we know that its this person who answered the calls

#===just use signals instead that trigger a pre_save action

@receiver(pre_save,sender=Transaction)
def update_transaction(sender, instance, **kwargs):
    #==if instance/row is being created, then do nothing
    if instance.id is None:pass 
    #==else if it is being modified
    else:
        current = instance
        #to update the collected amount we need the previous colelcted
        #===previous table===
        previous = Transaction.objects.get(id=instance.id)
        if previous is None:
            current.total_collected = current.amount 
            #if no previous table,total_collected_amount will equal the amount collected
        else:
            current.total_collected = previous.total_collected+current.amount
            #incase there is a prev transaction table total collected 

        








