import requests
r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=Karimnagar&appid=8237f12da23286084471a504a5df0787')
with open("weather1.text",'wb') as f:
 f.write(r.content)