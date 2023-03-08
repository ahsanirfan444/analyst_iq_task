from django.shortcuts import render
from django.http import JsonResponse
from .forms import ContactForm
from django.views import View
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/admin')
def contactPage(request):
	form = ContactForm()
	return render(request, "contact.html", {"contactForm": form})

def postContact(request):
	if request.method == "POST" and request.is_ajax():
		form = ContactForm(request.POST)
		print(form,"........")
		form.save()
		return JsonResponse({"success":True}, status=200)
	return JsonResponse({"success":False}, status=400)

