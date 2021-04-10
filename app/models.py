from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hood')
    image = models.ImageField(upload_to='neighborhoods/')
    description = models.TextField()
    medical_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)
    population = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f'{self.name}'

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    @classmethod
    def update_population(cls, neighborhood_id):
        occupation = cls.objects.get(id=neighborhood_id)
        new_count = occupation.occupation_count +1
        cls.objects.filter(id=neighborhood_id).update(occupation_count=new_count)

    def update_neighborhood(self):
        name = self.name
        self.name = name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    status = models.TextField()
    Neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='residents', blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    def delete_profile(self):
        self.delete()


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    email = models.EmailField(max_length=100)
    Neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')

    class Meta:
        verbose_name = 'Business'
        verbose_name_plural = 'Businesses'

    def __str__(self):
        return f'{self.name}'

    def save_business(self):
        self.save()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    def update_business(self):
        name = self.name
        self.name = name


class Post(models.Model):
    categories = (
        ('1', 'Crimes and Safety'),
        ('2', 'Health'),
        ('3', 'Recommendations'),
        ('4', 'Fire Breakouts'),
        ('5', 'Lost and Found'),
        ('6', 'Deaths'),
        ('7', 'Events'),   
    )

    category = models.CharField(max_length=120, choices=categories)
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='neighborhood_post')

    def __str__(self):
        return f'{self.title}'

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
