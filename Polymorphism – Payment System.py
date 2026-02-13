
#Polymorphism is an OOPS concept where the same method behaves differently for different objects.
#One function name, different behavior.
class Payment:
    def pay(self, amount):
        pass
class CreditCardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI")
class CashPayment(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash")
payments = [
    CreditCardPayment(),
    UPIPayment(),
    CashPayment()
]
for p in payments:
    p.pay(1000)
