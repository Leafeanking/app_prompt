from django.conf.urls import url, include
from rest_framework import routers
from prompts.views import PromptViewSet, UserList, UserDetail, getAuthTokenUser

router = routers.DefaultRouter()
router.register(r'prompts', PromptViewSet)

urlpatterns = [
    url(r'^prompts/random/$', PromptViewSet.as_view({'get': 'random', 'post': 'random'})),
    url(r'^', include(router.urls)),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^token-auth/', getAuthTokenUser.as_view())
]
