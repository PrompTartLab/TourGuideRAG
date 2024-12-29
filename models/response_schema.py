from pydantic import BaseModel, Field
from typing import Literal

class RouteQuery(BaseModel):
    """Route a user query to the most relevant datasource."""
    datasource: Literal["local_tourist_spots", "foreign_tourist_spots", "restaurants", "web"] = Field(
        ..., description="Given a user question choose which datasource would be most relevant for answering their question",
    )