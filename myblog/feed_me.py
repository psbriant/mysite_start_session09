from django.contrib.syndication.views import Feed
from django.urls import reverse
from mymodel.models import Post

class LatestEntriesFeed(Feed):
    title = "Blog Posts"
    link = "/feedme/"
    description = "Feeds the blog all the newses."

    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
