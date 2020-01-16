daemon=True
bind='unix:/engn001/news_venv/run/gunicorn.sock news.wsgi:application'
workers=5
