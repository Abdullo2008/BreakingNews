from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import NewsModel, Category, Contact
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.shortcuts import render


class index(ListView):
    model = NewsModel
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()[1:]
        context["categories_all"] = Category.objects.all()
        context['contacts'] = Contact.objects.all()[:5]
        context['news_lists'] = NewsModel.published.all().order_by('-publish_time')[:15]
        context['popular_news'] = NewsModel.published.all().order_by('-publish_time')[:4]
        context['photos'] = NewsModel.published.all().order_by('-publish_time')[:6]
        context['mahalliy_xabarlar'] = NewsModel.published.all().filter(category__name="Mahalliy") \
                                           .order_by('-publish_time')[:15]
        context['uzbs'] = NewsModel.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[:15]
        context['jaxon'] = NewsModel.published.all().filter(category__name="Jaxon").order_by('-publish_time')[:15]
        context['bizness'] = NewsModel.published.all().filter(category__name="Biznes") \
                                 .order_by('-publish_time')[:15]
        context['sports'] = NewsModel.published.all().filter(category__name="Sport") \
                                .order_by('-publish_time')[:15]
        return context


def single(request, id):
    yangiliklar = NewsModel.objects.filter(id=id)
    context = {
        'yangiliklar': yangiliklar
    }
    return render(request, 'pages/single.html')


def categories_all(request, id):
    categorys = NewsModel.published.all().filter(category_id=id).order_by('-publish_time')
    context = {
        'categorys': categorys
    }
    return render(request, 'pages/category_page.html', context)


@login_required(login_url='login')
def Contact_Page_View(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return HttpResponseBadRequest("Invalid data submitted.")
    else:
        form = ContactForm()
        return render(request, 'pages/contact.html', {'form': form})


class NewsUpdateView(UpdateView):
    model = NewsModel
    fields = ('title', 'body', 'image', 'category', 'status')
    template_name = 'crud/edit.html'
    success_url = reverse_lazy('index')


class NewsDeleteView(DeleteView):
    model = NewsModel
    template_name = 'crud/delete.html'
    success_url = reverse_lazy('index')


class NewsCreateView(CreateView):
    model = NewsModel
    template_name = 'crud/create.html'
    fields = ('title', 'slug', 'body', 'image', 'category', 'status')
    success_url = reverse_lazy('index')


def SearchView(request):
    if request.method == 'POST':
        search = request.POST['search']
        news_search = NewsModel.objects.filter(title__contains=search)
        news_all = NewsModel.objects.all()
        return render(request, 'pages/search.html', {'search': search,
                                                     'news_search': news_search,
                                                     'news_all': news_all})
    else:
        return render(request, 'pages/search.html')
