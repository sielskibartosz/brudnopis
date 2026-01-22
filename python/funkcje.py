import pytest

class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance
    def get_balance(self):
        return self._balance


# Testy

class TestBankAccount:
    @pytest.fixture
    def account(self):
        return BankAccount()

    def test_instance_creation(self, account):
        assert isinstance(account, BankAccount)
        assert hasattr(account, "_balance")

    def test_initial_balance(self):
        account = BankAccount(50)
        assert account.balance == 50

    def test_deposit_increases_balance(self, account):
        account.deposit(100)
        assert account.balance == 100

    def test_deposit_negative_raises(self, account):
        with pytest.raises(ValueError):
            account.deposit(-10)

    def test_withdraw_decreases_balance(self, account):
        account.deposit(100)
        account.withdraw(40)
        assert account.balance == 60

    def test_withdraw_more_than_balance_raises(self, account):
        account.deposit(50)
        with pytest.raises(ValueError):
            account.withdraw(100)

    def test_withdraw_negative_raises(self, account):
        with pytest.raises(ValueError):
            account.withdraw(-10)
