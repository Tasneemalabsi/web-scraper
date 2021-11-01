import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_citations_needed_count(url):
    """
    this function takes a wikipedia link to scrape it, and returns the number of citations needed in this page
    Arguments:
    url: string
    returns: integer
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    number_of_citations_needed = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    return len(number_of_citations_needed)

def get_citations_needed_report(url):
    """
    this function takes a wikipedia link to scrape it, and returns a report for each paragraph that needs a citation in the page
    Arguments:
    url: string
    returns: string
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    number_of_citations_needed = soup.find_all("sup", class_="noprint Inline-Template Template-Fact")
    arr = []
    paragraphs = ''
    for i in number_of_citations_needed:
        paragraphs += "{}\n".format(i.parent.text) 
    return paragraphs      
        
    


# if __name__ == "__main__":
#     print(get_citations_needed_count(url))
#     print(get_citations_needed_report(url))
#     print(get_citations_needed_report(url).splitlines())