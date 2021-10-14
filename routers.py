from fastapi import APIRouter, Depends, status
import schemas
import services
import dependencies as deps

string_router = APIRouter(prefix="/string")


@string_router.get("/{string_to_reverse}", response_model=schemas.ReverseStringResponse, status_code=status.HTTP_200_OK)
def reverse_string(string_to_reverse: str,
                   string_service: services.StringService = Depends(deps.get_string_service)):
    reversed_string = string_service.reverse_string(string_to_reverse)
    return schemas.ReverseStringResponse(reversed_string=reversed_string)
