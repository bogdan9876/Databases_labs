from abc import ABC
from typing import List


class GeneralService(ABC):
    _dao = None

    def find_all(self) -> List[object]:
        return self._dao.find_all()

    def find_by_id(self, key: int) -> object:
        return self._dao.find_by_id(key)

    def create(self, obj: object) -> object:
        return self._dao.create(obj)

    def create_all(self, obj_list: List[object]) -> List[object]:
        return self._dao.create_all(obj_list)

    def update(self, key: int, obj: object) -> None:
        self._dao.update(key, obj)

    def patch(self, key: int, field_name: str, value: object) -> None:
        self._dao.patch(key, field_name, value)

    def delete(self, key: int) -> None:
        self._dao.delete(key)

    def delete_all(self) -> None:
        self._dao.delete_all()