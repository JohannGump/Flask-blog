from flaskblog.models import Post
from flask import render_template, request, Blueprint

main = Blueprint('main', __name__)


# posts = [
#     {
#         'auhtor': 'Corey Schafer',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'auhtor': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018'
#     }    
# ]


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    #posts = Post.query.all()
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('home.html', posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')