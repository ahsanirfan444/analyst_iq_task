
from django.contrib import admin
from django.urls import path
from contact import views as contact
from user import views as user


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', contact.contactPage),
    path('ajax/contact', contact.postContact, name = 'contact_submit'),

]
