from misc.decorator import render_to, is_ajax
from django.http import Http404, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.context_processors import csrf
from django.views.decorators.http import require_POST

from randomizer.forms import MainForm
from randomizer import *

@ensure_csrf_cookie
@render_to("index.html")
def index(request):
  output = csrf(request)
  output.update({
    "names": NAMES[:2],
    "not_in_game": NAMES[2:],
    "nations":NATIONS})
  return output



@ensure_csrf_cookie
@render_to("update.html")
def update(request):
  return csrf(request)


@is_ajax
@require_POST
def get_update(request):
  return HttpResponse("OK")

@is_ajax
@require_POST
def submit(request):
  print request.POST
  return HttpResponse("OK")