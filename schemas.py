from pydantic import BaseModel, Field
from typing import Literal

class TicketAnalysis(BaseModel):

    category: Literal[
        "billing",
        "technical",
        "account",
        "general"
    ]

    priority: Literal[
        "low",
        "medium",
        "high"
    ]

    sentiment:Literal[
        "positive",
        "neutral",
        "frustrated",
        "angry"
    ]

    summary:str=Field(
        description="A concise summary of customer complaint"
    )

    requires_human:bool

    suggested_action: str=Field(
        description="Suggested action according to the complaint"
    )

    