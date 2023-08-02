"""
To render html web pages
"""
from django.http import HttpResponse
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """

    article_obj = Article.objects.get(id=2)

    # article_title = article_obj.title
    # article_content = article_obj.content
    # article_id = article_obj.id

    context = {

        "id": article_obj.id,
        "title": article_obj.title,
        "content": article_obj.content
    }

    name = "Gonen"

    HTML_STRING = f"""

        <h1>Hello {name} !!!</h1>

    """

    # HTML_DATA = f"""
    #    <h3>{article_title}</h3>
    #    <p>{article_content}</p>
    #    <p>{article_id}</p>
    # """

    HTML_DATA = """
        <h3>{title}</h3>
        <p>{content}</p>
        <p>{id}</p>
    """.format(**context)

    HTML_RESPONSE = HTML_STRING + HTML_DATA

    return HttpResponse(HTML_RESPONSE)
