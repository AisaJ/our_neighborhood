from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
  url(r'^$',views.home,name='home'),
  url(r'^accounts/',include('registration.backends.simple.urls')),
  url(r'^hood/',views.hoods,name='hood-details'),
  url(r'^new/neighborhood$',views.new_hood,name='newHood'),
  url(r'^new/neighbour$',views.new_neighbour,name='newNeighbour'),
  url(r'^new/business$',views.new_business,name='newBusiness'),
]

if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
