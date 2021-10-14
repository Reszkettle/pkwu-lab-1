from fastapi import FastAPI, Depends
import service
import dependencies as deps

app = FastAPI()


@app.get("/{string_to_reverse}")
def reverse_string(string_to_reverse: str,
                   string_service: service.StringService = Depends(deps.get_string_service)):
    ...
