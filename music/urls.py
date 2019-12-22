"""URLconfig of the music app.
Different URL patterns for an app are typically specified in the following ways:
    - for function-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view function>, name='<the corresponding view name>'>
        ]
    - for class-based views:
        urlpatterns = [
            path('<URL segment>/', views.<the corresponding view class>.as_view(), name='<the corresponding view name>'>
        ]
"""

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]

urlpatterns += [
    path('performers/', views.PerformerListView.as_view(), name='performer-list')
]

urlpatterns += [
    path('performers/<int:pk>/', views.PerformerDetailView.as_view(), name='performer-detail')
]

urlpatterns += [
    path('festivals/', views.FestivalListView.as_view(), name='festival-list')
]

urlpatterns += [
    path('festivals/<int:pk>/', views.FestivalDetailView.as_view(), name='festival-detail')
]

urlpatterns += [
    path('performers/create/', views.PerformerCreateView.as_view(), name='performer-create'), 
    path('performers/<int:pk>/update/', views.PerformerUpdateView.as_view(), name='performer-update'), 
    path('performers/<int:pk>/delete/', views.PerformerDeleteView.as_view(), name='performer-delete'),
]

urlpatterns += [
    path('festivals/create/', views.FestivalCreateView.as_view(), name='festival-create'),
    path('festivals/<int:pk>/update/', views.FestivalUpdateView.as_view(), name='festival-update'),
    path('festivals/<int:pk>/delete/', views.FestivalDeleteView.as_view(), name='festival-delete'),
]


