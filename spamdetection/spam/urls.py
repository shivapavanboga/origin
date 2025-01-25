from django.urls import path
from .views import MarkSpam

urlpatterns = [
    path('mark-spam/', MarkSpam.as_view(), name='mark_spam'),
]
