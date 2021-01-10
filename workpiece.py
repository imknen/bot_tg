from dastetime import date
import time
from __future__ import annotations


class Task:
    def __init__(self, part=False, progress=0):
        self.task: str
        self.description: str
        self.part = part
        self.date = Сalendar().getFreeTime()
        self.progress = progress


class Calendar:
    def __init__(self):
        self.current_date = GetCurrentDate()

    def GetFreeTime(self):
        pass

    def GetCurrentDate(self):
        pass

    def NextFreeData(self):
        pass

    def PrevData(self):
        pass


class User:
    def __init__(self, name, female):
        self.name = name
        self.female = female


def InputTask():
    pass


def GetTasksToday():
    pass


def GetTasksOfData(target_date: date) -> None:
    pass


def NextTimeTask():
    pass


def PrevTimeTask():
    pass


class IODB:
    pass
