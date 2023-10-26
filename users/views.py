from django.shortcuts import render
from  .forms import UserRegisrationForm
from django.urls import reverse
from django.http import HttpResponseRedirect


def register(request):
    if request.method == "POST":
        form = UserRegisrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegisrationForm()

    context = {'form': form}





    return  render(request, template_name='register.html', context=context)





