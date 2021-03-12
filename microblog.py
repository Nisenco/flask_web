from app import app
from fakes import fake_admin, fake_categories, fake_posts, fake_comments, fake_links

if __name__ == '__main__':
    # fake_admin()
    app.run(debug=True)
