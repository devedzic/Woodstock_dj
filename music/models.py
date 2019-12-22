from django.db import models

# Create your models here.
from django.db.models import CharField, BooleanField, DateField, ForeignKey
from django.urls import reverse
from nbconvert import export

from woodstock_dj import settings

"""
Create some model(s) in the <app>/models.py file
    typical fields:
        models.CharField(max_length=<n>, default='<...>')
        models.BooleanField(verbose_name=<verbose name>, 
		    		        choices=<choices_list>, 
		    		        default=<choice from choices_list>,
		    		        ...)
        models.DateField(null=True, blank=True)
        models.TimeField(null=True, blank=True,
		    		     default=datetime.time(hour=<int>, minute=<int>, second=<int>))
        models.ForeignKey(<AnotherModel>,
		                  on_delete=models.SET_NULL,	# CASCADE, SET_DEFAULT,…
		                  null=True, 
		                  blank=True)
        ...
	typical methods:
	    __str__()
        get_absolute_url()		# return reverse('<model>-detail', args=[str(self.id)])
        ...
Register each model in <app>.admin.py with a separate line like:
    admin.site.register(<Model>)
Run:
    manage.py@<project_site>  > makemigrations <app>
Run:
    manage.py@<project_site>  > migrate
in order to create those model tables in your database
Run another cycle of change models - makemigrations - migrate whenever you make changes to your model(s) / database
Run (optionally):
    manage.py@<project_site>  > sqlmigrate <app> <migration number> 
    (e.g., manage.py@polls_site  > sqlmigrate polls 0001) 
to see the SQL equivalent of a specific migration
"""


class Festival(models.Model):
    """The model class describing the concept of a festival.
    It includes a name, location and the start and end dates.
    """

    name = CharField(max_length=100, default='unknown')
    start = DateField(null=True, blank=True)
    end = DateField(null=True, blank=True)
    location = CharField(max_length=100, default='location unknown')

    def __str__(self):
        return f'{self.name} ({self.start.isoformat()} - {self.end.isoformat()}), {self.location}'

    def get_absolute_url(self):
        """Returns the URL to access a particular festival instance.
        Enables specific Festival pages in admin to include "View on site" button.
        """

        return reverse('festival-detail', args=[str(self.id)])


class Performer(models.Model):
    """The model class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether they are a solo performer or a band.
    """

    musician_or_band = [
        (False, 'musician'),
        (True, 'band')
    ]
    name = CharField(max_length=100)
    is_band = BooleanField(verbose_name='Musician/Band',
                           choices=musician_or_band,
                           default=False)
    festival = ForeignKey(Festival, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.name} (band)' if self.is_band else f'{self.name} (musician)'

    def get_absolute_url(self):
        """Returns the URL to access a particular performer instance.
        Enables specific Performer pages in admin to include "View on site" button.
        """

        return reverse('performer-detail', args=[str(self.id)])


