from django.urls import path

from . import views

urlpatterns = [
    #projects's urls
    path('projects/',views.ProjectsListCreateView.as_view(), name='projects'),
    path('projects/<int:id>/',views.ProjectsRetrieveUpdateDestroyView.as_view(), name='project-detail'),

    #services's urls
    path('services/',views.ServicesListCreateView.as_view(), name='services'),
    path('services/<int:id>/',views.ServicesRetrieveUpdateDestroyView.as_view(), name='services-detail'),

    #reviews's urls
    path('reviews/',views.ReviewsListCreateView.as_view(), name='reviews'),
    path('reiviews/<int:id>/',views.ReviewsRetrieveUpdateDestroyView.as_view(), name='review-detail'),
]