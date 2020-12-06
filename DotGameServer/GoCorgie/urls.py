from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from GoCorgie.api import ScoreAPI, UserAPI, GetAuthToken, SavegameAPI

urlpatterns = [
    
    #apis
    path('api/score', ScoreAPI.as_view()),
    path('api/user/{pk}/$', UserAPI.as_view()),
    path('api/user', UserAPI.as_view()),
    path('api/getauthtoken', GetAuthToken.as_view()),
    path('api/savegame/{pk}/$', SavegameAPI.as_view()),
    path('api/savegame', SavegameAPI.as_view()),
    path('api/savegames/', SavegameAPI.as_view()),

 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
