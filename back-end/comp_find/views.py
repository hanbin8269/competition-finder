import json
from django.views import View
from django.http import JsonResponse , HttpResponse
from .site_crawling import crawlers

class ShowCompView(View):
    def get(self,request,genre_key):
        competitons = crawlers.onoffmix_crawler(genre_key)
        
        json_data = {
            'competitons' : competitons
        }
        print(json.dumps(json_data))
        return JsonResponse(json_data,status = 200,safe=False)
        