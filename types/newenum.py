from aenum import Enum, auto, skip


class NewEnum(Enum):
    def __new__(cls, *args: any, **kwds: any) -> object:
        value = len(cls.__members__)
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __str__(self):
        return self.name
