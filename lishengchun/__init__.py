# coding: utf-8
import sys
from flask import Flask, request, url_for, render_template
from flask_wtf.csrf import CsrfProtect
from flask.ext.uploads import configure_uploads
from flask_debugtoolbar import DebugToolbarExtension
from . import config

# convert python's encoding to utf8
reload(sys)
sys.setdefaultencoding('utf8')


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # CSRF protect
    CsrfProtect(app)

    if app.debug:
        DebugToolbarExtension(app)

    register_db(app)
    register_routes(app)
    register_jinja(app)
    register_error_handle(app)
    register_logger(app)
    register_uploadsets(app)

    @app.before_request
    def before_request():
        pass

    return app


def register_jinja(app):
    #from . import filters

    #app.jinja_env.filters[''] = filters.

    # inject vars into template context
    @app.context_processor
    def inject_vars():
        from .models import WorkType
        return dict(g_work_types=WorkType.query.order_by(WorkType.show_order.asc()).all())

    # url generator for pagination
    def url_for_other_page(page):
        view_args = request.view_args.copy()
        args = request.args.copy().to_dict()
        args['page'] = page
        view_args.update(args)
        return url_for(request.endpoint, **view_args)

    app.jinja_env.globals['url_for_other_page'] = url_for_other_page

    from .permissions import check_admin

    app.jinja_env.globals['check_admin'] = check_admin


def register_logger(app):
    """Send error log to admin by smtp"""
    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        credentials = (config.SMTP_USER, config.SMTP_PASSWORD)
        mail_handler = SMTPHandler((config.SMTP_SERVER, config.SMTP_PORT), config.SMTP_FROM,
                                   config.SMTP_ADMIN, 'lsc-log', credentials)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


def register_db(app):
    from .models import db
    db.init_app(app)


def register_routes(app):
    from .controllers import admin, site, work

    app.register_blueprint(site.bp, url_prefix='')
    app.register_blueprint(admin.bp, url_prefix='/admin')
    app.register_blueprint(work.bp, url_prefix='/work')


def register_error_handle(app):
    @app.errorhandler(403)
    def page_403(error):
        return render_template('site/403.html'), 403

    @app.errorhandler(404)
    def page_404(error):
        return render_template('site/404.html'), 404

    @app.errorhandler(500)
    def page_500(error):
        return render_template('site/500.html'), 500


def register_uploadsets(app):
    from .uploadsets import workimages
    configure_uploads(app, (workimages))

app = create_app()