"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin'''
from django.contrib import admin
from django.urls import path # noqa: E402
from blog import views  # noqa: E402
'''from blog import admin'''  # noqa: E402
''' path('', include('myblog.urls'))'''
'''path('admin/', admin.site.urls)'''

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('search/', views.search, name='search'),
    path('', views.home, name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category_posts'), 
    path('tag/<slug:slug>/', views.tag_posts, name='tag_posts'),
    

]
