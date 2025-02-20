import random
from datetime import datetime, timedelta


class TimestampGenerator():
    def generate(self):
        random_seconds = random.randint(0, 7 * 24 * 60 * 60)
        current_time = datetime.now()
        random_timestamp = current_time - timedelta(seconds=random_seconds)

        return random_timestamp
