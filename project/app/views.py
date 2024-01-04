from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import PullRequestModel

from .forms import PullRequestForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def list_view(request):
    pull_requests = PullRequestModel.objects.all()
    context = {
        'pull_requests': pull_requests
    }
    return render(context=context, request=request, template_name='app/list.html')

def register(request):
    if request.method == 'POST':
        form = PullRequestForm(request.POST)
        if form.is_valid():
            model = PullRequestModel()
            model.set_Form(form)
            model.save()
        else:
            print(form.errors)
        return HttpResponseRedirect('list')
    else:
        # getとして扱う
        form = PullRequestForm()
        return render(request, 'app/register.html', {'form': form})

