from django.urls import path

# from .views import home_page_view
from .views import homePageView

urlpatterns = [
    # path("", home_page_view),
    path("", homePageView),
]