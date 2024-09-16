from django.db import models


PUBLISHER_CHOICES = {
    ('Archie Comics (formerly M.L.J.)', 'Archie Comics (formerly M.L.J.)'),
    ('Boom! Studios', 'Boom! Studios'),
    ('Dark Horse', 'Dark Horse'),
    ('DC (formerly National)', 'DC (formerly National)'),
    ('Dell', 'Dell'),
    ('EC/Entertaining Comics (formerly Educational Comics)', 'EC/Entertaining Comics (formerly Educational Comics)'),
    ('Fawcett', 'Fawcett'),
    ('IDW', 'IDW'),
    ('Image Comics', 'Image Comics'),
    ('Marvel (formerly Atlas)', 'Marvel (formerly Atlas)'),
    ('Valiant Comics', 'Valiant Comics'),
    (' ', '* Other')
}


class ComicbookCollection(models.Model):
    publisher = models.CharField(max_length=100, choices=PUBLISHER_CHOICES)
    Series_Title = models.CharField(max_length=200, default="", blank=False, null=True)
    Volume_number = models.CharField(max_length=4, default="", blank=True, null=False)
    Issue_number = models.IntegerField(default="", blank=False, null=True)
    Year = models.CharField(max_length=4, default="", blank=False, null=True)

    object = models.Manager()

    def __str__(self):
        display_entry = '{0.Series_Title} #{0.Issue_number}'
        return display_entry.format(self)
