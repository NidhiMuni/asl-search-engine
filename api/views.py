from rest_framework.response import Response
from rest_framework.decorators import api_view
from translator.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone
from rest_framework import status

@api_view(['GET'])
def getData(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    questionSerializer = QuestionSerializer(questions, many = True)
    choiceSerializer = ChoiceSerializer(choices, many = True)
    return Response({'question': questionSerializer.data, 'choice': choiceSerializer.data})

from django.http import JsonResponse

@api_view(['POST'])
def vote(request):
    try:
        print("hello")
        question_ids_and_choices = request.data.get('questions', {})
        for question_id, selected_choice_ids in question_ids_and_choices.items():
            question = get_object_or_404(Question, pk=question_id)
            for choice_id in selected_choice_ids:
                choice = get_object_or_404(Choice, pk=choice_id)
                choice.votes += 1
                choice.save()
        return JsonResponse({"success": True, "message": "Votes updated successfully"})
    except Exception as e:
        return JsonResponse({"success": False, "message": "Failed to update votes", "error": str(e), "req":request})


    '''return JsonResponse()
    print("voting")
    question_ids_and_choices = request.data.get('questions', {})
    for question_id, selected_choice_ids in question_ids_and_choices.items():
        question = get_object_or_404(Question, pk=question_id)
        for choice_id in selected_choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id)
            choice.votes += 1
            choice.save()
    return JsonResponse({"message": "Votes updated suck"})'''

