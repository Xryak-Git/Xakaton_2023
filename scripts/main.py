from abc import ABC, abstractmethod
import vk_api
import selenium
import pprint
import json
import sqlite3

from config import VK_LOGIN, VK_PASSWORD

MY_VK_ID = "56757868"
OUTPUT_PATH = r"../output/"

class AuthException(Exception):
    pass


class GetUserExeption(Exception):
    pass


class AbstractParser(ABC):
    @abstractmethod
    def parse_one(self, *args, **kwargs):
        ...


class Writer:
    @staticmethod
    def json(data: dict, file_path="groups_discription.txt"):
        with open(OUTPUT_PATH+file_path, 'a', encoding='utf8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)




class VkParser(AbstractParser):
    def __init__(self, login, password):
        vk_session = vk_api.VkApi(login=VK_LOGIN, password=VK_PASSWORD, app_id=2685278)
        try:
            vk_session.auth()
        except Exception:
            raise AuthException()

        self.vk = vk_session.get_api()
        self.users = {}

    def parse_one(self, vk_id):
        self._check_if_user_exists(vk_id=vk_id)

        groups_ids = self._parse_one_person_groups(vk_id=vk_id)
        groups_discription = self._get_groups_description(groups_ids)

        return {vk_id: groups_discription}

    def _parse_one_person_groups(self, vk_id):
        response = self.vk.groups.get(user_id=vk_id)
        groups = response["items"]
        return groups

    def _get_groups_description(self, groups_ids: []):
        response = self.vk.groups.getById(group_ids=groups_ids, fields="name, description")
        groups_description = {}
        for group in response:
            id = group["id"]
            name = group["name"]
            description = group["description"]
            groups_description[id] = {"name": name, "description": description}
        return groups_description

    def _check_if_user_exists(self, vk_id):
        try:
            self.vk.users.get(user_ids=vk_id)
        except Exception:
            raise GetUserExeption()


def main():
    vk_parser = VkParser(login=VK_LOGIN, password=VK_PASSWORD)
    data = vk_parser.parse_one(vk_id=MY_VK_ID)

    Writer.json(data=data)


if __name__ == "__main__":
    main()
