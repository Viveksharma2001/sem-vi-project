from distutils.command import upload
from email.policy import default
from sre_parse import CATEGORIES
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    def __str__(self):
        return self(self.name)


CATEGORY_CHOICES=(
    ('MS','Mens shoes'),
    ('WS','Womens shoes'),
    ('BS','Boys shoes'),
    ('GS','Girls shoes'),
)


class product(models.Model):
    product_id=models.AutoField
    title=models.CharField(max_length=100,default="")
    product_name=models.CharField(max_length=50)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    discount_price=models.FloatField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name




class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=122)
    lname=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.fname



    
