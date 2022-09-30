from django.urls import include, path

from product.views import (MagazineAPIView, MagazineUserAPIView,
                           ProductDetailView, ProductHotAPIView,
                           ProductLikeView)

app_name = "product"

urlpatterns = [
    path("<int:id>/", ProductDetailView.as_view()),
    path("<int:id>/like/", ProductLikeView.as_view()),
    path("hot/", ProductHotAPIView.as_view()),
    path("magazine/", MagazineAPIView.as_view()),
    path("user-magazine/", MagazineUserAPIView.as_view()),
    path("<int:id>/review/", include("review.urls")),
]
