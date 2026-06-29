from abc import ABC, abstractmethod


class BaseAccount(ABC):
    """Lớp trừu tượng định nghĩa khung chuẩn cho mọi loại tài khoản ngân hàng."""

    # Class Attribute - dùng chung cho mọi instance
    bank_name = "Vietcombank"

    def __init__(self, owner_name, balance=0):
        self.owner_name = owner_name
        # Private attribute (name mangling: _BaseAccount__balance)
        self.__balance = balance

    # ---------- Property ----------
    @property
    def balance(self):
        """
        Đọc số dư tài khoản.
        Không có setter trực tiếp -> bắt buộc phải đi qua deposit()/withdraw()
        để đảm bảo nghiệp vụ (validate số tiền, log giao dịch, v.v.)
        """
        return self.__balance

    # Hàm nội bộ để các lớp con cập nhật số dư một cách an toàn
    def _update_balance(self, amount):
        self.__balance += amount

    # ---------- Abstract Methods ----------
    @abstractmethod
    def deposit(self, amount):
        """Nạp tiền vào tài khoản - mỗi loại tài khoản tự định nghĩa logic riêng."""
        pass

    @abstractmethod
    def withdraw(self, amount):
        """Rút tiền khỏi tài khoản - mỗi loại tài khoản tự định nghĩa logic riêng."""
        pass

    # ---------- Operator Overloading ----------
    def __add__(self, other):
        """
        Cộng số dư của 2 đối tượng tài khoản bất kỳ.
        Trả về tổng số tiền dạng số (int/float), không trả về object.
        """
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance + other.balance

    def __lt__(self, other):
        """So sánh số dư: self < other -> True/False"""
        if not isinstance(other, BaseAccount):
            return NotImplemented
        return self.balance < other.balance

    def __repr__(self):
        return f"{self.__class__.__name__}(owner='{self.owner_name}', balance={self.balance})"