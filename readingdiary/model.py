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
    def __int__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED
        self.notes = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        note = Note(text, page, date)
        self.notes.append(note)
        return True

    def set_rating(self, rating: int) -> bool:
        if rating not in (Book.EXCELENT, Book.GOOD, Book.BAD):
            return False
        self.rating = rating
        return True

    def get_notes_of_page(self, page: int):
        result = []
        for note in self.notes:
            if note.page == page:
                result.append(note)
        return result

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1
        count = {}
        for note in self.notes:
           if note.page not in count:
               count[note.page] = 0
               count[note.page] += 1

        return max(count, key=count.get)

    def __str__(self):
        if self.rating == Book.EXCELENT:
            rating_str = "excelent"
        elif self.rating == Book.GOOD:
            rating_str = "good"
        elif self.rating == Book.BAD:
            rating_str = "bad"
        else:
            rating_str = "unrated"

        return f"""ISBN: {self.isbn}
Title: {self.title}
Author: {self.author}
Pages: {self.pages}
Rating: {self.rating}"""











