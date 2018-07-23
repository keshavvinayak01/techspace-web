from django.conf.urls import url
from .views import contentForCommunity

app_name = 'community'

urlpatterns = [
    # url(r'^$', BlogListView.as_view(), name='community_blog_view'),
    # url(r'^$', EventListView.as_view(), name='community_event_view'),
    url(r'^$', contentForCommunity, name='community_content_view'),


]