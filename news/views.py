from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index (request):
    return render(request, 'news/index.html')

def news(request):
    query = request.POST.get('query', '')
    api="6766728e52404902aee45a5bde33974e"
    url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-11&sortBy=publishedAt&apiKey={api}"
    c=requests.get(url)
    c=c.json()
    articles=c["articles"]
    

    return render(request, 'news/articles.html', {'articles': articles})







# api="6766728e52404902aee45a5bde33974e"

# url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-11&sortBy=publishedAt&apiKey={api}"

# c=requests.get(url)
# c=c.json()
# articles=c["articles"]

# for article in articles:
#     print( article["title"])
#     print( article["url"])
#     print("/n---------------------------/n")