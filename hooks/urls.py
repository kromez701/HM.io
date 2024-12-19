from django.urls import path
from . import views

app_name = 'hooks'

urlpatterns = [
  path('upload/', views.upload_hook, name='upload'),
  path(
    'processing/<str:task_id>/<str:aspect_ratio>/',
    views.processing,
    name='processing'
  ),
  path(
    'check_status/<str:task_id>/', views.check_task_status, name='check_status'
  ),
  path('download_zip/<str:task_id>/', views.download_zip, name='download_zip'),
  path(
    'download_output/<path:videopath>/',
    views.download_video,
    name='download_output'
  ),
  path(
    'processing_successful/<str:task_id>/',
    views.processing_successful,
    name='processing_successful'
  ),
  path(
    'validate-google-sheet-link/',
    views.validate_google_sheet_link,
    name='validate_google_sheet_link'
  ),
  path('validate-api-key/', views.validate_api_key, name='validate_api_key'),
]
