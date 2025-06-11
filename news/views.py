from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'news/index.html')

def news(request):
    query = request.POST.get('query', '').strip()

    if not query:
        return HttpResponse("Please enter a search query.", status=400)

    api = "6766728e52404902aee45a5bde33974e"
    url = f"https://newsapi.org/v2/everything?q={query}&from=2025-05-11&sortBy=publishedAt&apiKey={api}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if HTTP status is not 200
        data = response.json()
        articles = data.get("articles", [])
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"API Error: {str(e)}", status=500)
    except ValueError:
        return HttpResponse("Invalid JSON response from API", status=500)

    return render(request, 'news/articles.html', {'articles': articles})
