import webapp2
import os
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class Post(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

class NewPost(Handler):
    def render_newpost(self, subject="", content="", error=""):
        self.render("newpost.html", subject=subject, content=content, error=error)

    def get(self):
        self.render_newpost()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if content and subject:
            a = Post(subject=subject, content=content)
            b_key = a.put()
            self.redirect("/blog/%d" % b_key.id())
        else:
            error = "we need both a title and some artwork!"
            self.render_newpost(subject, content, error)

class Permalink(Handler):
    def get(self, blog_id):
        post = Post.get_by_id(int(blog_id))
        self.render("front.html", posts=[post])

class MainPage(Handler):
    def render_front(self, subject="", content=""):
        posts = db.GqlQuery("SELECT * FROM Post "
                           "ORDER BY created DESC")

        self.render("front.html", posts=posts)

    def get(self):
        self.render_front()

app = webapp2.WSGIApplication([('/blog', MainPage),
                               ('/blog/newpost', NewPost),
                               ('/blog/(\d+)', Permalink)], debug=True)

