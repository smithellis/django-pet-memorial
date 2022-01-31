from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Hospital(models.Model):

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'Washington D.C.'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    ]
    name = models.CharField(max_length=200)
    address_one = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default='GA'
    )
    phone = models.CharField(max_length=200)

    billing_name = models.CharField(max_length=200, default='None')
    billing_address_one = models.CharField(max_length=200, default='None')
    billing_address_two = models.CharField(max_length=200, blank=True, null=True)
    billing_address_zipcode = models.CharField(max_length=200, default='None')
    billing_address_state = models.CharField(max_length=2, default="GA")
    billing_phone_number = models.CharField(max_length=200, default="None")
    billing_contact_email = models.EmailField(max_length=200, default="smithe@gmail.com")

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

class Profile(models.Model):
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, default=1)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    primary_hospital_contact = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
        
class Memorial(models.Model):
    CAT = "cat"
    DOG = "dog"
    BIRD = "bird"
    HORSE = "horse"
    LIZARD = "lizard"
    TURTLE = "turtle"
    OTHER = "other"

    PET_TYPE_CHOICES = [(CAT,'Cat'),
                        (DOG,'Dog'),
                        (BIRD,'Bird'),
                        (HORSE,'Horse'),
                        (LIZARD,'Lizard'),
                        (TURTLE,'Turtle'),
                        (OTHER,'Other')]

    STATE_CHOICES = [
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DC', 'Washington D.C.'),
        ('DE', 'Delaware'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    ]

    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    donation = models.ForeignKey('Donation', on_delete=models.CASCADE, null=True)
    owner_name = models.CharField(max_length=200)
    owner_address_one = models.CharField(max_length=200)
    owner_address_two = models.CharField(max_length=200, null=True)
    owner_city = models.CharField(max_length=200)
    owner_state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default='GA'
    )
    owner_zipcode =models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    pet_species = models.CharField(
        max_length=10,
        choices=PET_TYPE_CHOICES,
        default=CAT
    )
    
    status = models.CharField(max_length=200, default='New')
    create_date = models.DateField(auto_now=True)
    cvm_status = models.CharField(max_length=200, default="New")
    bad_address = models.BooleanField(default=False)

    def __str__(self):
        return self.pet_name

    def get_update_url(self):
        return reverse('memorial-update', kwargs={'pk': self.pk})
    
    def get_detail_url(self):
        return reverse('memorial-detail', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('memorial-delete', kwargs={'pk': self.pk})

    def get_create_url(self):
        return reverse('memorial-create')

class Fund(models.Model):
    fund_name = models.CharField(max_length=200)
    url_code = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.fund_name

class Donation(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, default=1)
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, default=1)
    fund = models.ForeignKey('Fund', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=200, null=True)
    code = models.CharField(max_length=200, null=True)
    submitted_for_payment_date = models.DateField(null=True)
    payment_status = models.CharField(max_length=200, default='Not Paid')
    payment_code = models.CharField(max_length=200, null=True)
    count_mems_submitted = models.IntegerField(default=0)

    def __str__(self):
        return self.code