from pydantic import BaseModel, field_validator, validator, Field


class Post(BaseModel):
    id: int = Field(le=2)
    title: str

    # @validator('id')
    # def check_that_id_is_less_than_two(self, v):
    #     if v > 2:
    #         raise ValueError('Id is not less than two')
    #     else:
    #         return v
