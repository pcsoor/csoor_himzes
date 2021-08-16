from django.contrib import admin
from .models import Kategoria, Szin, Meret, Termek, Color, Carousel
from mptt.admin import DraggableMPTTAdmin
from django_summernote.admin import SummernoteModelAdmin


class KategoriaAdmin(DraggableMPTTAdmin, SummernoteModelAdmin):
    mptt_indent_field = "nev"
    list_display = ('tree_actions', 'indented_title', 'ar', 'related_Termeks_count', 'related_Termeks_cumulative_count')
    list_display_links = ('indented_title',)
    list_editable = ('ar',)
    summernote_fields = ('leiras',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative Termek count
        qs = Kategoria.objects.add_related_count(
                qs,
                Termek,
                'kategoria_id',
                'Termeks_cumulative_count',
                cumulative=True)

        # Add non cumulative Termek count
        qs = Kategoria.objects.add_related_count(qs,
                 Termek,
                 'kategoria_id',
                 'Termeks_count',
                 cumulative=False)
        return qs

    def related_Termeks_count(self, instance):
        return instance.Termeks_count
    related_Termeks_count.short_description = 'Related Termeks (for this specific Kategoria)'

    def related_Termeks_cumulative_count(self, instance):
        return instance.Termeks_cumulative_count
    related_Termeks_cumulative_count.short_description = 'Related Termeks (in tree)'


class TermekekAdmin(SummernoteModelAdmin):
    list_display = ('nev', 'sorrend', 'get_kategoria', 'get_meretek', 'ar', 'osszetetel', 'kulso', 'anyag')
    list_editable = ('sorrend', 'ar')
    filter_horizontal = ['szin_id','meret_id']
    summernote_fields = ('leiras',)

    def get_kategoria(self, obj):
        return obj.kategoria_id.nev

    def get_meretek(self, obj):
        list = ", ".join([str(p) for p in obj.meret_id.all()])
        return list

    #def get_szinek(self, obj):
    #   list = ", ".join([str(sz) for sz in obj.szin_id.all()])
    #    return list

    get_kategoria.short_description = 'Kategória'
    get_meretek.short_description = 'Méretek'


class SzinAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'szin')
    list_editable = ('szin',)


class MeretekAdmin(admin.ModelAdmin):
    list_display = ('nev', 'sorrend')
    list_editable = ('sorrend',)


class ColorAdmin(admin.ModelAdmin):
    list_display = ('nev', 'hex', 'azonosito', 'small_image', 'sotet')
    list_display_links = ('nev',)
    list_editable = ('hex', 'azonosito', 'small_image','sotet')


# Register your models here.
admin.site.register(Kategoria, KategoriaAdmin)
admin.site.register(Szin, SzinAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Meret, MeretekAdmin)
admin.site.register(Termek, TermekekAdmin)
admin.site.register(Carousel)


