from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.http import JsonResponse
from .models import *
from django.http import JsonResponse
import time
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import requests
import base64
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.urls import reverse
from django.contrib import messages
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import shutil
import os 
MEDIA_ROOT=settings.MEDIA_ROOT

def add_text_overlay(image_path, customer, date, custom_text, output_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)

    # Define font and size
    font_size = 20
    font = ImageFont.truetype("arial.ttf", font_size)
    ascent, descent = font.getmetrics()
    text_width = font.getmask(custom_text).getbbox()[2]
    text_height = font.getmask(custom_text).getbbox()[3] + descent

    # Set box size based on text size
    box_width = img.width
    box_height = 80

    # get

    # Draw grey box
    draw.rectangle([(0, 0), (box_width, box_height)], fill=(128, 128, 128, 128))

    # Draw text on the image
    draw.text((15, 10), f"{customer} - {date}", fill=(0, 0, 0, 255), font=font)
    draw.text(
        ((img.width - text_width) // 2, 45), custom_text, fill=(0, 0, 0, 255), font=font
    )

    # Save the image with overlay
    img.save(output_path)

    # # # Convert image to bytes
    # img_byte_array = BytesIO()
    # img.save(img_byte_array, format="JPEG")

    # # Reset file pointer to the beginning
    # img_byte_array.seek(0)

    # return img_byte_array


class viewReport(View):
    def get(self, request, pk):
        data_obj = FormData.objects.get(id=pk)
        images = data_obj.uploaded_images.all()
        print(images)
        return render(
            request, "home/report.html", context={"obj": data_obj, "images": images}
        )


class viewUsersJobs(View):
    def get(self, request):
        # Query all users
        users = User.objects.all()

        # Pass the users to the template
        return render(
            request,
            "home/viewUsersJobs.html",
            context={"users": users},
        )


def signup(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]

        # Create a new user with additional information
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        return redirect("login")
    else:
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "home/signup.html")

    return render(request, "home/signup.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")  # Replace 'dashboard' with your desired URL
    else:
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, "home/login.html")

    return render(request, "home/login.html")


def user_logout(request):
    logout(request)
    return redirect("login")


def profile(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user_profile = User.objects.get(username=request.user)

            jobs = FormData.objects.filter(user=request.user)

            context = {
                "first_name": user_profile.first_name,
                "last_name": user_profile.last_name,
                "jobs": jobs,
            }

            return render(request, "home/profile.html", context)
        else:
            return redirect("login")


class home(View):
    def post(self, request):
        date = request.POST.get("date")
        ID = request.POST.get("ID")
        customer = request.POST.get("customer")
        job = request.POST.get("job")
        contractor = request.POST.get("contractor")
        timeIn = request.POST.get("timeIn")
        timeOut = request.POST.get("timeOut")
        totalTime = request.POST.get("totalTime")
        jobDescription = request.POST.get("jobDescription")
        whatWasCompleted = request.POST.get("whatWasCompleted")
        stillNeedsCompleted = request.POST.get("stillNeedsCompleted")
        notes = request.POST.get("notes")
        uploaded_images = request.FILES.getlist("data_files")
        captions = request.POST.getlist("caption")
        print(len(uploaded_images))

        # creating object and saving data
        form_data = FormData.objects.create(
            date=date,
            WO_ID=ID,
            customer=customer,
            job=job,
            contractor=contractor,
            inTime=timeIn,
            outTime=timeOut,
            totalTime=totalTime,
            job_description=jobDescription,
            waht_was_completed=whatWasCompleted,
            still_needs_completed=stillNeedsCompleted,
            issues=notes,
            signature=f"Signatures/signature_{customer}.png",
            user=request.user,
        )

        # Add uploaded images to FormData
        for image in uploaded_images:
            print(image)
            form_data.add_uploaded_image(image)
            
        # # Add uploaded images to FormData
        # for caption,image in zip(captions,uploaded_images):
        #     print(image.name)
        #     image_name=image.name
        #     # Example usage:
        #     img_bytes = add_text_overlay(
        #         image.file, customer, date, caption, image_name
        #     )
        #     shutil.copyfile(image_name, f"{MEDIA_ROOT}/Images/{image_name}")
        #     form_data.add_uploaded_image(f"Images/{image_name}")
        #     os.remove(f"{image_name}")

        #     # form_data.add_uploaded_image("output_image.jpg")

            # sending email
        view_report_url = f"http://70.35.199.230/view_report/{form_data.id}"
        context_data = {
            "date": date,
            "ID": ID,
            "customer": customer,
            "job": job,
            "contractor": contractor,
            "timeIn": timeIn,
            "timeOut": timeOut,
            "totalTime": totalTime,
            "jobDescription": jobDescription,
            "whatWasCompleted": whatWasCompleted,
            "stillNeedsCompleted": stillNeedsCompleted,
            "notes": notes,
            "view_report_url": view_report_url,
        }
        email_html_message = render_to_string("home/email_template.html", context_data)

        # Send the email
        subject = f"{date} - {customer}"
        from_email = "ap1solutions0201@gmail.com"  #
        to_email = "deliverables@ap1solutions.com"  #
        # to_email = "zh2935461@gmail.com"

        text_content = strip_tags(email_html_message)

        # Send the email as both HTML and plain text
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(email_html_message, "text/html")
        msg.send()

        # return render(
        #     request,
        #     "home/index.html",
        #     {"message": "Your Data is submitted successfully!"},
        # )
        message = "Your Data is submitted successfully!"
        # Add success message to Django's messages framework
        messages.success(request, message)
        return redirect(reverse("home"))

    def get(self, request):
        print(MEDIA_ROOT)
        # if request.user.is_authenticated:
        return render(request, "home/index.html")

    # else:
    #     return redirect("login")


class tests(View):
    def get(self, request):
        return render(request, "home/tests.html")
