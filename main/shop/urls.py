from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('main-product/', views.product, name='product'),
    path('other-product/', views.product1, name='product1'),
    path('main-product/andexb51/', views.andex, name='andex'),
    path('main-product/TileGum/', views.tile, name='tile'),
    path('main-product/B12/', views.b12, name='b12'),
    path('main-product/Whte-cement/', views.white, name='white'),
    path('main-product/Grout-cement/', views.grout, name='grout'),
     path('main-product/Tile-polish', views.polish, name='polish'),
]
