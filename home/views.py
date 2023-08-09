from django.shortcuts import redirect, render
from django.urls import reverse
from .models import info, Image, Video
from .forms import Login_form, Signup_form


# Create your views here.


def home(request):
    name = "Guest"
    return render(request, "Home Page.html", {"name": name})


def User_home(request, id, name):
    return render(request, "Home Page.html", {"name": name, "id": id})


def Login(request):
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                info_instance = info.objects.get(email=data["Email_Id"])
                # ID exists in the database
                if int(info_instance.password) == int(data["Password"]):
                    name = info_instance.name
                    id = data["Email_Id"]
            except:
                name = "Guest"
            return render(request, "Home Page.html", {"name": name, "id": id})
    else:
        return render(request, "Login.html", {"form": Login_form})


def upload(request):
    return render(request, "upload.html")


def Signup(request):
    if request.method == "POST":
        form = Signup_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            info.objects.create(
                name=data["Name"],
                age=data["Age"],
                email=data["Email_Id"],
                password=data["Password"],
            )
            return render(request, "Login.html", {"form": Login_form})
    else:
        return render(request, "Signup.html", {"form": Signup_form})


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


def display_image(request, id):
    info_instance = info.objects.get(email=id)
    name = info_instance.name
    array = info_instance.img_id.split(" ")
    context = []
    for i in range(1, len(array)):
        try:
            img_instance = Image.objects.get(id=array[i])
            context.append(img_instance.img)
        except:
            print("ID Does Not match")
    return render(request, "display.html", {"context": context, "id": id})


def display_video(request, id):
    info_instance = info.objects.get(email=id)
    array = info_instance.vid_id.split(" ")
    context = []
    for i in range(1, len(array)):
        try:
            vid_instance = Video.objects.get(id=array[i])
            context.append(vid_instance.vid)
        except:
            print("Id Does not match")
    return render(request, "display_video.html", {"context": context, "id": id})


def add_img_id(request, id):
    info_instance = info.objects.get(email=id)
    img_id = str(request.GET.get("img_id"))
    value = info_instance.img_id
    value = value + " " + img_id
    info_instance.img_id = value
    info_instance.save()
    return render(request, "display.html")


def add_vid_id(request, id):
    info_instance = info.objects.get(email=id)
    value = info_instance.vid_id
    ID = str(request.GET.get("vid_id"))
    value = value + " " + ID
    info_instance.vid_id = value
    info_instance.save()
    return render(request, "display_video.html")
