from pydantic import BaseModel


class CiscoToAws(BaseModel):
    iface_config: str
