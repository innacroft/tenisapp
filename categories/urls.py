from django.urls import path
from .views import UserRankingView

urlpatterns = [
    path('ranking/', UserRankingView.as_view(), name='user-ranking'),
]