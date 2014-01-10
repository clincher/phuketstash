# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from forms import RegistrationForm, UserUpdateForm


class UserCreateView(CreateView):
    model = get_user_model()
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('register-success')


class UserUpdateView(UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            messages.success(request, 'Профиль успешно обновлен.')
            return self.form_valid(form)
        else:
            messages.error(request, 'Ошибка при сохранении профиля.')
            return self.form_invalid(form)
