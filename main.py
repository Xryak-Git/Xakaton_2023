from abc import ABC, abstractmethod
import vk_api
import selenium

from config import VK_LOGIN, VK_PASSWORD


class AuthException(Exception):
    pass


class AbstractParser(ABC):
    @abstractmethod
    def parse_one(self):
        ...


class VkParser(AbstractParser):
    def __init__(self, login, password):
        vk_session = vk_api.VkApi(login=VK_LOGIN, password=VK_PASSWORD, app_id=2685278)
        vk_session.auth()

        self.vk = vk_session.get_api()
        self.users = []
        print(self.vk.wall.post(message='Hello world!'))

    def parse_one(self):
        pass



def main():
    vk_parser = VkParser(login=VK_LOGIN, password=VK_PASSWORD)
    vk_parser.parse_one()


if __name__ == "__main__":
    main()
