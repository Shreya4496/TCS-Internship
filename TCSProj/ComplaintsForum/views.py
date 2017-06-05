from django.shortcuts import render, redirect, render_to_response
from .forms import ComplaintForm
# from django.views.generic import View
# from django.contrib import messages


def complaint_new(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            # data.username = request.session.get('username')
            data.save()
            return render(request, 'done.html')
    else:
        form = ComplaintForm()
    return render(request, 'complaint_new.html', {'form': form})


