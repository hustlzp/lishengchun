from fabric.api import run, env, cd, lcd, prefix

host_string = ""


def first():
    env.host_string = host_string
    run('apt-get update')
    run('apt-get dist-upgrade')

    run('apt-get install libjpeg-dev')
    run('ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib')
    run('ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib')
    run('ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib')

    with cd('/var/www/'):
        run('mkdir lsc_uploads')
        run('git clone https://github.com/hustlzp/lishengchun.git')

    env.host_string = "localhost"
    with lcd('/var/www/lishengchu/lishengchun'):
        run('scp config_remote.py %s:/var/www/lishengchun/lishengchun/config.py' % host_string)

    env.host_string = host_string
    with cd('/var/www/lishengchun'):
        # virtualenv
        run('virtualenv venv')
        with prefix('source venv/bin/activate'):
            run('pip install -r requirements.txt')

        # mysql
        run('mysql -uroot -poptico2014 < create_db.sql')
        run('python manage.py syncdb')

        # nginx
        run('cp nginx.conf /etc/nginx/sites-available/lsc')
        run('ln -sf /etc/nginx/sites-available/lsc /etc/nginx/sites-enabled/')
        run('nginx -s reload')

        # # supervisor
        run('cp supervisor.conf /etc/supervisor/conf.d/lsc.conf')
        run('supervisorctl reread')
        run('supervisorctl update')


def deploy():
    env.host_string = host_string
    with cd('/var/www/lishengchun'):
        run('git pull')
        run('supervisorctl restart lsc')


def restart():
    env.host_string = host_string
    run('supervisorctl restart lsc')