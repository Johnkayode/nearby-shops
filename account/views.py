from django.shortcuts import render, redirect


from .forms import UserRegistrationForm


def signUp(request):
    if request.user.is_authenticated:
        return redirect(home)  

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'first_name':user_form.cleaned_data['first_name']}
            return redirect(home)   
        else:
            print('Errors: ', user_form.errors)
            context = {'user_form':user_form} 
            return render(request, 'account/register.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {'user_form':user_form}
        return render(request, 'account/register.html', context)
  

def signin(request):
    return render(request, 'account/login.html')