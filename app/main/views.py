from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news


@main.route('/')
def index():
  '''
  View that returns the index page and its data
  '''

  #Getting news categories
  breaking_news = get_news('breaking')
  trending_news = get_news('trending')
  politic_news = get_news('politic')
  technology_news = get_news('technology')

  title = 'News Room'


  return render_template('index.html',title = title, breaking = breaking_news,trending = trending_news, politic = politic_news, technology = technology_news)