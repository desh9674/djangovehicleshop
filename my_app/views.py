from email import message
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import CarsCreate
from .models import Car
#from django.contrib.messages import get_messages
# Create your views here.
def home(request):
    #print(request.user.is_staff())
    return HttpResponse("Hello this is view inside my_app")


def index(request):
    shelf = Car.objects.all()
    #print(request.user.is_staff)
    return render(request, 'car/garage.html', {'shelf': shelf})


def upload(request):
    if request.user.is_staff:
        upload = CarsCreate()
        if request.method == 'POST':
            upload = CarsCreate(request.POST, request.FILES)
            print(upload)
            if upload.is_valid():
                upload.save()
                return redirect('index')
            else:
                return HttpResponse("""your form is wrong, reload on <a href = "{{ url : '/myapp/cars'}}">reload</a>""")
        else:
            return render(request, 'car/upload_form.html', {'upload_form':upload})
    else:
        message
        return redirect('index', )


def update_car(request, car_id):
    if request.user.groups.filter(name='mods').exists():
        print(request.user.groups.filter(name='mods').exists())
        car_id = int(car_id)
        try:
            car_sel = Car.objects.get(id = car_id)
        except Car.DoesNotExist:
            return redirect('index')
        car_form = CarsCreate(request.POST or None, instance = car_sel)
        if car_form.is_valid():
            #print(car_form.is_valid)
            car_form.save()
            return redirect('index')
        return render(request, 'car/upload_form.html', {'upload_form':car_form})
    else:
        return redirect("index")

def delete_car(request, car_id):
    print(request.user.is_staff)
    if request.user.is_staff:
        car_id = int(car_id)
        print(request.user)
        try:
            car_sel = Car.objects.get(id = car_id)
        except Car.DoesNotExist:
            return redirect('index')
        car_sel.delete()
        return redirect('index')
    else:
        return redirect('index')













def getCars(request):
    carJson = {
    "vNumber": "2981F",
    "vType": "3",
    "vModel": "Italian",
    "vDescription": "Was used for f1 races"
}
    context = {}
    form = CarsCreate(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    
    context['form'] = form
    return render(request, "home.html", context)

#