from django.contrib import admin
from django.db import models
from .models import *
from django.utils.html import format_html

MODELS = [FormData]


@admin.register(FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = [
        field.name
        for field in FormData._meta.get_fields()
        if field.name != "uploaded_images"
    ] + ["display_uploaded_images"]

    def display_uploaded_images(self, obj):
        image_urls = [
            "http://127.0.0.1:8000" + image.image.url
            for image in obj.uploaded_images.all()
        ]
        clickable_images = [
            format_html('<a href="{}" target="_blank">{}</a>', url, url)
            for url in image_urls
        ]
        return format_html(", ".join(clickable_images))

    display_uploaded_images.short_description = "Uploaded Images"


@admin.register(ImagesData)
class ImagesDataAdmin(admin.ModelAdmin):
    list_display = ["id", "image"]
