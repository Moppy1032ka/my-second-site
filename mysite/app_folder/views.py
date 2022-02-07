from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import SampleDB, Question, Choice, Document
from .forms import SampleForm, DocumentForm

# top page
def top_page(requests):
    return render(requests, 'app_folder/top_page.html')

# search page
class SampleView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/page01.html')

    def post(self, request, *args, **kwargs): 
        input_data = request.POST['input_data']
        result = SampleDB.objects.filter(sample1=input_data)
        try:           
            result_sample1 = result[0].sample1
            result_sample2 = result[0].sample2
        except IndexError:
            result_sample1 = input_data
            result_sample2 = 'none'
        context={'result_sample1':result_sample1, 'result_sample2':result_sample2}
        return render(request, 'app_folder/page02.html', context=context,)

search = SampleView.as_view()

# hello page
def hello(request):
    return render(request, 'app_folder/hello.html')

# touhoyou page
def poll(request):
    latest_question_list = Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'app_folder/poll.html', context=context)



def detail(request, question_id):
    try:
        question = Question.objects.filter(pub_date__lte=timezone.now()).get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'app_folder/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app_folder/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'app_folder/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app_folder:results', args=(question.id,)))


# mozinoiropage
def input_page(request):
    return render(request, 'app_folder/input_page.html')

def colorful(request):
    word1 = request.POST['sentence1']
    word2 = request.POST['sentence2']
    context = {'word1': word1, 'word2': word2}
    return render(request, 'app_folder/colorful.html', context=context)


# search add page
@login_required
def new_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'app_folder/page01.html')
    else:
        form = SampleForm()
    return render(request, 'app_folder/new_sample.html', {'form': form})

def add_question(request):
    return render(request, 'app_folder/add_question.html')


# file show and save

def allfile(request):
    fileurl = Document.objects.all()
    context = {'fileurl': fileurl}
    return render(request, 'app_folder/allfile.html', context=context)

@login_required
def modelform_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            fileurl = Document.objects.all()
            context = {'fileurl': fileurl}
            return render(request, 'app_folder/allfile.html', context=context)
    else:
        form = DocumentForm()
    return render(request, 'app_folder/modelform_upload.html', {'form': form})
