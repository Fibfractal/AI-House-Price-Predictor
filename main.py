from sanic import Sanic, response as res

app = Sanic(__name__)


if __name__ == "__main__":
    app.run(port = 8000)