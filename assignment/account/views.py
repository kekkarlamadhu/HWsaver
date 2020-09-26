from django.shortcuts import render,redirect,get_object_or_404

from django.urls import reverse_lazy,reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import UserRegisterForm,UserForm,ProfileForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
)

def home(request):

    return redirect('login')


def about(request):
    return render(request, 'account/about.html', {'title': 'About'})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('register')
        else:
            messages.error(request,form.error_messages)

    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})

class ProfileView(LoginRequiredMixin,TemplateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'account/profile.html'
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'account/profile-update.html'
    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.error(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))
        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

