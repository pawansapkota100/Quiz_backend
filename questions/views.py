from django.shortcuts import render
from rest_framework.views import APIView
from .models import Quiz, Question,Option,Result
from .serializers import quizSerializer, QuestionsSerializer,OptionsSerializer,UserAnswerSerializer,QuizResultSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class ListQuiz(APIView):
    def get(self, request):
        quiz= Quiz.objects.all()
        serializer= quizSerializer(quiz, many=True)
        return Response(serializer.data)

class RetrieveQuiz(APIView):
    def get(self, request, pk):
        quiz= Quiz.objects.get(id=pk)
        serializer= quizSerializer(quiz, many=False)
        return Response(serializer.data)

class RetreveQuestion(APIView):
    def get(self, request,pk):
        question=Question.objects.get(id=pk)
        serializer= QuestionsSerializer(question, many=False)
        return Response(serializer.data)
    
class RetrieveOption(APIView):
    def get(self, request,question_id):
        option=Option.objects.filter(question_id=question_id)
        serializer= OptionsSerializer(option, many=True)
        return Response(serializer.data)

from rest_framework import status
from .models import UserAnswer
from rest_framework.permissions import IsAuthenticated
class User_answer(APIView):
    def get(self, request,pk):
        answer= UserAnswer.objects.get(id=pk)
        serializer= UserAnswerSerializer(answer, many=False)
        return Response(serializer.data)
    
    def post(self, request):
        serializer= UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def submit_quiz_result(request):
    serializer = QuizResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_quiz_results(request):
    user = request.user
    results = Result.objects.filter(user=user)
    serializer = QuizResultSerializer(results, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)