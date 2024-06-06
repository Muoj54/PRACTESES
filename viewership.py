# import requests
# from django.shortcuts import render

# def home(request):
  # response = requests.get('https://api.github.com/events')
  # data = response.json()
  # results = data[0]["id"]

  # response2 = requests.get('https://dog.ceo/api/breeds/image/random')
  # data2 = response2.json()
  # results2 = data2["message"]
  # return render(request, 'templates/index.html', {'results':results, 'results2':results2})