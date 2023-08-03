from django.shortcuts import render
from .models import Article

# Create your views here.


def article_search_view(request):

    query_dict = request.GET  # dictionay

    try:
        query = query_dict.get("q")  # < input type='text' name='q' />
    except:
        query = None

    article_obj = None

    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {"object": article_obj}

    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):

    article_obj = Article.objects.get(id=id) if id is not None else None

    context = {
        "object": article_obj,
    }

    return render(request, "articles/detail.html", context=context)
