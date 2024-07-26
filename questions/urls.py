from django.urls import path
from .views import *

urlpatterns = [
    path('quiz/', ListQuiz.as_view(),name='quiz'),
    path('quiz/<int:pk>', RetrieveQuiz.as_view(),name='quiz'),
    path('question/<int:pk>', RetreveQuestion.as_view(),name='question'),
    path('option/<int:question_id>', RetrieveOption.as_view(),name='option>'),
    path('user-answer/<int:pk>', User_answer.as_view(),name='answer>'),
    path('quiz_results/', submit_quiz_result, name='submit_quiz_result'),

]
