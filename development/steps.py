"""Steps in developing a Django application
"""

# Setup

"""
Open a Django project in PyCharm:
    specify one app in Application name
    check Enable Django admin (in earlier versions of PyCharm)
Add another app (optionally) using:
    manage.py@<project_site>  > startapp <app_label>
Run:
    manage.py@<project_site>  > runserver
    (Tools / Run manage.py Task...)
        click http://127.0.0.1:8000/ 
        open http://127.0.0.1:8000/admin 
Verify / Add the following line in INSTALLED_APPS in settings.py:
    '<app>.apps.<App>Config' (e.g., 'music.apps.MusicConfig')
Specify the database in DATABASES in settings.py (default: sqlite3)
Include (optionally) the call to the static() function in <project_site>/urls.py, 
    in order to enable the serving of static files (CSS, JavaScript, images) during development:
        in <project_site>/urls.py extend the urlpatterns list like this:
            from django.conf import settings
            from django.conf.urls.static import static
            ...
            urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
Create (optionally) the static, static/css, static/images and other directories in the <app> directory 
    to store static files that the <app> might need
Run:
    manage.py@<project_site>  > makemigrations
    (although it is probably not absolutely necessary at this stage)
Run:
    manage.py@<project_site>  > migrate
    (in order to create some initial database tables)
Create admin superuser:
    manage.py@<project_site>  > createsuperuser
    open http://127.0.0.1:8000/admin
Create the <project_site>/templates/<app> folder for the first <app>
"""

# Development 1

"""
Write the simplest index view (returning just HttpResponse("Hello, world"))
Create the corresponding <app>/urls.py file:
    import views.py:
        from . import views
    create the urlpatterns list:
        urlpatterns = [
	        path('', views.index, name='index')
        ]
Include <app>/urls.py in the urlpatterns list of the <project_site>/urls.py:
        urlpatterns = [
	        path('<app>/', include('<app>.urls'))
        ]
Verify that the index view works:
    run:
        manage.py@<project_site>  > runserver 
    again if it was closed after running it for the first time
    open http://localhost:8000/<app>/ (e.g., http://localhost:8000/music/) 
        (you should see "Hello, World!" printed in the browser)
Redirect (optionally) the root URL of your site (i.e. 127.0.0.1:8000) to 127.0.0.1:8000/<app>/, 
    i.e. make '<app>/' the landing page:
        in <project_site>/urls.py extend the urlpatterns list like this:
            urlpatterns += [
	            path('', RedirectView.as_view(url='music/'))
            ]
Commit 1
"""


