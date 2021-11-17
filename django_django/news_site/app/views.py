from django.shortcuts import render, redirect

from .forms import Contactform, CotegoryForm
from .models import *


# Create your views here.

def home(requests, slug=None):
    news = News.objects.all()
    ctg = Category.objects.all()
    one = news[6]
    one2 = news[3:]
    one3 = news[::-1]
    one4 = news[::-6]
    one1 = news[6]

    ctx = {
        "news": news,
        "ctg": ctg,
        "one": one,
        "one1": one1,
        "one2": one2,
        "one3": one3,
        "one4": one4
    }
    return render(requests, 'index.html', ctx)


def category(requests, slug=None):
    ctg_one = Category.objects.get(slug=slug)
    news1 = News.objects.all().filter(ctg_id=ctg_one.id)
    ctg = Category.objects.all()
    loop = news1[0]
    ctx = {
        "news": news1,
        "ctg": ctg,
        "ctg_one": ctg_one,
        "loop": loop
    }
    return render(requests, 'category.html', ctx)


def search(requests, slug=None):
    ctg = Category.objects.all()
    news = News.objects.all()

    if requests.GET:
        savol = requests.GET.get('v')
    else:
        savol = False
    all_news = []
    for i in news:
        if savol and savol in i.title:
            all_news.append(i)
    print("savol :", savol)
    print(all_news)
    news1 = news[::-1]

    ctx = {
        "a1": news,
        "a2": news1,
        "news": all_news,
        "len": len(all_news),
        "savol": savol,
        "ctg": ctg
    }
    return render(requests, "search.html", ctx)


def contact(requests, slug=None):
    ctg = Category.objects.all()
    ctx = {
        "ctg": ctg
    }
    return render(requests, "contact.html", ctx)


def form(requests):
    forms = Contactform()
    ctg = CotegoryForm()
    print("forms: ", forms)

    if requests.POST:
        forms = CotegoryForm(requests.POST)
        if forms.is_valid():
            forms.save()
            return redirect("home")

    ctx = {
        "form": forms,
        "ctg": ctg
    }

    return render(requests, "form.html", ctx)


def register(requests, pk=None):
    form = Contactform()
    if requests.POST:
        forms = Contactform(requests.POST or None,
                            requests.FILES or None)
        if forms.is_valid():
            forms.save()
            save = True
        else:
            save = False
    else:
        save = False

    ctx = {
        "form": form,
        "save": save
    }
    return render(requests, 'register.html', ctx)


