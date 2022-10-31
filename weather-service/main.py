from src.ioc import IOC, TestClass
from injector import Injector
from sanic_openapi import openapi2_blueprint
from sanic import Sanic, Request, HTTPResponse, text


app = Sanic("WeatherService")
app.blueprint(openapi2_blueprint)

ioc_container = Injector(IOC())


@app.get("/health_check")
def health_check(request: Request) -> HTTPResponse:
    global ioc_container
    test_class = ioc_container.get(TestClass)
    return text(app.config.KEY1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
