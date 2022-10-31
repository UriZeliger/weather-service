from injector import Module, provider


class TestClass:
    def say_hello(self) -> str:
        return "hello"


class IOC(Module):
    @provider
    def provide_test(self) -> TestClass:
        return TestClass()
