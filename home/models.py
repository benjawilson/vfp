from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

# import MultiFieldPanel:
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):

    # Models for Hero section
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

    # Models for Card
    card_title = models.CharField(
        blank=True,
        max_length=255,
    ) 
    card_subtitle = models.CharField(
        blank=True,
        max_length=255,
    )
    card_button_text = models.CharField(
        blank=True,
        max_length=255,
    )
    card_button_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        verbose_name="Button Link",
        help_text="Choose a page to link to from the card",
    )

    # Models for Carousel
    first_slide_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="First photo in Carousel",
    )
    second_slide_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Second photo in Carousel",
    )
    third_slide_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Third photo in Carousel",
    )
    first_slide_description = models.CharField(
        blank=True,
        max_length=255,
    )
    second_slide_description = models.CharField(
        blank=True,
        max_length=255,
    )
    third_slide_description = models.CharField(
        blank=True,
        max_length=255,
    )
    first_slide_label = models.CharField(
        blank=True,
        max_length=255,
    )
    second_slide_label = models.CharField(
        blank=True,
        max_length=255,
    )
    third_slide_label = models.CharField(
        blank=True,
        max_length=255,
    )

    # Content Panels for Home Page
    content_panels = Page.content_panels + [
        # Hero Section
        MultiFieldPanel(
            [
                FieldPanel("hero_text"),
                FieldPanel("hero_cta"),
            ],
            heading="Hero section",
        ),
        # Mission Section
        MultiFieldPanel(
            [
                FieldPanel("mission_heading"),
                FieldPanel("mission_statement"),
            ],
            heading="Mission section"
        ),
        # Card Section
        MultiFieldPanel(
            [
                FieldPanel("card_title"),
                FieldPanel("card_subtitle"),
                FieldPanel("card_button_text"),
                FieldPanel("card_button_link"),
            ],
            heading = "Action Card"
        ),
        # Carousel Section
        MultiFieldPanel(
            [
                FieldPanel("first_slide_image"),
                FieldPanel("first_slide_label"),
                FieldPanel("first_slide_description"),
                FieldPanel("second_slide_image"),
                FieldPanel("second_slide_label"),
                FieldPanel("second_slide_description"),
                FieldPanel("third_slide_image"),
                FieldPanel("third_slide_label"),
                FieldPanel("third_slide_description"),
            ],
            heading = "Photo Carousel"
        )
    ]