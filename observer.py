import abc

class FoodRequest:
    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        print(f"{observer} attached!")
        self._observers.add(observer)

    def detach(self, observer):
        print(f"{type(observer)} detached!")
        self._observers.discard(observer)

    def _notify(self):
        print(f"Client ask someone to: {self._subject_state}")
        for observer in self._observers:
            print(f"Notifying {type(observer)}")
            observer.update(self._subject_state)

    @property
    def subject_state(self):
        return self._subject_state

    @subject_state.setter
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()

class RestaurantObserver:
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass

class ChefObserver(RestaurantObserver):
    def update(self, arg):
        self._observer_state = arg
        print("Request ok for chef!")
        print(f"Start cooking") if self._observer_state == "COOK" else print("Nothing to cook")


class CashierObserver(RestaurantObserver):
    def update(self, arg):
        self._observer_state = arg
        print("Request ok for cashier!")
        print(f"Start charge") if self._observer_state == "PAY" else print("Nothing to charge!")

if __name__ == "__main__":
    client = FoodRequest()
    chef = ChefObserver()
    cashier = CashierObserver()
    client.attach(chef)
    client.attach(cashier)

    client.subject_state = "COOK"

    client.subject_state = "PAY"