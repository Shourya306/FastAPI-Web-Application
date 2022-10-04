from pydantic import BaseModel

class linear_model(BaseModel):
    R_D:float
    Administration:float
    Marketing:float
    State_California:bool
    State_Florida:bool
    State_New_York:bool
