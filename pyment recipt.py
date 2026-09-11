from abc import ABC, abstractmethod
from datetime import datetime
import uuid


# -------------------------------------------------
# 1. RECEIPT CLASS
# -------------------------------------------------

class Receipt:
    def __init__(self, amount, method, status):
        self.transaction_id = str(uuid.uuid4())[:8]
        self.amount = amount
        self.method = method
        self.status = status
        self.time = datetime.now()

    def __str__(self):
        return f"""
--------------------------------
        PAYMENT RECEIPT
--------------------------------
Transaction ID : {self.transaction_id}
Amount         : ₹{self.amount}
Payment Method : {self.method}
Status         : {self.status}
Time           : {self.time}
--------------------------------
"""


# -------------------------------------------------
# 2. ABSTRACT PAYMENT STRATEGY
# -------------------------------------------------

class PaymentStrategy(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


# -------------------------------------------------
# 3. CREDIT CARD PAYMENT
# -------------------------------------------------

class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number, cvv, expiry):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate(self):
        return (
            len(self.card_number) == 16
            and len(self.cvv) == 3
            and len(self.expiry) == 5
        )

    def pay(self, amount):

        if self.validate():
            print("Processing Credit Card payment...")
            return Receipt(amount, "Credit Card", "SUCCESS")

        return Receipt(amount, "Credit Card", "FAILED")


# -------------------------------------------------
# 4. PAYPAL PAYMENT
# -------------------------------------------------

class PayPalPayment(PaymentStrategy):

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate(self):
        return "@" in self.email and len(self.password) >= 6

    def pay(self, amount):

        if self.validate():
            print("Processing PayPal payment...")
            return Receipt(amount, "PayPal", "SUCCESS")

        return Receipt(amount, "PayPal", "FAILED")


# -------------------------------------------------
# 5. UPI PAYMENT
# -------------------------------------------------

class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):

        if self.validate():
            print("Processing UPI payment...")
            return Receipt(amount, "UPI", "SUCCESS")

        return Receipt(amount, "UPI", "FAILED")


# -------------------------------------------------
# 6. NET BANKING PAYMENT
# -------------------------------------------------

class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank_name, account_number):
        self.bank_name = bank_name
        self.account_number = account_number

    def validate(self):
        return (
            self.bank_name != ""
            and self.account_number.isdigit()
            and len(self.account_number) >= 8
        )

    def pay(self, amount):

        if self.validate():
            print("Processing Net Banking payment...")
            return Receipt(amount, "Net Banking", "SUCCESS")

        return Receipt(amount, "Net Banking", "FAILED")


# -------------------------------------------------
# 7. LOGGING DECORATOR
# -------------------------------------------------

def log_transaction(function):

    def wrapper(self, amount):

        print("\n[LOG] Payment started")
        print("[LOG] Amount:", amount)

        result = function(self, amount)

        print("[LOG] Payment completed")
        print("[LOG] Status:", result.status)

        return result

    return wrapper


# -------------------------------------------------
# 8. PAYMENT PROCESSOR - CONTEXT
# -------------------------------------------------

class PaymentProcessor:

    # Registry stores payment methods
    _registry = {}

    def __init__(self, strategy):
        self.strategy = strategy

    # Change payment method at runtime
    def set_strategy(self, strategy):
        self.strategy = strategy
        print("\n[CONFIG] Payment method changed.")

    # Process payment
    @log_transaction
    def process_payment(self, amount):

        if self.strategy is None:
            return Receipt(amount, "Unknown", "FAILED")

        return self.strategy.pay(amount)

    # Register new payment method
    @classmethod
    def register_strategy(cls, key, strategy_class):
        cls._registry[key] = strategy_class
        print("[REGISTRY] Registered:", key)

    # Show available payment methods
    @classmethod
    def available_methods(cls):
        return list(cls._registry.keys())

    # Create processor using payment method name
    @classmethod
    def create(cls, key, **kwargs):

        if key not in cls._registry:
            raise ValueError("Payment method not found!")

        strategy_class = cls._registry[key]

        strategy = strategy_class(**kwargs)

        return cls(strategy)


# =================================================
# MAIN PROGRAM
# =================================================

if __name__ == "__main__":

    print("======================================")
    print("     PAYMENT PROCESSING SYSTEM")
    print("======================================")

    # Register payment methods
    PaymentProcessor.register_strategy(
        "upi",
        UPIPayment
    )

    PaymentProcessor.register_strategy(
        "credit_card",
        CreditCardPayment
    )

    PaymentProcessor.register_strategy(
        "paypal",
        PayPalPayment
    )

    PaymentProcessor.register_strategy(
        "net_banking",
        NetBankingPayment
    )

    print("\nAvailable Payment Methods:")
    print(PaymentProcessor.available_methods())


    # ---------------------------------------------
    # UPI PAYMENT
    # ---------------------------------------------

    print("\n\n===== UPI PAYMENT =====")

    processor = PaymentProcessor.create(
        "upi",
        upi_id="student@upi"
    )

    receipt = processor.process_payment(1500)

    print(receipt)


    # ---------------------------------------------
    # CHANGE TO CREDIT CARD
    # ---------------------------------------------

    print("\n===== SWITCHING TO CREDIT CARD =====")

    credit_card = CreditCardPayment(
        "1234567812345678",
        "123",
        "12/28"
    )

    processor.set_strategy(credit_card)

    receipt = processor.process_payment(2500)

    print(receipt)


    # ---------------------------------------------
    # CHANGE TO NET BANKING
    # ---------------------------------------------

    print("\n===== SWITCHING TO NET BANKING =====")

    net_banking = NetBankingPayment(
        "SBI",
        "123456789012"
    )

    processor.set_strategy(net_banking)

    receipt = processor.process_payment(5000)

    print(receipt)


    # ---------------------------------------------
    # INVALID PAYMENT
    # ---------------------------------------------

    print("\n===== INVALID UPI PAYMENT =====")

    invalid_upi = UPIPayment(
        "invalid_upi"
    )

    processor.set_strategy(invalid_upi)

    receipt = processor.process_payment(1000)

    print(receipt)