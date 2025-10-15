from datetime import date
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ContractBase(BaseModel):
    customer_id: int = Field(..., alias="CustomerID")
    start_date: Optional[date] = Field(None, alias="StartDate")
    end_date: Optional[date] = Field(None, alias="EndDate")
    total_amount: Optional[Decimal] = Field(None, alias="TotalAmount")
    status: Optional[str] = Field(None, alias="Status")
    notes: Optional[str] = Field(None, alias="Notes")

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


class ContractCreate(ContractBase):
    pass


class ContractUpdate(BaseModel):
    customer_id: Optional[int] = Field(None, alias="CustomerID")
    start_date: Optional[date] = Field(None, alias="StartDate")
    end_date: Optional[date] = Field(None, alias="EndDate")
    total_amount: Optional[Decimal] = Field(None, alias="TotalAmount")
    status: Optional[str] = Field(None, alias="Status")
    notes: Optional[str] = Field(None, alias="Notes")

    model_config = ConfigDict(populate_by_name=True)


class ContractRead(BaseModel):
    id: int = Field(..., alias="ContractID")
    customer_id: int = Field(..., alias="CustomerID")
    start_date: Optional[date] = Field(None, alias="StartDate")
    end_date: Optional[date] = Field(None, alias="EndDate")
    total_amount: Optional[Decimal] = Field(None, alias="TotalAmount")
    status: Optional[str] = Field(None, alias="Status")
    notes: Optional[str] = Field(None, alias="Notes")

    model_config = ConfigDict(populate_by_name=True, from_attributes=True)


