from pydantic import ValidationError

from prompts import SYSTEM_PROMPT
from schemas import TicketAnalysis
import ollama


def analyze_ticket(message: str) -> TicketAnalysis:

    try:
        response=ollama.chat(
            model="qwen3:8b",
            messages=[
                {"role":"system", "content":SYSTEM_PROMPT},
                {"role":"user", "content":message}
            ],
            format=TicketAnalysis.model_json_schema()
        )
    
        result= response.message.content
    
        if result is None:
            raise ValueError("LLM returned an empty response")
    
        ticket= TicketAnalysis.model_validate_json(result)
    
        return ticket

    except ollama.RequestError as e:
        raise RuntimeError(
            f"Could not connect to ollama: {e}"
        ) from e

    except ollama.ResponseError as e:
        raise RuntimeError(
            f"Ollama API error: {e}"
        ) from e

    except ValidationError as e:
        raise ValueError(
            f"Invalid ticket response: {e}"
        ) from e