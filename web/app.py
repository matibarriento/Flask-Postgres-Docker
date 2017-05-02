from flask import request, render_template
from index import app, db
from models import Post


@app.route('/', methods=['GET', 'POST'])
def index():
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        text = request.form['text']
        post = Post(text)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/single', methods=['GET'])
def single():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    single_posts = posts[:1]
    return render_template('index.html', posts=single_posts)

if __name__ == '__main__':
    app.run()
