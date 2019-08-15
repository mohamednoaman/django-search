from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import BooleanField


class Medicine(models.Model):
   # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    title             = models.CharField(max_length=120)
    price             = models.FloatField()
    summary           = models.TextField(default='this is cool')
    featured          = models.BooleanField(default=True)
    created_date      = models.DateTimeField(default=timezone.now)
    published_date    = models.DateTimeField(blank=True, null=True)
    AUTH_USER_MODEL   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
      verbose_name_plural = "Medicine"

      def __str__(self):
        return self.name

'''

    models.CharField – this is how you define text with a limited number of characters.
    models.TextField – this is for long text without a limit. Sounds ideal for blog post content, right?
    models.DateTimeField – this is a date and time.
    models.ForeignKey – this is a link to another model.

        #active_ingredient = models.TextField(blank=True, null=True)
    #other_ingredients = models.TextField(blank=True, null=True)

'''