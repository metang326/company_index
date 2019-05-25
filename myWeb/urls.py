from django.conf.urls import url,include
from django.contrib import admin
import easet.views as bv

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('easet.urls',namespace='easet')),

]
