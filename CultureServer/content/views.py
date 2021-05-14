from django.shortcuts import render
from .models import Content
from django.views import generic 
#이 부분 확인 

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'content/index/html'
  page_template = 'content/all_contents.html'
  context_object_name = 'all_contents'
  model = Content

  def get_context_data(self, **kwargs): #얘는 뭐...
    context = super(IndexView, self).get_context_data(**kwargs)
    context.update({
      'all_contents': Content.objects.all(), #이 부분 확인 
      'page_title': 'Search Result'
    })
    return context

  def get_queryset(self):
    query = self.request.GET.get('q')
    if query:
      return Content.objects.filter(title__icontans=query)
    else:
      return Content.objects.all()
