from django.conf.urls import url

import events.views as event_views


urlpatterns = [
    # Future events list
    url(
        r'^$',
        event_views.EventListView.as_view(),
        name='event_list'
    ),

    # Past events list
    url(
        r'^past/$',
        event_views.PastEventListView.as_view(),
        name='past_event_list'
    ),

    # Speakers
    url(
        r'^speakers/$',
        event_views.SpeakerListView.as_view(),
        name='speaker_list'
    ),
    url(
        r'^speaker/(?P<slug>[\w-]+)/$',
        event_views.SpeakerDetailView.as_view(),
        name='speaker_detail'
    ),

    # Organizations
    url(
        r'organizations/^$',
        event_views.OrganizerListView.as_view(),
        name='organizer_list'
    ),

    # Event detail views
    url(
        r'^(?P<pk>\d+)/$',
        event_views.EventDetailView.as_view(),
        name='event_detail'
    ),
    url(
        r'^(?P<slug>[\w-]+)/$',
        event_views.EventDetailView.as_view(),
        name='event_detail'
    ),


]
