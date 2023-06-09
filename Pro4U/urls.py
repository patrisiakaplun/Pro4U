"""Pro4U URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from landing import views as landing_views
from review import views as review_views
from review.models import Review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_views.homepage, name='homepage'),
    path('learn-more/', landing_views.learn_more, name='learn_more'),
    path('', include('reservation.urls')),
    path('', include('account.urls.login_urls')),
    path('', include('SearchHistory.urls')),
    path('', include('account.urls.profile_urls')),
    path('professional/<int:pk>/reviews/', review_views.ReviewListView.as_view(model=Review, paginate_by=10),
         name='reviews'),
    path('professional/<int:pk>/reviews/new/', review_views.ReviewCreateView.as_view(), name='review-create'),
    path('professional/<int:pk>/reviews/update/', review_views.ReviewUpdateView.as_view(), name='review-update'),
    path('', include('chatmessage.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
