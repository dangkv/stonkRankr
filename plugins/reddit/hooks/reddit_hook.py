from airflow.hooks.base_hook import BaseHook
import praw


class RedditHook(BaseHook):
    def __init__(
        self,
        conn_id,
        *args,
        **kwargs,
    )

    self.conn_id = conn_id
    self.args = args
    self.kawrgs = kwargs

    self.connection = None
    self.extras = None
    self.reddit = None

    def get_conn(self):
        if self.reddit:
            return self.reddit
        
        self.connection = self.get_connection(self.conn_id)
        self.extras = self.connection.extra_dejson

        reddit = praw(
            client_id=self.extras['client_id'],
            client_secret=self.extras['client_secret'],
            password=self.connection.password,
            user_agent=self.extras['user_agent'],
            username=self.connection.login,
        )

        self.reddit = reddit
        return reddit
