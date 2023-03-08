from ray import serve

@serve.deployment
class Hello:
    async def __call__(self) -> str:
        return "Hello world!"

app = Hello.bind()
if __name__ == "__main__":
    serve.run(app)
