from fastapi import FastAPI, Depends
import service
import dependencies as deps
import schemas

app = FastAPI()


@app.get("/{string_to_reverse}", response_model=schemas.ReverseStringResponse)
def reverse_string(string_to_reverse: str,
                   string_service: service.StringService = Depends(deps.get_string_service)):
    reversed_string = string_service.reverse_string(string_to_reverse)
    return schemas.ReverseStringResponse(reversed_string=reversed_string)
