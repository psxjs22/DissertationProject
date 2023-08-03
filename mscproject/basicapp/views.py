from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsentFormForm
from django.contrib import messages
from django.http import Http404
from .models import ConsentForm, Participant, TreatmentGroup
import random


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
            total_groups = 4
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
            return render(request, 'demographics.html')

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


def demographics(request):
    return render(request, 'demographics.html')



