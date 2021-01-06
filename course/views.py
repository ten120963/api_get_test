from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.contrib import messages


def home(request):
	import requests
	import json
	
	if request.method == 'POST':
		course = request.POST['course']
		api_request = requests.get("https://enigmatic-plains-38574.herokuapp.com/courses/" + str(course))

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."
		return render(request, 'home.html', {'api': api})		
	else:
		return render(request, 'home.html', {'course': 'Enter a Course ID Above'})	
	
	
def about(request):
	return render(request, 'about.html', {})	


def add_course(request):
	import requests
	import json

	if request.method == 'POST':
		form = CourseForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, ("Course Has Been Added!"))
			return redirect('add_course')
	else:	
		course = Course.objects.all()
		output = []
		for course_item in course:

			api_request = requests.get("https://enigmatic-plains-38574.herokuapp.com/courses/" + str(course_item))

			try:
				api = json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api = "Error..."	

		return render(request, 'add_course.html', {'course': course, 'output': output})	


def delete(request, course_id):
	item = Course.objects.get(pk=course_id)
	item.delete()
	messages.success(request, ("Course Has Been Deleted!"))
	return redirect('delete_course')	


def delete_course(request):
	course = Course.objects.all()
	return render(request, 'delete_course.html', {'course': course})			

