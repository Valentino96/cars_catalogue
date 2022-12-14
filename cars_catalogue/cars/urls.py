from django.urls import path, include

from cars_catalogue.cars.views import index, create_profile, details_profile, edit_profile, delete_profile, catalogue, \
    create_car, details_car, delete_car, edit_car

urlpatterns = (
    path('', index, name='index'),
    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
    path('catalogue/', catalogue, name='catalogue'),
    path('car/', include([
        path('create/', create_car, name='create car'),
        path('<int:pk>/details/', details_car, name='details car'),
        path('<int:pk>/edit/', edit_car, name='edit car'),
        path('<int:pk>/delete/', delete_car, name='delete car'),
    ])
))