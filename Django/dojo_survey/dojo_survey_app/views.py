from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    name_from_form = request.POST['full_name']
    location_from_form = request.POST['location']
    language_from_form = request.POST['language']
    comment_from_form = request.POST['comment']
    context = {
        'name_from_form' : name_from_form,
        'location_from_form' : location_from_form,
        'language_from_form' : language_from_form,
        'comment_from_form' : comment_from_form,
    }
    return render(request, 'results.html', context)