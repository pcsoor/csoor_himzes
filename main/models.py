from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.text import slugify
from django.db.models import F


# Create your models here.
class Kategoria(MPTTModel):
    id = models.AutoField(primary_key=True)
    nev = models.CharField(max_length=200)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.jpg")
    leiras = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    borito = models.ImageField(null=True, blank=True, upload_to="images", default="images/placeholder.jpg")
    ar = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nev

    def get_all_products(self):
        Termek.objects.filter(kategoria_id__in=self.get_descendants(include_self=True))

    class MPPTMeta:
        order_insertion_by = ['nev']



    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.nev)

            has_slug = Kategoria.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.nev) + '-' + str(count)
                has_slug = Kategoria.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    nev = models.CharField(max_length=255)
    hex = models.CharField(max_length=7)
    azonosito = models.CharField(max_length=2, null=True, blank=True)
    sotet = models.BooleanField(default=False)
    small_image = models.ImageField(null=True, blank=True, upload_to="images/", default="")

    def __str__(self):
        return self.nev

    class Meta:
        ordering = ['nev']


class Carousel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False, default="Slider name")
    image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/placeholder.jpg")
    order = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']




class Szin(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/placeholder.jpg")
    szin = models.ForeignKey(Color, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return self.image.name



class Meret(models.Model):
    id = models.AutoField(primary_key=True)
    nev = models.CharField(max_length=100, unique=True)
    sorrend = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nev

    class Meta:
        ordering = ['sorrend']


class Termek(models.Model):
    id = models.AutoField(primary_key=True)
    nev = models.CharField(max_length=255)
    image_id = models.ForeignKey(Szin, null=True, on_delete=models.SET_NULL, related_name="termekimage", blank=True)
    kategoria_id = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)
    leiras = models.TextField(null=True, blank=True)
    anyag = models.CharField(max_length=255, blank=True, null=True)
    osszetetel = models.CharField(max_length=255, blank=True, null=True)
    meret_id = models.ManyToManyField(Meret, blank=True, related_name="meret")
    tomeg = models.CharField(max_length=255, blank=True, null=True)
    kulso = models.CharField(max_length=255, blank=True, null=True)
    szin_id = models.ManyToManyField(Szin, blank=True, related_name="termekszin")
    ar = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=True)
    sorrend = models.IntegerField(default="valami")

    def __str__(self):
        return self.nev

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.nev)

            has_slug = Termek.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.nev) + '-' + str(count)
                has_slug = Termek.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)



    class Meta:
        unique_together = ('sorrend', 'nev')



class Kepek(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/", default="placeholder.png")





