from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsentFormForm, DemographicsForm, QuizResponseForm, UsabilityQuestionnaireForm
from django.contrib import messages
from django.conf import settings
from django.http import Http404, JsonResponse
from .models import ConsentForm, Participant, TreatmentGroup, Demographic, Question, Response, Tutorial, UsabilityQuestionnaire
import random
import json
import os

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def method(request):
    return render(request, 'method.html')


def consent_create(request):
    if request.method == 'POST':
        form = ConsentFormForm(request.POST)
        if form.is_valid():
            # Save the form to get the ConsentForm instance
            consent_form_instance = form.save()

            # Calculate the treatment_group_id based on the current counts of participants in each group
            total_groups = 2
            group_counts = [Participant.objects.filter(treatment_group_id=group_id).count() for group_id in
                            range(1, total_groups + 1)]

            # Find the group with the fewest participants
            min_group_count = min(group_counts)
            min_group_indices = [i for i, count in enumerate(group_counts) if count == min_group_count]

            # Randomly select one of the groups with the fewest participants
            treatment_group_id = random.choice(min_group_indices) + 1

            # Create a new Participant instance with the linked consent_form_instance and the assigned treatment_group_id
            participant_instance = Participant.objects.create(
                consent_form=consent_form_instance,
                treatment_group_id=treatment_group_id
            )

            # Redirect to a success page or do something else
            return redirect('demographics', participant_id=participant_instance.id)

    else:
        form = ConsentFormForm()

    return render(request, 'consent.html', {'form': form})


def consent_edit(request, pk=None):
    if pk is not None:
        consent = get_object_or_404(ConsentForm, pk=pk)
    else:
        consent = None

    if request.method == 'POST':
        form = ConsentForm(request.POST, instance=consent)
        if form.is_valid():
            updated_consent = form.save()
            if consent is None:
                messages.success(request, "ConsentForm \"{}\" was created.".format(updated_consent))
            else:
                messages.success(request, "ConsentForm \"{}\" was updated.".format(updated_consent))
            return redirect("consent_edit", updated_consent.pk)
    else:
        form = ConsentForm(instance=consent)

    return render(request, "consent.html", {"method": request.method, "form": form})


def demographics(request, participant_id):
    try:
        participant_instance = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create')

    if request.method == 'POST':
        form = DemographicsForm(request.POST)
        if form.is_valid():
            # Save the demographics data to the Demographics table
            demographic_data = form.cleaned_data
            Demographic.objects.create(
                participant=participant_instance,
                gender=demographic_data['gender'],
                age=demographic_data['age'],
                ethnicity=demographic_data['ethnicity'],
                occupation=demographic_data['occupation'],
                education=demographic_data['education'],

            )
            # Redirect to a success page after successful form submission
            return redirect('quiz_instructions', participant_id=participant_instance.id)

    else:
        form = DemographicsForm()

    return render(request, 'demographics.html', {'form': form, 'participant': participant_instance})


def quiz_instructions(request, participant_id):
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create.html')

    return render(request, 'quiz_instructions.html', {'participant': participant })


def quiz(request, participant_id, question_number, question_attempt):
    try:
        question = Question.objects.get(id=question_number)
    except Question.DoesNotExist:
        return redirect('consent_create.html')

    form = QuizResponseForm()

    return render(request, 'quiz.html', {
        'participant_id': participant_id,
        'question': question,
        'question_attempt': question_attempt,
        'form': form,
    })


def submit_response(request, participant_id, question_number, question_attempt):
    if request.method == 'POST':
        form = QuizResponseForm(request.POST)
        if form.is_valid():
            # Process and save the response data to the model
            response_data = form.cleaned_data
            response = Response(
                participant_id=participant_id,
                question_id=question_number,
                response=response_data['response'],
                confidence=response_data['confidence'],
                reason=response_data['reason'],
                attempt=question_attempt,
            )
            response.save()

            # Calculate the next question number
            next_question_number = question_number + 1

            total_questions = Question.objects.count()
            if next_question_number > total_questions:
                # All questions have been answered, redirect based on attempt
                if question_attempt == 1:
                    return redirect('post_quiz', participant_id=participant_id)
                elif question_attempt == 2:
                    return redirect('quiz_debrief', participant_id=participant_id, tutorial_id=1)
            else:
                # Continue to the next question page
                return redirect('quiz', participant_id=participant_id, question_number=next_question_number,
                                question_attempt=question_attempt)

    # Handle form errors or GET requests
    return redirect('quiz', participant_id=participant_id, question_number=question_number, question_attempt=question_attempt)



def post_quiz(request, participant_id):
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create.html')

    return render(request, 'post_quiz.html', {'participant': participant})


def tutorial_video(request, participant_id, tutorial_id):
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create.html')

    json_file_path = os.path.join(settings.BASE_DIR, 'basicapp/fixtures/tutorial.json')
    with open(json_file_path) as json_file:
        tutorials = json.load(json_file)

    tutorial = tutorials[tutorial_id - 1]  # Adjust the index for 0-based indexing

    page_title = tutorial['fields']['page_title']
    intro_text = tutorial['fields']['intro_text']
    video_url = tutorial['fields']['video_url']

    tutorial = (Tutorial.objects.get(id=tutorial_id))
    tutorial = tutorial.page_title

    return render(request, 'tutorial_video.html', {
        'participant': participant,
        'page_title': page_title,
        'intro_text': intro_text,
        'video_url': video_url,
        'tutorial': tutorial,
    })

def tutorial_summary(request, participant_id, tutorial_id):
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create.html')

    tutorial = (Tutorial.objects.get(id=tutorial_id))
    tutorial = tutorial.page_title
    treatment_group = participant.treatment_group.name

    return render(request, 'tutorial_summary.html', {
        'participant': participant,
        'tutorial': tutorial,
        'treatment_group': treatment_group,
    })


def recapquiz_instructions(request, participant_id):
    try:
        participant = Participant.objects.get(id=participant_id)
    except Participant.DoesNotExist:
        return redirect('consent_create.html')

    return render(request, 'recapquiz_instructions.html', {'participant': participant})


def finished(request):
    return render(request, 'finished.html')


def quiz_debrief(request, participant_id, tutorial_id):
    try:
        participant = Participant.objects.get(id=participant_id)
        question = Question.objects.get(id=tutorial_id)
    except Question.DoesNotExist:
        return redirect('consent_create.html')

    form = QuizResponseForm()

    next_question_number = tutorial_id + 1

    total_questions = Question.objects.count()
    if next_question_number > total_questions:
        # All questions have been answered, redirect to the post-quiz page
        return redirect('finished')
    else:
        return render(request, 'quiz_debrief.html', {
            'participant': participant,
            'question': question,
            'next_question_number': next_question_number,
            'form': form,
        })


def usability_questionnaire(request):
    if request.method == 'POST':
        form = UsabilityQuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('finished')  # Redirect to the finished page
    else:
        form = UsabilityQuestionnaireForm()

    context = {'form': form}
    return render(request, 'usability_questionnaire.html', context)
