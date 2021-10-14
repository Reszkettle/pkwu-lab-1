from fastapi import FastAPI

app = FastAPI()


@app.get("/{string_to_reverse}")
def reverse_string(string_to_reverse: str):
    ...
