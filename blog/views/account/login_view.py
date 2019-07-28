# Django imports.
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View


class UserLoginView(View):
    """
     Logs author into dashboard.
    """
    template_name = 'account/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        if username and password:
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
            messages.error(request, "Please Provide username and password")
            return render(request, self.template_name)



