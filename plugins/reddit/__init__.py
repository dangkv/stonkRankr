from airflow.plugins_manager import AirflowPlugin
from reddit.hooks.reddit_hook import RedditHook

class AirflowRedditPlugin(AirflowPlugin):
    name = "RedditPlugin"
    operators = []
    sensors = []
    hooks = [RedditHook]
    excutors = []
    macros = []
    admin_views = []
    flask_blueprints = []
    menu_links = []
    appbuilder_views = []
    appbuilder_menu_items = []
    global_operator_extra_links = []
    operator_extra_links = []
