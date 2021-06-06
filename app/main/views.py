from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles
from ..models import NewsSource

#views
@main.route('/')
def index():
	'''
	view root page function that returns the index the page and its data
	'''
	technology = get_sources('technology')
	business = get_sources('business')
	sports = get_sources('sports')
	entertainment = get_sources('entertainment')
	title = "News Highlighter"

	return render_template('index.html',title = title, technology = technology,business = business,sports = sports,entertainment = entertainment)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)