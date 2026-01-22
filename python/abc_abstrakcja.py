from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Dupa(PaymentMethod):
    def pay(self, amount):
        pass
    def pays(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using credit card")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using PayPal")

# payment = PaymentMethod()  ❌ Błąd! Nie można tworzyć instancji klasy abstrakcyjnej
payment = PayPal()
payment.pay(100)
dupa = Dupa()
dupa.pays(1)