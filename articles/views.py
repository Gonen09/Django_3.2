from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ArticleForm
from .models import Article

# Create your views here.


def article_search_view(request):

    query_dict = request.GET  # dictionay

    try:
        query = int(query_dict.get("q"))  # < input type='text' name='q' />
    except:
        query = None

    article_obj = None

    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {"object": article_obj}

    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):

    # forma con Django ModelForm

    form = ArticleForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # return redirect("article-detail, slug=article_objetcs.slug")
        return redirect(article_object.get_absolute_url())

    return render(request, "articles/create.html", context=context)

    # forma con Django forms
    """
    form = ArticleForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():

        article_object = form.save()  # reemplaza las lineas a continuacion
        print(request.POST)
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        print(title, content)
        article_object = Article.objects.create(title=title, content=content)

        context['object'] = article_object
        context['created'] = True
    """

    """  forma con form

    # print (request. POST)
    form = ArticleForm()
    # print(dir(form))  # Contenido de articleForm (atributos y metodos)
    context = {"form": form}

    if request.method == "POST":

        print("Post data: ", request.POST)
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    """


def article_detail_view(request, slug=None):

    article_obj = None

    if slug is not None:

        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)
