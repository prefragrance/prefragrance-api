from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from search.views import SearchAPIView

app_name = 'search'

urlpatterns = [
    path('', SearchAPIView.as_view()),
    # path('<int:product_id>',SearchRetrieveAPIView.as_view()),
]
