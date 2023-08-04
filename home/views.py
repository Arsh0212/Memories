from django.http import HttpResponse
from django.shortcuts import render
from .models import info, Image, Video


# Create your views here.


def home(request):
    return render(request, "home.html")


def Login(request):
    if request.method == "POST":
        name = request.POST.get("username")
        age = request.POST.get("age")
        email = request.POST.get("email")
        password = request.POST.get("password")
        info.objects.create(name=name, age=age, email=email, password=password)
        return render(request, "Login.html")
    else:
        return render(request, "Login.html")


def upload(request):
    return render(request, "upload.html")


def Signup(request):
    return render(request, "Signup.html")


def user(request):
    if request.method == "POST":
        submitted_id = request.POST.get("email")
        password = request.POST.get("password")
        try:
            info_instance = info.objects.get(email=submitted_id)
            request.session["ID"] = info_instance.email
            # ID exists in the database
            if int(info_instance.password) == int(password):
                return render(request, "user.html", {"info_instance": info_instance})
            else:
                return render(request, "home.html", {"message": "Password is Wrong"})
        except info.DoesNotExist:
            # ID does not exist in the database
            return render(request, "home.html", {"message": "Email is Wrong"})
    else:
        return render(request, "home.html")


def upload_image(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        id = request.POST.get("id-image")
        print(image)
        Image.objects.create(id=id, img=image)
        return render(request, "upload.html")
    else:
        return render(request, "Login.html")


def upload_video(request):
    if request.method == "POST":
        video = request.FILES.get("video")
        id = request.POST.get("id-video")
        Video.objects.create(id=id, vid=video)
        return render(request, "upload.html")
    else:
        return render(request, "Login.html")


def display_image(request):
    id = request.session["ID"]
    info_instance = info.objects.get(email=id)
    array = info_instance.img_id.split(" ")
    context = []
    for i in range(len(array)):
        try:
            img_instance = Image.objects.get(id=array[i])
            context.append(img_instance.img)
        except Image.DoesNotExist:
            # ID does not exist in the database
            print(str(array[i]) + "does not exist")
    print(context)
    return render(request, "display.html", {"context": context})


def display_video(request):
    id = request.session["ID"]
    info_instance = info.objects.get(email=id)
    array = info_instance.vid_id.split(" ")
    context = []
    for i in range(len(array)):
        try:
            vid_instance = Video.objects.get(id=array[i])
            context.append(vid_instance.vid)
        except Video.DoesNotExist:
            # ID does not exist in the database
            print(str(array[i]) + "does not exist")
    print(context)
    return render(request, "display_video.html", {"context": context})


def add_img_id(request):
    id = request.session["ID"]
    info_instance = info.objects.get(email=id)
    ID = str(request.GET.get("img_id"))
    value = info_instance.img_id
    value = value + " " + ID
    info_instance.img_id = value
    info_instance.save()
    return render(request, "display.html")


def add_vid_id(request):
    id = request.session["ID"]
    info_instance = info.objects.get(email=id)
    value = info_instance.vid_id
    ID = str(request.GET.get("vid_id"))
    value = value + " " + ID
    info_instance.vid_id = value
    info_instance.save()
    return render(request, "display_video.html")
