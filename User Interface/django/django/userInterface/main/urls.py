from django.urls import path
from  . import views


urlpatterns = [
    path("<int:id>",views.index,name ="index"),
    path("afficher/",views.afficher,name ="afficher"),
    path('rate/<int:rating>/', views.rate),
    path('process_data/', views.process_data, name='process_data'),
    path('ajouter/', views.ajouter),

]
