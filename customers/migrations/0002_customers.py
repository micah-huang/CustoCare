# Generated by Django 3.0.6 on 2020-05-28 15:31

from django.db import migrations


# grabbing Customer class of our customers app and creating 
#   a demo customer to insert into the database

def create_data(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000", address="Customer 000 Address", description= "Customer 001 description").save()


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
            migrations.RunPython(create_data),
            ]