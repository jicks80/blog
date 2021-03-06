from flask import Flask, render_template
from src.common.database import Database
from src.models.post import Article

from flask import Flask, render_template

from src.common.database import Database
from src.models.post import Article
from babel import  dates
app = Flask(__name__)  # '__main__'
app.secret_key = "jose"

'''
@app.route('/')
def home_template():
    return render_template('/html')
'''


@app.before_first_request
def initialize_database():
    Database.initialize()


# frtch all blogs
@app.route('/')
def page():
    blog = Article.fetch_all()
    return render_template('index.html', blog=blog)


# fetch a  blog by article
@app.route('/pages/<string:user>')
def pages(user):
    blog = Article.fetch_cat(user)
    return render_template('index.html', blog=blog)


@app.route('/pages1/<string:user>')
def pages1(user):
    blog = Article.fetch_article(user)
    blogs = Article.fetch_all()
    return render_template('singlepost.html', blog=blog,blogs=blogs,date=dates.format_date(blog.ArtCdate, 'full'))


if __name__ == '__main__':
    app.run(port=4550, debug=True)
