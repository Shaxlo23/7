from django.urls import path
from . import views

urlpatterns = [
    path('library/',views.LibraryListAPIView.as_view(),name="library-list"),
    path('library/create/',views.LibraryCreateAPIView.as_view(),name="library-create"),
    path('library/<int:pk>/',views.LibraryRetrieveAPIView.as_view(),name="library-detail"),
    path('library/update/<int:pk>/',views.LibraryUpdateAPIView.as_view(),name="library-update"),
    path('library/delete/<int:pk>/',views.LibraryDestroyAPIView.as_view(),name="library-update"),
    path('library/detail-update/<int:pk>/',views.LibraryRetrieveUpdateAPIView.as_view(),name="library-update"),
    path('library/detail-delete/<int:pk>',views.LibraryRetrieveDestroyAPIView.as_view(),name="library-detail-delete"),
    path('library/<int:pk>/manage/',views.LibraryRetrieveUpdateDestroyAPIView.as_view(),name="library-manage"),
]


