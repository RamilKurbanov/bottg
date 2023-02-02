from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import urllib
import requests
from requests_html import HTMLSession


def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.',
                      'https://google.',
                      'https://webcache.googleusercontent.',
                      'http://webcache.googleusercontent.',
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    return response

def parse_results(response):
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".VwiC3b"

    results = response.html.find(css_identifier_result)

    output = []

    i = 0
    for result in results:
        item = {
            'title': result.find(css_identifier_title, first=True).text, #заголовок
            'link': result.find(css_identifier_link, first=True).attrs['href'], #ссылка
            'text': result.find(css_identifier_text, first=True).text #краткое описание
        }

        output.append(item)

        #берем именно 5 ссылок
        i += 1

        if i >= 5:
            break

    return output


def google_search(query):
    response = get_results(query)
    return parse_results(response)


results = google_search("ВАШ ЗАПРОС")
print(results)
