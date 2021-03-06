from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Index page:
    url(r'^$', 'session.views.index'),

    # Login/logout:
    url(r'^login/?', 'django.contrib.auth.views.login', {'template_name' : 'login.html'}),
    url(r'^logout/?$', 'django.contrib.auth.views.logout_then_login'),

    # Registration:
    url(r'^register/?$', 'session.views.register'),

    # Profile editing:
    url(r'^profile/edit/?$', 'session.views.edit_profile'),
    url(r'^profile/edit/change_password/?$',
        'django.contrib.auth.views.password_change',
        {
            'template_name' : 'change_password.html',
            'post_change_redirect' : '/session/welcome/',
            }
        ),
)
