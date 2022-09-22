from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import watch_xml
from mywatchlist.views import watch_json
from mywatchlist.views import show_xml_id
from mywatchlist.views import show_json_id

app_name = 'mywatchlist'

urlpatterns = {
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', watch_xml, name='watch_xml'),
    path('json/', watch_json, name='watch_json'),
    path('json/<int:id>', show_xml_id, name='show_xml_id'),
    path('xml/<int:id>', show_json_id, name='show_jason_id'),
}
