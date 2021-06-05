from flask import render_template,request,redirect,url_for
from . import main


@main.route('/')
def index():
  '''
  View that returns the index page and its data
  '''

  return render_template('index.html')