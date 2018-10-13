import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','CRUDProject.settings')
import django
django.setup()

from CrudApp.models import *
from faker import Faker
from random import *
fake = Faker('hi_IN')
def insert(n):
    for i in range(n):
        feid=randint(1001,9999)
        fename=fake.name()
        femail=fake.email()
        fcity=fake.city()
        fphone=fake.phone_number()
        emp=Employee.objects.get_or_create(eid=feid,ename=fename,emailid=femail,city=fcity,phone=fphone)
        #emp=Employee.objects.get_or_create(eid=feid,ename=fename,emailid=femail,city=fcity,phone=fphone)

insert(1)
