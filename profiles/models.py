"""Code source walkthrough boutique ado"""
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Books, Posters

from django_countries.fields import CountryField
from django.utils import timezone


class UserProfile(models.Model):
    """
    User profile for delivery information and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_order = models.BooleanField(default="True")
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(
        max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(
        max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(
        max_length=40, null=True, blank=True)
    default_postcode = models.CharField(
        max_length=20, null=True, blank=True)
    default_county = models.CharField(
        max_length=80, null=True, blank=True)
    default_country = CountryField(
        blank_label="Country", null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
        # Existing users: just save the profile
    instance.userprofile.save()


class Contact(models.Model):
    class Meta:
        verbose_name_plural = "Contact"

    email = models.EmailField(verbose_name="Your Email Address")
    reason = models.CharField(max_length=64, verbose_name="Message Subject")
    body = models.TextField(max_length=1064, verbose_name="Message")
    admin_responded = models.BooleanField(default="False")

    def __str__(self):
        return self.email


class SiteReview(models.Model):
    class Meta:
        verbose_name_plural = "Site Rewiew"

    RATING = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))

    name = models.CharField(max_length=50, verbose_name="Your Name")
    title = models.CharField(max_length=64, verbose_name="Review Title")
    rating = models.IntegerField(choices=RATING, verbose_name="Rate Us")
    body = models.TextField(max_length=1064, verbose_name="Your Review")
    admin_approved = models.BooleanField(default="False")

    def __str__(self):
        return self.title


class SubscribeEmail(models.Model):

    email = models.EmailField(
        help_text="We will respond to this address.",
        verbose_name="Your Email Address",
        unique=True,
    )
    created = models.DateTimeField("Date Created", default=timezone.now)

    def __str__(self):
        return self.email
