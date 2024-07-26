from django.contrib import admin
from django.urls import path, include, re_path
from photo_comp_main.views import *
from photo_comp_app.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers



urlpatterns = [
    path('', home, name='home'),
    path('pod/', pod, name='pod'),
    path('disposable/', disposable, name='disposable'),
    path('vape_juice/', vape_juice, name='vape_juice'),
    path('consumables/', consumables, name='consumables'),

    path('hookah/', hookah, name='hookah'),
    path('tobacco_free_mixtures/', tobacco_free_mixtures, name='tobacco_free_mixtures'),
    path('tobacco/', tobacco, name='tobacco'),
    path('goal/', goal, name='goal'),
    path('accessory/', accessory, name='accessory'),

    path('test/', test, name='test'),

    path('accounts/profile/', profile),
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/photocomp/', PhotoCompAPIList.as_view()),
    path('api/v1/photocomp/<int:pk>/', PhotoCompAPIUpdate.as_view()),
    path('api/v1/photocompdelete/<int:pk>/', PhotoCompAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )