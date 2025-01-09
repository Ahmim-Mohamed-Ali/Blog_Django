from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.


def register_view(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            messages.success(request,f"Your account is now created. You are now able to log in")
            return redirect("login")

    else:
        form =UserRegisterForm()
    return render(request,"users/register.html",context={
        "form":form
    })

@login_required
def view_profile(request,id_user):
    user = get_object_or_404(User, id=id_user)


    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f"Your Profile Is Now Updated")
            return redirect("view_profile",id_user=id_user)
        
    else:       
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'users/profile.html', {
        'user': user,
        'u_form':u_form,
        "p_form":p_form
        })
