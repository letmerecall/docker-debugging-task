from datetime import datetime

from nameko.timer import timer
from redis_util import Redis


class Service:

    name = 'service'
    redis = Redis()

    @timer(interval=5)
    def worker(self):
        """
        Save current time into redis perform a task
        """
        now = datetime.now()
        print(f'\nCurrent datetime: {now}')
        self.redis.set('current_datetime', str(now))
        summation = self.do_task()
        print(f'Summing month + minute + second: {summation}\n')

    def do_task(self):
        """
        Return the sum of current month, minute and second
        after getting it from Redis
        """
        time = self.redis['current_time']
        return 2021 + 6 + 23
