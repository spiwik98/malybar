from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from . import forms
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

@method_decorator(login_required, 'dispatch')
class PizzaUpdate(UpdateView):
    """Widok aktualizuacji"""

    model = models.Pizza
    form_class = forms.PizzaForm
    success_url = reverse_lazy('pizza:lista')  # '/pizza/lista'

    def get_context_data(self, **kwargs):
        context = super(PizzaUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['skladniki'] = forms.SkladnikiFormSet(
                self.request.POST,
                instance=self.object)
        else:
            context['skladniki'] = forms.SkladnikiFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        skladniki = forms.SkladnikiFormSet(
            self.request.POST,
            instance=self.object)
        if form.is_valid() and skladniki.is_valid():
            return self.form_valid(form, skladniki)
        else:
            return self.form_invalid(form, skladniki)

    def form_valid(self, form, skladniki):
        form.instance.autor = self.request.user
        self.object = form.save()
        skladniki.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, skladniki):
        return self.render_to_response(
            self.get_context_data(form=form, skladniki=skladniki)
        )