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

import pandas as pd
import numpy as np

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

        # read in data
        edges = pd.read_csv('minimal-model/filteredEdges.csv')

        print("baby")

        # setOfSigns = pd.DataFrame()
        toConcat = []

        for i, row in enumerate(selected_results):
            thisRelation = row['selected_relation']
            thisObject = row['selected_object']
            signsWithThose = edges[edges['relation'] == str(thisRelation)][edges['object'] == str(thisObject)]
            toConcat.append(signsWithThose)

        setOfSigns = pd.concat(toConcat, ignore_index=True)

        counts = setOfSigns['subject'].value_counts()
        setOfSigns['repeat_count'] = setOfSigns['subject'].map(counts)
        setOfSigns['match_proportion'] = setOfSigns['repeat_count'] / setOfSigns['subject_count']

        max_index = np.argmax(setOfSigns['match_proportion'].values)
        highest_ratio_row = setOfSigns.loc[max_index]
        predicted_subject = highest_ratio_row['subject']
        print(predicted_subject)

        # Calculate the most voted choice overall
        #most_voted_choice = Choice.objects.order_by('-votes').first()
        #most_voted_text = most_voted_choice.choice_text if most_voted_choice else "No votes yet"

        return JsonResponse({
            "success": True,
            "message": "Match found",
            "most_voted": predicted_subject
        })
    except Exception as e:
        return JsonResponse({
            "success": False,
            "message": "Failed to update votes",
            "error": str(e)
        })
