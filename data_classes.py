from typing import List
from sqlalchemy import String, Integer, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Serializer(object):
    def serialize(self):
        return {key: getattr(self, key) for key in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(element_list):
        return [element.serialize() for element in element_list]


class Base(DeclarativeBase):
    pass


class SMWHackInfo(Base, Serializer):
    __tablename__ = 'smw_hacks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    authors: Mapped[List[str]] = mapped_column(String())
    exits: Mapped[int] = mapped_column(Integer())
    difficulty: Mapped[str] = mapped_column(String())
    dates: Mapped[List[str]] = mapped_column(String())
    demo: Mapped[bool] = mapped_column(Integer())
    hall_of_fame: Mapped[bool] = mapped_column(Integer())

    def serialize(self):
        d = Serializer.serialize(self)
        return d


class YIHackInfo:
    __tablename__ = 'yi_hacks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    authors: Mapped[List[str]] = mapped_column(String())
    levels: Mapped[int] = mapped_column(Integer())
    dates: Mapped[List[str]] = mapped_column(String())
    demo: Mapped[bool] = mapped_column(Integer())


class SM64HackInfo:
    __tablename__ = 'sm64_hacks'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String())
    authors: Mapped[List[str]] = mapped_column(String())
    stars: Mapped[int] = mapped_column(Integer())
    difficulty: Mapped[str] = mapped_column(String())
    dates: Mapped[List[str]] = mapped_column(String())
    demo: Mapped[bool] = mapped_column(Integer())
