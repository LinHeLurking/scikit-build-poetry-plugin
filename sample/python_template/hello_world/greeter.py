from python_template import ext


class Greeter:
    def __init__(self) -> None: ...

    def simple_greet(self) -> str:
        return "Hello world!"

    def complex_greet(self, names: list[str], common_message: str) -> dict[str, str]:
        res = {}
        for name in names:
            res[name] = f"Hello, {name}! {common_message}"
        return res


class ExtGreeter:
    def __init__(self) -> None:
        self.impl = ext.Greeter()

    def simple_greet(self) -> str:
        return self.impl.simple_greet()

    def complex_greet(self, names: list[str], common_message: str) -> dict[str, str]:
        return self.impl.complex_greet(names, common_message)
