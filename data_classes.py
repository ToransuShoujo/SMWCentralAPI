class SMWHackInfo:
    def __init__(self, title=None, author=None, date=None, difficulty=None, exits=None, download_url=None, demo=None,
                 hall_of_fame=None, moderator=None):
        self.title = title
        self.author = author
        self.date = date
        self.difficulty = difficulty
        self.exits = exits
        self.download_url = download_url
        self.demo = demo
        self.hall_of_fame = hall_of_fame
        self.moderator = moderator

    title = None
    author = None
    date = None
    difficulty = None
    exits = None
    download_url = None
    demo = None
    hall_of_fame = None
    moderator = None


class YIHackInfo:
    def __init__(self, title=None, author=None, date=None, levels=None, demo=None, moderator=None):
        self.title = title
        self.author = author
        self.date = date
        self.levels = levels
        self.demo = demo
        self.moderator = moderator

    title = None
    author = None
    date = None
    levels = None
    demo = None
    moderator = None


class SM64HackInfo:
    def __init__(self, title=None, author=None, date=None, stars=None, difficulty=None, demo=None):
        self.title = title
        self.author = author
        self.date = date
        self.stars = stars
        self.difficulty = difficulty
        self.demo = demo

    title = None
    author = None
    date = None
    levels = None
    demo = None
    moderator = None