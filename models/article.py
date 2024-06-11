class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        # Validate data types and values
        if not isinstance(id, int):
            raise ValueError("Article ID must be an integer")
        if not isinstance(title, str) or len(title) == 0:
            raise ValueError("Article title must be a non-empty string")
        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("Article content must be a non-empty string")
        if not isinstance(author_id, int):
            raise ValueError("Author ID must be an integer")
        if not isinstance(magazine_id, int):
            raise ValueError("Magazine ID must be an integer")

        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author_id(self):
        return self._author_id

    @property
    def magazine_id(self):
        return self._magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'