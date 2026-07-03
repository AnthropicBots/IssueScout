from pydantic import BaseModel


class RootResponse(BaseModel):
    """
    Root API response.
    """

    name: str
    version: str
    docs: str
    openapi: str
    health: str


class HealthResponse(BaseModel):
    """
    Health check response.
    """

    status: str
    service: str
    version: str
