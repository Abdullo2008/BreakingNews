from .models import NewsModel, Category


def latest_news(request):
    latest_news = NewsModel.published.all().order_by('-publish_time')[:10]
    context = {
        'latest_news': latest_news
    }
    return context


def categories_news(request):
    categories_news = Category.objects.all()
    context = {
        'categories_news': categories_news
    }
    return context
