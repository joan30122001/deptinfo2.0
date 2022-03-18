from django.shortcuts import render
from .models import TB_Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import Http404
from .forms import CommentForm


# Create your views here.

def article(request):
    search_article = request.GET.get('searched')
    context = {}
    if search_article:
        list_articles = TB_Article.objects.filter(Q(title__icontains = search_article)).order_by('-created_at')
    else:
        list_articles = TB_Article.objects.all().order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_articles, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {"liste_articles": articles, "searched": search_article}
    return render(request, "blog/blog.html", context)



def detail_article(request, slug_text):
    try:
        article = TB_Article.objects.get(slug = slug_text)
    except Article.DoesNotExist:
        raise Http404('Cet article n\' existe pas!!')
    # category = article.category
    # articles_en_relation = Article.objects.filter(category = category)[:3]
    autres = TB_Article.objects.all().order_by('-created_at')[:4]



    comments = article.comments.filter(active=True).order_by("-date_added")

    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()



    return render(request, "blog/detail_article.html", {"article": article, "aer": autres, "comments": comments, "new_comment": new_comment, "comment_form": comment_form})
    # return render(request, "information/detail_article.html", {"article": article, "aer": autres})