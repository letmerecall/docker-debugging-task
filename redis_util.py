import msgpack_numpy as m

from redis import StrictRedis as _StrictRedis
from nameko.extensions import DependencyProvider

m.patch()

# Key to get REDIS_URI from config.yaml
REDIS_URI_KEY = 'REDIS_URI'


class Redis(DependencyProvider):
    """
    A nameko dependency for Redis
    """
    def __init__(self, **options):
        self.client = None
        self.options = {
            'decode_responses': False,
        }
        self.options.update(options)

    def setup(self):
        self.redis_uri = self.container.config[REDIS_URI_KEY]

    def start(self):
        self.client = _StrictRedis.from_url(self.redis_uri, **self.options)

    def stop(self):
        self.client = None

    def kill(self):
        self.client = None

    def get_dependency(self, worker_ctx):
        return self.client
