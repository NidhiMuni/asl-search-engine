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

@api_view(['POST'])
def vote(request, question_id):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id)
    selected_choice_ids = request.data.get('choice', [])
    print(selected_choice_ids)
    selected_choices = question.choice_set.filter(pk__in=selected_choice_ids)
    print(selected_choices)
    selected_choices.update(votes=F('votes') + 1)
    return HttpResponseRedirect(reverse("translator:results", args=(question.id,)))