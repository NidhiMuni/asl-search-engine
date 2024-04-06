from django.http import HttpResponse, HttpResponseRedirect
from .models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = "translator/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Question
    template_name = "translator/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "translator/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice_ids = request.POST.getlist('choice')
        selected_choices = question.choice_set.filter(pk__in=selected_choice_ids)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "translator/detail.html",
            {
                "question": question,
                "error_message": "You didn't select any choice.",
            },
        )
    else:
        # Increment votes for all selected choices
        selected_choices.update(votes=F('votes') + 1)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("translator:results", args=(question.id,)))


from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from translator.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]