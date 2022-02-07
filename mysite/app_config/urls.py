"""app_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views

from . import view


urlpatterns = [
    # 管理サイトのURL
    path('admin/', admin.site.urls),
    # login用のURL
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    # logout用のURL
    path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    # 何もURLを設定しない場合（app_config/view.pyで自動的に「app_folder」にアクセス設定）
    path('', view.index, name='index'),
    # 今回作成するアプリにアクセスするURL
    path('app_folder/', include('app_folder.urls')),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
