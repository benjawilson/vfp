from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    # Models for Hero section
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        blank=True,
        max_length=255, help_text="Write an introduction for the site"
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name="Hero CTA",
        max_length=255,
        help_text="Text to display on Call to Action",
    )

    # Models for Mission section
    mission_heading = models.CharField(
        blank=True,
        max_length=255,
        help_text="Mission statement title"
    ) 
    mission_statement = models.TextField() 

    # Models for Carousel

    body = RichTextField(blank=True)

    # modify your content_panels:
    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
            ],
            heading="Hero section",
        ),
        MultiFieldPanel(
            [
                FieldPanel("mission_heading"),
                FieldPanel("mission_statement"),
            ],
            heading="Mission section"
        ),
        FieldPanel('body'),
    ]