from datetime import datetime

class Note:
    def __init__(self, text: str, page: str, date: datetime):
        self.text: str = text
        self.page: str = page
        self.date: datetime = date

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1



