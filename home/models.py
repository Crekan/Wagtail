from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    subtitle = models.CharField(max_length=250, blank=True, null=True, verbose_name='Подзаголовок')
    rtfbody = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtfbody'),
    ]

    # promote_panels = []
    # settings_panels = []
