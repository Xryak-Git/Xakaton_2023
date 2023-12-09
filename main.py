import selenium
from abc import ABC, abstractmethod


class AuthException(Exception):
    pass


class AbstractParser(ABC):
    @abstractmethod
    def parse(self):
        ...

    @abstractmethod
    def get_data(self):
        ...


class VkParser(AbstractParser):
    def __init__(self):
        pass

    def parse(self):
        raise NotImplementedError()

    def get_data(self):
        raise NotImplementedError()


def main():
    pass


if __name__ == "__main__":
    main()
