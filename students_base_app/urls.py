from django.conf.urls import include, url

grouppatterns = [
    url(r'^(?P<group_id>\d+)/$', 'students_base_app.views.group_view', name='group_view'),
    url(r'^add/$', 'students_base_app.views.group_add', name='group_add'),
    url(r'^(?P<group_id>\d+)/edit/$', 'students_base_app.views.group_edit', name='group_edit'),
    url(r'^(?P<group_id>\d+)/delete/$', 'students_base_app.views.group_delete', name='group_delete'),
]

studentpatterns = [
    url(r'^add/$', 'students_base_app.views.student_add', name='student_add'),
    url(r'^(?P<student_id>\d+)/edit/$', 'students_base_app.views.student_edit', name='student_edit'),
    url(r'^(?P<student_id>\d+)/delete/$', 'students_base_app.views.student_delete', name='student_delete'),
]

accountpatterns = [
    url(r'^login/$', 'students_base_app.views.account_login', name='account_login'),
    url(r'^logout/$', 'students_base_app.views.account_logout', name='account_logout'),
]

urlpatterns = [
    url(r'^$', 'students_base_app.views.home', name='home'),
    url(r'^group/', include(grouppatterns)),
    url(r'^student/', include(studentpatterns)),
    url(r'^accounts/', include(accountpatterns)),
]

