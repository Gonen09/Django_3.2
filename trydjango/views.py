"""
To render html web pages
"""
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """

    article_obj = Article.objects.get(id=2)
    article_queryset = Article.objects.all()

    # Metodo 1

    # article_title = article_obj.title
    # article_content = article_obj.content
    # article_id = article_obj.id

    # HTML_DATA = f"""
    #    <h3>{article_title}</h3>
    #    <p>{article_content}</p>
    #    <p>{article_id}</p>
    # """

    # Metodo 2
    # context = {
#
    #    "id": article_obj.id,
    #    "title": article_obj.title,
    #    "content": article_obj.content
    # }
#
    # HTML_DATA = """
    #    <h3>{title}</h3>
    #    <p>{content}</p>
    #    <p>{id}</p>
    # """.format(**context)

    # Metodo 3

    context = {
        "object_list": article_queryset,
        "objet": article_obj,
        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }

    # HTML_RESPONSE = HTML_STRING + HTML_DATA

    HTML_RESPONSE = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_RESPONSE)
