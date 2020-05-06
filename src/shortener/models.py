from django.db import models
from .utils import code_generator, create_shortcode

# Create your models here.

# define models.objects.[methods]
class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        query_set = super(KirrURLManager, self).all(*args, **kwargs)
        actived_set = query_set.filter(active=True)

        return actived_set

    def refresh_shortcodes(self, items=None):
        query_set = super(KirrURLManager, self).filter(id__gte=1)

        if items is not None and isinstance(items, int):
            query_set = query_set.order_by('-id')[:items]
        recreate_count = 0

        for query in query_set:
            query.shortcode = create_shortcode(query)
            print(query.id)
            query.save()
            recreate_count += 1

        return "New codes made: {i}".format(i=recreate_count)


class KirrURL(models.Model):
    url = models.CharField(max_length=220)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
    update_time = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = KirrURLManager()

    # override save method
    def save(self, *args, **kwargs):
        if(self.shortcode is None or self.shortcode == ''):
            self.shortcode = create_shortcode(self)

        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
