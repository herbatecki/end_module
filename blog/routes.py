# blog/routes.py

from flask import render_template, request
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

# dla zwykłego wyświetlania i dodawania z konsoli
@app.route("/")
def index():
      all_posts = Entry.query.filter_by(is_published = True).order_by(Entry.pub_date.desc())
      return render_template("homepage.html", all_posts=all_posts)
   
# return render_template("base.html") # dla wyświetlania pustego szablonu strony, bez możliwości wyświetlania wpisów

@app.route("/new_post/", methods = ['GET', 'POST'])
def create_entry():
      form = EntryForm()
      errors = ''
      if request.method == 'POST':
            if form.validate_on_submit():
                  entry = Entry(
                        title = form.title.data, # co daje
                        body=form.body.data,
                        is_published = form.is_published.data
                  )
                  db.session.add(entry)
                  db.session.commit()
            else:
                  errors = form.errors
      return render_template("entry_form.html", form=form, errors=errors)