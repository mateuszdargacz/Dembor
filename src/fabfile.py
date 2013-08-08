from fabric.api import local, prompt, run

def update():
    local("hg pull -u")
    local("python26 manage.py syncdb")
    local("python26 manage.py migrate")
    local("python26 manage.py collectstatic --noinput")
    local("touch site.wsgi")
    