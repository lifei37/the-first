from django.conf.urls import url
from api.views.course import coursehost
from api.views.user import account
from api.views.course import newspapers

urlpatterns = [
    url(r'^login/$', account.loginView.as_view()),


    url(r'^course/$', coursehost.CourseViewSet.as_view({"get": "list"})),
    url(r'^course/(?P<pk>\d+)/$', coursehost.CourseViewSet.as_view({"get": "retrieve"})),



    url(r'^newspapers/', newspapers.NewsPapers.as_view({"get": "list"})),
    url(r'^newspapers/(?P<pk>\d+)/$', newspapers.NewsPapers.as_view({"get": "retrieve"})),


    url(r'^newspapers/(?P<pk>\d+)/agree/$', newspapers.AgreeView.as_view({'post': 'post'})),

]
