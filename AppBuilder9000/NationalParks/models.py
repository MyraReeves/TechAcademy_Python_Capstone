from django.db import models


class VisitorComment(models.Model):
    Park_name = models.CharField(max_length=30, default="", blank=False, null=True)
    State = models.CharField(max_length=2, default="", blank=False, null=True)
    Weather = models.CharField(max_length=50, default="", blank=True, null=False)
    Summarize_your_trip_in_one_short_sentence = models.CharField(max_length=100, default="", blank=False)
    Leave_a_longer_description_here = models.TextField(max_length=800, default="", blank=True)
    Favorite_moment = models.CharField(max_length=100, default="", blank=True, null=False)
    Memorable_creatures_or_sights_seen = models.TextField(max_length=500, default="", blank=True)
    Helpful_tips_for_other_visitors = models.CharField(max_length=100, default="", blank=True, null=False)
    Your_name = models.CharField(max_length=50, default="", blank=True, null=False)

    object = models.Manager()

    def __str__(self):
        return self.Summarize_your_trip_in_one_short_sentence
