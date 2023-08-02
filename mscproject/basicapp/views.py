from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConsentFormForm
from django.contrib import messages
from django.http import Http404


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def method(request):
    return render(request, 'method.html')


def consent_create(request):
    if request.method == "POST":
        form = ConsentFormForm(request.POST)
        if form.is_valid():
            consent = form.save()  # Save the form data to the database
            messages.success(request, "ConsentForm \"{}\" was created.".format(consent))
            return redirect("home")
    else:
        form = ConsentFormForm()

    return render(request, 'consent.html', {"method": request.method, "form": form})


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






