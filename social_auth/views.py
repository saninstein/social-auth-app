from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import SignUpForm


class GeneralView(LoginRequiredMixin, TemplateView):
    template_name = "general.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    model = get_user_model()
    template_name = "registration/signup.html"
    success_url = reverse_lazy("general")

    def form_valid(self, form):
        res = super().form_valid(form)
        login(self.request, self.object, 'social_auth_app.auth_backends.CustomBackend')
        return res
