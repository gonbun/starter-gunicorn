import sys
from gunicorn.app.wsgiapp import run
if __name__ == '__main__':
    sys.argv = "gunicorn --bind 0.0.0.0:5151 economic_site.wsgi:economic_site".split()
    sys.exit(run())
