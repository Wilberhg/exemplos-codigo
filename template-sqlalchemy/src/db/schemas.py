from pydantic import BaseModel


class CriaRegistro(BaseModel):
    first_name: str
    last_name: str
    company_name: str
    role_company: str
    address: str
    email: str
    phone_number: str


class CriaControle(BaseModel):
    id_controle_analise: int
    dado_cadastrado: bool
