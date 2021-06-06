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
	science = get_sources('science')
	entertainment = get_sources('entertainment')
	health = get_sources('health')
	technology = get_sources('technoloy')
	business = get_sources('business')
	sports = get_sources('sports')
	title = "News Room"

	return render_template('index.html',title = title, science = science,entertainment = entertainment,health = health,technology = technology,business= business, sports = sports)

@main.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)
	title = f'NH | {id}'

	return render_template('news.html',title= title,articles = articles)