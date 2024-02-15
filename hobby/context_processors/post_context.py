from hobby.models import Hobby


def last_posts(request):
    posts = Hobby.objects.order_by('date')
    return {
        'last_posts': posts
    }