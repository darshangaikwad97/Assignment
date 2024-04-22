from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class Company(BaseModel):
    name: str
    invoice_amount: float

class BankAccount(BaseModel):
    name: str
    weekday_limit: float
    weekend_limit: float
    instant_limit: Optional[float] = None

class TransferSchedule(BaseModel):
    company: Company
    bank_account: BankAccount
    transfer_date: datetime
