from django.http import HttpResponse

# Create your views here.
def introduction(request):
    return HttpResponse ('This is Gallery')