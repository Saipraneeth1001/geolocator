from django.shortcuts import render
import requests
# Create your views here.

def home(request): 
	response = requests.get('http://api.ipstack.com/check?access_key=something')
	geodata = response.json()
	return render(request, 'blogapi/home.html',{

		'ip': geodata['ip'],
		'country': geodata['country_name'],
		})


