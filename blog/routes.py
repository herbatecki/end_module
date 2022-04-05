# blog/routes.py

from crypt import methods
from pickle import TRUE
from flask import render_template, request, session, flash, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm, LoginForm
import functools

def login_required(view_func):
      @functools.wraps(view_func) # funckja w funkcji i dekorator na drugą funkcją
      def check_permissions(*args, **kwargs):
            if session.get('logged_in'):
                  return view_func(*args,**kwargs)
            return redirect(url_for('login', next=request.path))
      return check_permissions

# dla zwykłego wyświetlania i dodawania z konsoli
@app.route("/")
def index():
      all_posts = Entry.query.filter_by(is_published = True).order_by(Entry.pub_date.desc())
      return render_template("homepage.html", all_posts=all_posts)
   
# return render_template("base.html") # dla wyświetlania pustego szablonu strony, bez możliwości wyświetlania wpisów

"""@app.route("/edit-post/", methods = ['GET', 'POST'])  # funkcja, gdy rozbijamy na dwie funkcje - ta jest do edycji postu, wtedy trzeba w "base.html" zmienić na href = /edit-post/
def create_entry():
      form = EntryForm()
      errors = ''
      if request.method == 'POST':
            if form.validate_on_submit():
                  entry = Entry(
                        title = form.title.data, # co daje "data"?
                        body=form.body.data,
                        is_published = form.is_published.data
                  )
                  db.session.add(entry)
                  db.session.commit()
            else:
                  errors = form.errors
      return render_template("entry_form.html", form=form, errors=errors)"""

@app.route("/edit-post/<int:entry_id>", methods = ['GET', 'POST'])
@login_required
def edit_entry(entry_id=0):
      errors = None
      if entry_id == 0:
            form = EntryForm()
      else:
            entry = Entry.query.filter_by(id=entry_id).first_or_404()
            form = EntryForm(obj=entry)
      if request.method == 'POST':
            if form.validate_on_submit():
                  if entry_id == 0:
                        entry = Entry(
                              title = form.title.data, # co daje "data"?
                              body=form.body.data,
                              is_published = form.is_published.data
                        )
                        db.session.add(entry)
                        db.session.commit()
           

                  else:
                        form.populate_obj(entry)
                        db.session.commit()    
                        
      return render_template("entry_form.html", form=form, errors=errors)

"""@app.route("/edit-post/<int:entry_id>", methods = ['GET', 'POST'])
def edit_entry(entry_id):
      entry = Entry.query.filter_by(id=entry_id).first_or_404()
      form = EntryForm(obj=entry)
      errors = None # zamienne z " errors = '' "
      if request.method == 'POST':
            if form.validate_on_submit():
                  form.populate_obj(entry)
                  db.session.commit()
            else:
                  errors = form.errors
      return render_template("entry_form.html", form=form, errors=errors)"""

@app.route("/login/", methods = ['GET', 'POST'])
def login():
      form = LoginForm()
      errors = None
      next_url = request.args.get('next')
      if request.method == 'POST':
            if form.validate_on_submit():
                  session['logged_in'] = True
                  session.permanent = True # use cookie to store session.
                  flash('You are now logged in.', 'success')
                  return redirect(next_url or url_for('index'))
            else:
                  errors = form.errors
      return render_template("login_form.html", form=form, errors=errors)

@app.route('/logout/', methods = ['GET', 'POST'])
def logout():
      if request.method == "POST":
            session.clear()
            flash('You are now logged out.', 'success')
      return redirect(url_for('index'))

@app.route("/drafts/", methods = ['GET'])
@login_required
def list_drafts():
      drafts = Entry.query.filter_by(is_published = False).order_by(Entry.pub_date.desc())
      return render_template("drafts.html", drafts=drafts)