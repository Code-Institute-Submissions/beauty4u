# Generated by Django 3.0.7 on 2020-12-04 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201204_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openhours',
            name='closingTime',
            field=models.CharField(choices=[('12 A.M', '12 a.m'), ('12.30 A.M', '12.30 a.m'), ('1 A.M', '1 a.m'), ('1.30 A.M', '1.30 a.m'), ('2 A.M', '2 a.m'), ('2.30 A.M', '2.30 a.m'), ('3 A.M', '3 a.m'), ('3.30 A.M', '3.30 a.m'), ('4 A.M', '4 a.m'), ('4.30 A.M', '4.30 a.m'), ('5 A.M', '5 a.m'), ('5.30 A.M', '5.30 a.m'), ('6 A.M', '6 a.m'), ('6.30 A.M', '6.30 a.m'), ('7 A.M', '7 a.m'), ('7.30 A.M', '7.30 a.m'), ('8 A.M', '8 a.m'), ('8.30 A.M', '8.30 a.m'), ('9 A.M', '9 a.m'), ('9.30 A.M', '9.30 a.m'), ('10 A.M', '10 a.m'), ('10.30 A.M', '10.30 a.m'), ('11 A.M', '11 a.m'), ('11.30 A.M', '11.30 a.m'), ('12 P.M', '12 p.m'), ('12.30 P.M', '12.30 p.m'), ('1 P.M', '1 p.m'), ('1.30 P.M', '1.30 p.m'), ('2 P.M', '2 p.m'), ('2.30 P.M', '2.30 p.m'), ('3 P.M', '3 p.m'), ('3.30 P.M', '3.30 p.m'), ('4 P.M', '4 p.m'), ('4.30 P.M', '4.30 p.m'), ('5 P.M', '5 p.m'), ('5.30 P.M', '5.30 p.m'), ('6 P.M', '6 p.m'), ('6.30 P.M', '6.30 p.m'), ('7 P.M', '7 p.m'), ('7.30 P.M', '7.30 p.m'), ('8 P.M', '8 p.m'), ('8.30 P.M', '8.30 p.m'), ('9 P.M', '9 p.m'), ('9.30 P.M', '9.30 p.m'), ('10 P.M', '10 p.m'), ('10.30 P.M', '10.30 p.m'), ('11 P.M', '11 p.m'), ('11.30 P.M', '11.30 p.m')], default='6 P.M', max_length=15),
        ),
        migrations.AlterField(
            model_name='openhours',
            name='openingTime',
            field=models.CharField(choices=[('12 A.M', '12 a.m'), ('12.30 A.M', '12.30 a.m'), ('1 A.M', '1 a.m'), ('1.30 A.M', '1.30 a.m'), ('2 A.M', '2 a.m'), ('2.30 A.M', '2.30 a.m'), ('3 A.M', '3 a.m'), ('3.30 A.M', '3.30 a.m'), ('4 A.M', '4 a.m'), ('4.30 A.M', '4.30 a.m'), ('5 A.M', '5 a.m'), ('5.30 A.M', '5.30 a.m'), ('6 A.M', '6 a.m'), ('6.30 A.M', '6.30 a.m'), ('7 A.M', '7 a.m'), ('7.30 A.M', '7.30 a.m'), ('8 A.M', '8 a.m'), ('8.30 A.M', '8.30 a.m'), ('9 A.M', '9 a.m'), ('9.30 A.M', '9.30 a.m'), ('10 A.M', '10 a.m'), ('10.30 A.M', '10.30 a.m'), ('11 A.M', '11 a.m'), ('11.30 A.M', '11.30 a.m'), ('12 P.M', '12 p.m'), ('12.30 P.M', '12.30 p.m'), ('1 P.M', '1 p.m'), ('1.30 P.M', '1.30 p.m'), ('2 P.M', '2 p.m'), ('2.30 P.M', '2.30 p.m'), ('3 P.M', '3 p.m'), ('3.30 P.M', '3.30 p.m'), ('4 P.M', '4 p.m'), ('4.30 P.M', '4.30 p.m'), ('5 P.M', '5 p.m'), ('5.30 P.M', '5.30 p.m'), ('6 P.M', '6 p.m'), ('6.30 P.M', '6.30 p.m'), ('7 P.M', '7 p.m'), ('7.30 P.M', '7.30 p.m'), ('8 P.M', '8 p.m'), ('8.30 P.M', '8.30 p.m'), ('9 P.M', '9 p.m'), ('9.30 P.M', '9.30 p.m'), ('10 P.M', '10 p.m'), ('10.30 P.M', '10.30 p.m'), ('11 P.M', '11 p.m'), ('11.30 P.M', '11.30 p.m')], default='9 A.M', max_length=15),
        ),
    ]
