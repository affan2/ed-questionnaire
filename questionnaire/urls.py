# vim: set fileencoding=utf-8

from django.conf.urls import patterns, url
from views import questionnaire, export_csv, get_async_progress, use_session, redirect_to_prev_questionnaire


urlpatterns = patterns(
    '',
    url(r'^$',
        questionnaire, name='questionnaire_noargs'),
    url(r'^csv/(?P<qid>\d+)/(?P<only_complete>[a-zA-Z]+)/$',
        export_csv, name='export_csv'),
    url(r'^(?P<runcode>[^/]+)/progress/$',
        get_async_progress, name='progress'),
    url(r'^(?P<runcode>[^/]+)/(?P<qs>[-]{0,1}\d+)/$',
        questionnaire, name='questionset'),
)

if not use_session:
    urlpatterns += patterns(
        '',
        url(r'^(?P<runcode>[^/]+)/$',
            questionnaire, name='questionnaire'),
    )
else:
    urlpatterns += patterns(
        '',
        url(r'^$',
            questionnaire, name='questionnaire'),
        url(r'^prev/$',
            redirect_to_prev_questionnaire,
            name='redirect_to_prev_questionnaire')
    )
