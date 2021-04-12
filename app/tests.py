from django.test import TestCase
from django.db import models
from .models import Neighbourhood, Profile, Business, Post
from django.contrib.auth.models import User

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User(username="Dorothy", password="password123")
        self.user.save()
        self.neighbourhood= Neighbourhood(name = "Victoria Courts", location= "Ngong Road", population= 1, admin = self.user,description='Testing',medical_contact='0700000000',police_contact='0700000000', fire_dept='0700000000')
        self.neighbourhood.save()

        self.profile = Profile(user = self.user,status='Here',email='neighborhood@test.com', hood = self.neighbourhood)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)
    
    # Testing Get Profile Method
    def test_get_profile(self):
        self.profile.save_profile()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)
    
    # Testing Delete Method
    def test_delete_method(self):
        self.profile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.profile.delete_profile()
        testdelete = Profile.objects.filter(name=self.user)
        self.assertEqual(len(testdelete), 0)
