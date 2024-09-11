from django.db import models


TYPE_CHOICES = {
    ('NP', 'National Park'),
    ('NHS', 'National Historic Site'),
    ('NHR', 'National Historical Reserve'),
    ('NHP', 'National Historical Park'),
    ('NRA', 'National Recreation Area'),
    ('NVM', 'National Volcanic Monument'),
}


class WashingtonPark(models.Model):
    name = models.CharField(max_length=70, default="", blank=False, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    description = models.TextField(max_length=800, default="", blank=True)
    website = models.CharField(max_length=110, default="", blank=False, null=True)
    visitor_center_hours = models.CharField(max_length=400, default="", blank=True, null=False)
    mail_to = models.CharField(max_length=100, default="", blank=True, null=False)
    mailing_street_address = models.CharField(max_length=50, default="", blank=True, null=False)
    city = models.CharField(max_length=30, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    zipcode = models.CharField(max_length=5, default="", blank=True, null=False)
    phone = models.CharField(max_length=12, default="555-555-5555", blank=False, null=True)
    google_maps_link = models.CharField(max_length=200, default="https://maps.app.goo.gl/", blank=False, null=True)

    object = models.Manager()

    # In admin site, display each object by its name value:
    def __str__(self):
        return self.name


class OregonPark(models.Model):
    name = models.CharField(max_length=30, default="", blank=False, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    description = models.TextField(max_length=800, default="", blank=True)
    website = models.CharField(max_length=100, default="", blank=False, null=True)
    visitor_center_hours = models.CharField(max_length=100, default="", blank=True, null=False)
    mail_to = models.CharField(max_length=100, default="", blank=True, null=False)
    mailing_street_address = models.CharField(max_length=50, default="", blank=True, null=False)
    city = models.CharField(max_length=30, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    zipcode = models.CharField(max_length=5, default="", blank=True, null=False)
    phone = models.CharField(max_length=12, default="555-555-5555", blank=False, null=True)
    google_maps_link = models.CharField(max_length=200, default="https://maps.app.goo.gl/", blank=False, null=True)

    object = models.Manager()

    # In admin site, display each object by its name value:
    def __str__(self):
        return self.name
