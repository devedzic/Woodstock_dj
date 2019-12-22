from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from music.models import Performer, Festival


# Create your views here.


# # The very first version of the index view, used only in the setup phase.
# # It just prints something in the browser.
# def index(request):
#     return HttpResponse("<h1>Woodstock</h1>")

def index(request):
    """The index view that defines a context to be rendered in index.html.
    This context includes, e.g., the numbers of Performer and Festival objects in the database.
    These numbers can be retrieved using <Model>.objects.all().count().
    The context is specified as a dictionary with the items in the format:
        '<string to be used in the index.html template>': <data item (e.g., the number of performers)>
    The view returns the result of the render() function,
    passing it the request, the template file name, and the context.
    """

    n_performers = Performer.objects.all().count()
    n_festivals = Festival.objects.all().count()
    context = {
        'n_p': n_performers,
        'n_f': n_festivals
    }
    return render(request, 'index.html', context=context)


class PerformerListView(ListView):
    """Class-based view that handles lists of Performer objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    In case more context is needed, which is completely optional and depends on the application
    (see https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-display/#adding-extra-context),
    it is also necessary to override ListView.get_context_data() and add more dictionary entries.
    """

    model = Performer
    template_name = 'music/performer-list.html'

    def get_queryset(self):
        return Performer.objects.all()


class PerformerDetailView(DetailView):
    """Class-based view that handles individual Performer objects.
    Typical fields that DetailView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    In case more context is needed, which is completely optional and depends on the application
    (see https://docs.djangoproject.com/en/dev/topics/class-based-views/generic-display/#adding-extra-context),
    it is also necessary to override ListView.get_context_data() and add more dictionary entries.
    """

    model = Performer
    template_name = 'music/performer-detail.html'

    # Get more context - enable showing info about all festivals in the database (along with performer details)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_festivals'] = Festival.objects.all()
        return context


class FestivalListView(ListView):
    """Class-based view that handles lists of Festival objects.
    Typical fields that ListView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_list.html')
    Typically, such views also override ListView.get_queryset(),
    making it return a QuerySet of objects (such as (possibly filtered) <Model>.objects.all()))
    """

    model = Festival
    template_name = 'music/festival-list.html'

    def get_queryset(self):
        return Festival.objects.all()


class FestivalDetailView(DetailView):
    """Class-based view that handles individual Festival objects.
    Typical fields that DetailView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_detail.html')
    """

    model = Festival
    template_name = 'music/festival-detail.html'


class PerformerCreateView(CreateView):
    """Class-based view that handles creation of individual Performer objects through a form.
    Typical fields that CreateView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - fields (a list of model fields to appear on the form,
          e.g. fields = ['<model_field_1>', '<model_field_1>',...];
          to include all fields from the model: model = '__all__')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_form.html')
    """

    model = Performer
    fields = '__all__'
    template_name = 'music/performer-form.html'


class PerformerUpdateView(UpdateView):
    """Class-based view that handles updating individual Performer objects through a form.
    Typical fields that UpdateView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - fields (a list of model fields to appear on the form,
          e.g. fields = ['<model_field_1>', '<model_field_1>',...];
          to include all fields from the model: model = '__all__')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_form.html')
    """

    model = Performer
    fields = '__all__'
    template_name = 'music/performer-form.html'


class PerformerDeleteView(DeleteView):
    """Class-based view that handles deleting individual Performer objects through a form.
    Typical fields that DeleteView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - success_url (the page to return to after deleting an object through a dialog form;
          typically provided by success_url = reverse_lazy('<view_name>'); '<view_name>' is, e.g., '<model>-list')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_confirm_delete.html')
    """

    model = Performer
    success_url = reverse_lazy('performer-list')
    template_name = 'music/performer-confirm-delete.html'


class FestivalCreateView(CreateView):
    """Class-based view that handles creation of individual Festival objects through a form.
    Typical fields that CreateView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - fields (a list of model fields to appear on the form,
          e.g. fields = ['<model_field_1>', '<model_field_1>',...];
          to include all fields from the model: model = '__all__')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_form.html')
    """

    model = Festival
    fields = '__all__'
    template_name = 'music/festival-form.html'


class FestivalUpdateView(UpdateView):
    """Class-based view that handles updating individual Festival objects through a form.
    Typical fields that UpdateView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - fields (a list of model fields to appear on the form,
          e.g. fields = ['<model_field_1>', '<model_field_1>',...];
          to include all fields from the model: model = '__all__')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_form.html')
    """

    model = Festival
    fields = '__all__'
    template_name = 'music/festival-form.html'


class FestivalDeleteView(DeleteView):
    """Class-based view that handles deleting individual Festival objects through a form.
    Typical fields that DeleteView-based classes specify include:
        - model (class name of the corresponding <Model> class
        - success_url (the page to return to after deleting an object through a dialog form;
          typically provided by success_url = reverse_lazy('<view_name>'); '<view_name>' is, e.g., '<model>-list')
        - template_name ('<app>/<template file name>'; default: '<app>/<model>_confirm_delete.html')
    """

    model = Festival
    success_url = reverse_lazy('festival-list')
    template_name = 'music/festival-confirm-delete.html'


