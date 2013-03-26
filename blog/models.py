from google.appengine.ext import db
from django.template.defaultfilters import slugify
from google.appengine.api import users

class Article(db.Model):
    title = db.StringProperty(required=True)
    slug = db.StringProperty()
    body = db.TextProperty(required=True)
    is_published = db.BooleanProperty()
    created_by = db.UserProperty()
    created_at = db.DateTimeProperty(auto_now_add=True)
    
    def get_absolute_url(self):
        return "/articles/" + self.slug

    def get_absolute_edit_url(self):
        return "/admin/articles/" + self.slug + "/edit"

    def put(self, *args, **kwargs):
        self.slug = slugify(self.title).decode()
        self.created_by = users.get_current_user()
        super(Article, self).put(*args, **kwargs)

    def __unicode__(self):
    	return self.title
