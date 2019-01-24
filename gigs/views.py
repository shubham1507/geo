from django.shortcuts import render
from django.views.generic.base import View


class LookupView(View):
   def get(self, request):
        return render_to_response('gigs/lookup.html')
