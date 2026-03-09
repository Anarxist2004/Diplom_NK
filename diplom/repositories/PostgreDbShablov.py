from interfaces.i_repository import IRepository
from services.tech_card import TechCardData
from services.tech_card import TypeObjectControl
from typing import List, Optional
import psycopg2
from psycopg2.extras import RealDictCursor

class PostgreDbShablov(IRepository[TechCardData]):
    def __init__(self, dsn: str):
        self._cards: List[TechCardData] = []
        try:
            self.conn = psycopg2.connect(dsn)
            self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)
            print("Подключение к базе успешно")
        except psycopg2.Error as e:
            print("Ошибка при подключении к базе:", e)
            self.conn = None
            self.cursor = None

    def add(self, entity: TechCardData) -> None:
        self._cards.append(entity)

    def update(self, entity: TechCardData) -> None:
        for i, card in enumerate(self._cards):
            if getattr(card, "id", None) == getattr(entity, "id", None):
                self._cards[i] = entity
                return

    def delete(self, entity: TechCardData) -> None:
        entity_id = getattr(entity, "id", None)
        self._cards = [c for c in self._cards if getattr(c, "id", None) != entity_id]

    def get_by_id(self, id: int) -> Optional[TechCardData]:
        for card in self._cards:
            if getattr(card, "id", None) == id:
                return card
        return None

    def list_all(self) -> List[TechCardData]:
        return self._cards.copy()

    def close(self) -> None:
        """Закрытие подключения к БД."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

    def get_params_for_type(self, type_id):#получение параметров всех типов контролирующего элемента
        pass


    def get_all_controlled_element_types(self)->T:#получение всех типов контролируемых эементов
        pass
    

    def get_all_objects_by_type_id(self, type_id)->T:#получние все контролируемых элементов по id типа
        pass

  
    def get_all_possible_values_by_param_and_element(self, element_type_id,param_id)->T:
        pass

    def get_params_for_element(self, element_id: int) -> T:
        """Получить все параметры и их значения для конкретного элемента (objectControl) по его id."""
        pass