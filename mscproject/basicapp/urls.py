from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('method/', views.method, name='method'),
    path('consent/', views.consent_create, name='consent_create'),
    path('consent/<int:pk>/', views.consent_edit, name='consent_edit'),
    path('demographics/<int:participant_id>/', views.demographics, name='demographics'),
    path('quiz_instructions/<int:participant_id>/', views.quiz_instructions, name='quiz_instructions'),
    path('quiz/<int:participant_id>/<int:question_number>/<int:question_attempt>/', views.quiz, name='quiz'),
    path('submit/<int:participant_id>/<int:question_number>/<int:question_attempt>/', views.submit_response, name='submit_response'),
    path('post_quiz/<int:participant_id>/', views.post_quiz, name='post_quiz'),
    path('tutorial_video/<int:participant_id>/<int:tutorial_id>/', views.tutorial_video, name='tutorial_video'),
    path('tutorial_summary/<int:participant_id>/<int:tutorial_id>/', views.tutorial_summary, name='tutorial_summary'),
    path('recapuiz_instructions/<int:participant_id>/', views.recapquiz_instructions, name='recapquiz_instructions'),
    path('finished/', views.finished, name='finished'),
    path('quiz_debrief/<int:participant_id>/<int:tutorial_id>/', views.quiz_debrief, name='quiz_debrief'),

]



