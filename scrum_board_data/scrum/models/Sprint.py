from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


class Sprint(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or _('Srint ending %s') % self.end


class SprintAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
