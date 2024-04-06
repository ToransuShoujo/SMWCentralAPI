class SMWHackInfo:
    def __init__(self, id_=None, title=None, author=None, exits=None, difficulty=None,
                 date=None, demo=None, hall_of_fame=None, moderator=None):
        self.id_ = id_
        self.title = title
        self.author = author
        self.exits = exits
        self.difficulty = difficulty
        self.date = date
        self.demo = demo
        self.hall_of_fame = hall_of_fame
        self.moderator = moderator

    id_ = None
    title = None
    author = None
    exits = None
    difficulty = None
    date = None
    demo = None
    hall_of_fame = None
    moderator = None


class YIHackInfo:
    def __init__(self, id_=None, title=None, author=None, levels=None, date=None, demo=None, moderator=None):
        self.id_ = id_
        self.title = title
        self.author = author
        self.levels = levels
        self.date = date
        self.demo = demo
        self.moderator = moderator

    id_ = None
    title = None
    author = None
    levels = None
    date = None
    demo = None
    moderator = None


class SM64HackInfo:
    def __init__(self, id_=None, title=None, author=None, stars=None, difficulty=None, date=None, demo=None):
        self.id_ = id_
        self.title = title
        self.author = author
        self.stars = stars
        self.date = date
        self.difficulty = difficulty
        self.demo = demo

    id_ = None
    title = None
    author = None
    stars = None
    difficulty = None
    date = None
    demo = None
