# Class Author
class Author:
    all_authors = []  # Store all authors

    def __init__(self, name):
        self._name = name  # Using a private variable
        Author.all_authors.append(self)

    @property
    def name(self):
        return self._name  # Return the private variable

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Can't reassign the name")
        elif isinstance(name, str) and len(name) > 0:
            self._name = name

    def authors_written_articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines_contributed(self):
        magazines = [article.magazine for article in Article.all_articles if article.author == self]
        return set(magazines)

    def add_article(self, magazine, title):
        return Article(author=self, magazine=magazine, title=title)

    def topic_areas(self):
        categories = []
        for article in Article.all_articles:
            if article.author == self and article.magazine.category not in categories:
                categories.append(article.magazine.category)
        return categories if categories else None









# Class Magazine
class Magazine:
    all_magazines = []  # Store all magazines

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles_published(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def authors(self):
        authors = [article.author for article in Article.all_articles if article.magazine == self]
        return set(authors)

    def article_titles(self):
        titles = [article.title for article in Article.all_articles if article.magazine == self]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in Article.all_articles:
            if article.magazine == self:
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None








# Class Article
class Article:
    all_articles = []  # Store all articles

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise Exception("Can't reassign title")
        elif isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title
        else:
            raise ValueError("Title must be a string with 5 to 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self._magazine = magazine


