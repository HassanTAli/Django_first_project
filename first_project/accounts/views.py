from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm



def create_user(req):
    form = UserCreationForm()
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:movie_index')
        
    return render(req,'registration/signup.html',context={'form': form})