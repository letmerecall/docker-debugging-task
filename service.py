from datetime import datetime

from nameko.timer import timer
from redis_util import Redis


class Service:

    name = 'service'
    redis = Redis(decode_responses = True)

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
        date_time = self.redis.get('current_datetime')

        date, time = date_time.split(' ')[0], date_time.split(' ')[1]
        [date_year, date_month, date_date] = date.split('-')

        [time_hour, time_min, time_sec] = time.split(':')
        time_sec, time_ms = time_sec.split(".")

        final_time = date_year+date_month+date_date+time_hour+time_min+time_sec+time_ms

        time_value = 0
        for char in final_time:
            time_value += int(char)

        return time_value
