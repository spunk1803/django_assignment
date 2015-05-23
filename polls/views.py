
from django.core.urlresolvers import reverse 
from django.http import HttpResponseRedirect 
from django.views import generic
from django.shortcuts import get_object_or_404, render
from polls.models import Question, Choice 
from django.utils import timezone

class IndexView(generic.ListView): 
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):

		return Question.objects.filter(
			pub_date__lte=timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question

	template_name = 'polls/details.html'
	def get_queryset(self):
		return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'







def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {
			'question': p,
			'error_message': "you didn't select a choice.",
		})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) 

