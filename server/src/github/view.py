__author__ = 'richa'

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import json, urllib, datetime

class ResultView(APIView):

    def post(self,request):
        api_data = {}
        url = request.data['url'].split('/')
        repository = url[3]+'/'+url[4]
        utc_datetime = datetime.datetime.utcnow()
        last_24hr = utc_datetime-datetime.timedelta(days=1)
        last_24hr = last_24hr.strftime("%Y-%m-%dT%H:%M:%S")
        last_7days = utc_datetime-datetime.timedelta(days=7)
        last_7days = last_7days.strftime("%Y-%m-%dT%H:%M:%S")

        api_url = "https://api.github.com/search/issues?q=repo:"+repository
        api_data['total_Open_issue'] = self.get_total_Open_issue(api_url)
        api_data['total_Open_issue_24'] = self.get_Open_issue_24(api_url, last_24hr)
        api_data['total_Open_issue_24_7'] = self.get_Open_issue_24_7(api_url, last_24hr, last_7days)
        api_data['total_Open_issue_7'] = self.get_Open_issue_7(api_url, last_7days)

        return Response(api_data, status=status.HTTP_200_OK)

    def get_total_Open_issue(self,api_url):
        data = urllib.urlopen(api_url+"+state:open&per_page=100").read()
        output = json.loads(data)
        return output['total_count']

    def get_Open_issue_24(self,api_url, last_24hr):

        data = urllib.urlopen(api_url+"+created:>"+last_24hr+"+state:open&per_page=100").read()
        output = json.loads(data)
        return output['total_count']

    def get_Open_issue_24_7(self, api_url, last_24hr, last_7days):

        data = urllib.urlopen(api_url+"+created:"+last_7days+".."+last_24hr+"+state:open&per_page=100").read()
        output = json.loads(data)
        return output['total_count']

    def get_Open_issue_7(self, api_url, last_7days):
        data = urllib.urlopen(api_url+"+created:<"+last_7days+"+state:open&per_page=100").read()
        output = json.loads(data)
        return output['total_count']