from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return render(request, 'news/index.html')

def news(request):
    query = request.POST.get('query', '').strip()

    if not query:
        return HttpResponse("Please enter a search query.", status=400)

    api = "9d3038b02d9e54bd8f621d365f5aff6b"  # Replace with your actual GNews API key
    url = f"https://gnews.io/api/v4/search?q={query}&lang=en&token={api}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        articles = data.get("articles", [])
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"API Error: {str(e)}", status=500)
    except ValueError:
        return HttpResponse("Invalid JSON response from GNews API", status=500)

    return render(request, 'news/articles.html', {'articles': articles})
