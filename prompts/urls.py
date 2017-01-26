from django.conf.urls import url, include
from rest_framework import routers
from prompts.views import PromptViewSet

router = routers.DefaultRouter()
router.register(r'^prompts', PromptViewSet)

urlpatterns = [
    url(r'^prompts/random/$', PromptViewSet.as_view({'get': 'random', 'post': 'random'})),
    url(r'^', include(router.urls)),
]
