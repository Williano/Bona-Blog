# Django imports.
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View

# Blog app imports
from blog.forms.account.login_forms import UserLoginForm


class UserLoginView(View):
    """
     Logs author into dashboard.
    """
    template_name = 'account/login.html'
    context_object = {"login_form": UserLoginForm}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context_object)

    def post(self, request, *args, **kwargs):

        login_form = UserLoginForm(request=request, data=request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f"Welcome {user.username}")
                    return redirect('blog:dashboard_home')
                else:
                    messages.error(request, "Your account has been disabled")
                    return render(request, self.template_name)
            else:
                messages.error(request,
                               f"Invalid Login details: {username}, {password}")
                return render(request, self.template_name)

        else:
            messages.error(request, "Invalid username and password")
            return render(request, self.template_name, self.context_object)



