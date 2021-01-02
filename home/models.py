from django.db import models

# Create your models here.
class openHours(models.Model):

    class Meta:
        verbose_name_plural = "Opening Hours"

    DAY_CHOICE = (
        (None, "Please Select A Day"),
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    )  

    OPENING_TIME_CHOICES = (
     (None, "Please Select An Opening Time"),
     ("12 A.M", "12 a.m"), ("12.30 A.M", "12.30 a.m"),
     ("1 A.M", "1 a.m"), ("1.30 A.M", "1.30 a.m"),
     ("2 A.M", "2 a.m"), ("2.30 A.M", "2.30 a.m"),
     ("3 A.M", "3 a.m"), ("3.30 A.M", "3.30 a.m"),
     ("4 A.M", "4 a.m"), ("4.30 A.M", "4.30 a.m"),
     ("5 A.M", "5 a.m"), ("5.30 A.M", "5.30 a.m"),
     ("6 A.M", "6 a.m"), ("6.30 A.M", "6.30 a.m"),
     ("7 A.M", "7 a.m"), ("7.30 A.M", "7.30 a.m"),
     ("8 A.M", "8 a.m"), ("8.30 A.M", "8.30 a.m"),
     ("9 A.M", "9 a.m"), ("9.30 A.M", "9.30 a.m"),
     ("10 A.M", "10 a.m"), ("10.30 A.M", "10.30 a.m"),
     ("11 A.M", "11 a.m"), ("11.30 A.M", "11.30 a.m"),
     ("12 P.M", "12 p.m"), ("12.30 P.M", "12.30 p.m"),
     ("1 P.M", "1 p.m"), ("1.30 P.M", "1.30 p.m"),
     ("2 P.M", "2 p.m"), ("2.30 P.M", "2.30 p.m"),
     ("3 P.M", "3 p.m"), ("3.30 P.M", "3.30 p.m"),
     ("4 P.M", "4 p.m"), ("4.30 P.M", "4.30 p.m"),
     ("5 P.M", "5 p.m"), ("5.30 P.M", "5.30 p.m"),
     ("6 P.M", "6 p.m"), ("6.30 P.M", "6.30 p.m"),
     ("7 P.M", "7 p.m"), ("7.30 P.M", "7.30 p.m"),
     ("8 P.M", "8 p.m"), ("8.30 P.M", "8.30 p.m"),
     ("9 P.M", "9 p.m"), ("9.30 P.M", "9.30 p.m"),
     ("10 P.M", "10 p.m"), ("10.30 P.M", "10.30 p.m"),
     ("11 P.M", "11 p.m"), ("11.30 P.M", "11.30 p.m"),
    )

    CLOSING_TIME_CHOICES = (
    (None, "Please Select A Closing Time"),
    ("12 A.M", "12 a.m"), ("12.30 A.M", "12.30 a.m"),
    ("1 A.M", "1 a.m"), ("1.30 A.M", "1.30 a.m"),
    ("2 A.M", "2 a.m"), ("2.30 A.M", "2.30 a.m"),
    ("3 A.M", "3 a.m"), ("3.30 A.M", "3.30 a.m"),
    ("4 A.M", "4 a.m"), ("4.30 A.M", "4.30 a.m"),
    ("5 A.M", "5 a.m"), ("5.30 A.M", "5.30 a.m"),
    ("6 A.M", "6 a.m"), ("6.30 A.M", "6.30 a.m"),
    ("7 A.M", "7 a.m"), ("7.30 A.M", "7.30 a.m"),
    ("8 A.M", "8 a.m"), ("8.30 A.M", "8.30 a.m"),
    ("9 A.M", "9 a.m"), ("9.30 A.M", "9.30 a.m"),
    ("10 A.M", "10 a.m"), ("10.30 A.M", "10.30 a.m"),
    ("11 A.M", "11 a.m"), ("11.30 A.M", "11.30 a.m"),
    ("12 P.M", "12 p.m"), ("12.30 P.M", "12.30 p.m"),
    ("1 P.M", "1 p.m"), ("1.30 P.M", "1.30 p.m"),
    ("2 P.M", "2 p.m"), ("2.30 P.M", "2.30 p.m"),
    ("3 P.M", "3 p.m"), ("3.30 P.M", "3.30 p.m"),
    ("4 P.M", "4 p.m"), ("4.30 P.M", "4.30 p.m"),
    ("5 P.M", "5 p.m"), ("5.30 P.M", "5.30 p.m"),
    ("6 P.M", "6 p.m"), ("6.30 P.M", "6.30 p.m"),
    ("7 P.M", "7 p.m"), ("7.30 P.M", "7.30 p.m"),
    ("8 P.M", "8 p.m"), ("8.30 P.M", "8.30 p.m"),
    ("9 P.M", "9 p.m"), ("9.30 P.M", "9.30 p.m"),
    ("10 P.M", "10 p.m"), ("10.30 P.M", "10.30 p.m"),
    ("11 P.M", "11 p.m"), ("11.30 P.M", "11.30 p.m"),
)

    day = models.CharField(max_length=15, choices=DAY_CHOICE)
    openingTime = models.CharField(max_length=15, choices=OPENING_TIME_CHOICES, blank=True)
    closingTime = models.CharField(max_length=15, choices=CLOSING_TIME_CHOICES, blank=True)
    markedClosed = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.day


class aboutUs(models.Model):

    class Meta:
        verbose_name_plural = "About Us Text" 

    content = models.TextField(default="About Us", max_length="2000")
    
    def __str__(self):
        return self.content



