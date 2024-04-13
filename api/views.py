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
from rest_framework.decorators import api_view
from translator.models import Question, Choice

import pandas as pd

@api_view(['POST'])
def vote(request):
    try:
        selected_results = []

        question_ids_and_choices = request.data.get('questions', {})
        for question_id, selected_choice_ids in question_ids_and_choices.items():
            question = get_object_or_404(Question, pk=question_id)
            for choice_id in selected_choice_ids:
                choice = get_object_or_404(Choice, pk=choice_id)
                print(question, choice)
                choice.votes += 1
                choice.save()
                selected_results.append({'selected_relation': question, 'selected_object': choice})
                
        print(selected_results)

        most_voted_choice = Choice.objects.order_by('-votes').first()
        most_voted_text = most_voted_choice.choice_text if most_voted_choice else "No votes yet"

        return JsonResponse({
            "success": True,
            "message": "Votes updated successfully",
            "most_voted": most_voted_text
        })
    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": "Failed to update votes",
            "error": str(e)
        })
