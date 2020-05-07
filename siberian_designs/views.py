from django.shortcuts import render
from django.views.generic import DetailView

from .models import Work, Example


# Create your views here.

def main(request):
    context = {
        'title': 'Рекламные контрукции по Сибири'
    }
    return render(request, 'siberian_designs/main-page.html', context)


def services(request):
    context = {
        'title': 'Услуги'
    }
    return render(request, 'siberian_designs/services.html', context)


def examples(request):
    works = Work.objects.filter(is_visible=True)
    context = {
        'title': 'Наши работы',
        'works': works,
    }
    return render(request, 'siberian_designs/examples.html', context)


class ExampleDetails(DetailView):
    model = Work
    template_name = 'siberian_designs/example-details.html'

    def get_context_data(self, **kwargs):
        context = super(ExampleDetails, self).get_context_data(**kwargs)
        context['title'] = Work.objects.get(title=self.object.title)
        context['examples'] = Example.objects.filter(work=self.object.id)  # (work=self.objects.id)
        # context['ids'] = Example.objects.all().get(id=self.object.id)
        return context



def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'siberian_designs/contacts.html', context)
