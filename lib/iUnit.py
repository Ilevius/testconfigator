from abc import ABC, abstractmethod

class IUnit(ABC):
      @abstractmethod
      def get_json(self)->dict:
          pass