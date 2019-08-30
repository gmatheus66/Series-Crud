from django.shortcuts import render, redirect, get_object_or_404
from .forms import SeriesForm
from .models import Serie
from django.views.generic import ListView, DetailView


#Home view
class IndexView(ListView):
	template_name = 'Series/index.html'
	context_object_name = 'serie_list'
	"""docstring for IndexView"""
	def get_queryset(self):
		return Serie.objects.all()


#Detail view
class SerieDetailView(DetailView):
	model = Serie
	template_name = 'Series/serie-detail.html'

#New serie view
def serieview(request):
	if request.method == 'POST':
		form = SeriesForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index')
	form = SeriesForm()
	return render(request, 'Series/serie.html', {'form' : form})

#Edit a serie
def edit(request, pk, template_name='Series/edit.html'):
	serie = get_object_or_404(Serie, pk = pk)
	form = SeriesForm(request.POST or None, instance = serie)
	if form.is_valid():
		form.save()
		return redirect('index')
	return render(request, template_name, {'form': form})

#Delete serie
def delete(request, pk, template_name='Series/confirm_delete.html'):
	serie = get_object_or_404(Serie, pk=pk)
	if request.method == 'POST':
		serie.delete()
		return redirect('index')
	return render(request, template_name, {'object' : serie})