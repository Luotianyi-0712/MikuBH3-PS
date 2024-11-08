from pydantic import BaseModel


class GranterLoginBodyData(BaseModel):
    uid: str
    guest: bool
    token: str


class GranterLoginBody(BaseModel):
    app_id: int
    channel_id: int
    data: str  # Assuming this is a JSON string that can be parsed
    device: str
    sign: str

    @property
    def parsed_data(self) -> GranterLoginBodyData:
        """Parse the data field into a GranterLoginBodyData instance."""
        return GranterLoginBodyData.parse_raw(self.data)
