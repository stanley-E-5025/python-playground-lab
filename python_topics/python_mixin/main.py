class RoleMixInValidator:
    def validates(self, role: str):
        if role == "admin":
            return True
        else:
            return False


class ToDictMixin:
    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if not k.startswith("_")}


class UserValidatorMixin(RoleMixInValidator, ToDictMixin):
    def __init__(self, role: str, name: str):
        super().__init__()
        self.role = role
        self.name = name
        self.validate()

    def validate(self):
        if not super().validates(self.role):
            if self.role != "admin":
                if not self.name:
                    print("Name is required for non-admin users")
                else:
                    print("You have less permissions")


class MyClass(UserValidatorMixin):
    def __init__(self, x: int, y: int, role: str, name: str):
        self.x = x
        self.y = y
        super().__init__(role, name)


obj = MyClass(1, 2, "admin", "")
print(obj.to_dict())  # {'x': 1, 'y': 2}

obj2 = MyClass(1, 2, "user", "John")
print(obj2.to_dict())
# Output: {'x': 1, 'y
