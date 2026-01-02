from .models import Category, Tag

def blog_data(request):
    return {
        'categories': Category.objects.all(),
        'tags': Tag.objects.all(),
    }
