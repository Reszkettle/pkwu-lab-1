from pydantic import BaseModel


class ReverseStringResponse(BaseModel):
    reversed_string: str
