from django.http import HttpResponse


# Function Base View

# Class Home
def home(request):
    print(dir(request))
    return HttpResponse("<h1>Hello World</h1>")