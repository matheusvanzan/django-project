from django.views.generic import View
from django.shortcuts import render


class IndexView(View):
	template = 'index.html'

	def __init__(self):
		super(IndexView, self).__init__()

	def get(self, request):
		return render(request, 'my_app/index.html', {})