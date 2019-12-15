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
