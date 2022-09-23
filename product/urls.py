from django.urls import path, include

from product.views import (
    ProductDetailView,
    ProductLikeView,
    ProductHotAPIView,
    Recommend,
)

app_name = "product"

urlpatterns = [
    path("<int:id>/", ProductDetailView.as_view()),
    path("<int:id>/review/", include('review.urls')),
    path("<int:id>/like/", ProductLikeView.as_view()),
    path("hot/", ProductHotAPIView.as_view()),
    path('', Recommend.as_view()),
]