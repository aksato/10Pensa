from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import UserCreationFormWithEmail
from pagina_inicial.models import Produto

class SignUpView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class PerfilView(LoginRequiredMixin, generic.ListView):
    model = Produto
    template_name = 'accounts/perfil.html'

    def get_queryset(self):
        return Produto.objects.filter(usuario=self.request.user)