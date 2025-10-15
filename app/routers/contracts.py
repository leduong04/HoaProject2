from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Contract
from ..schemas.contract import ContractCreate, ContractRead, ContractUpdate


router = APIRouter(prefix="/contracts", tags=["contracts"])


@router.get("", response_model=List[ContractRead])
def list_contracts(db: Session = Depends(get_db)):
    result = db.execute(select(Contract)).scalars().all()
    return [
        ContractRead(
            ContractID=c.ContractID,
            CustomerID=c.CustomerID,
            StartDate=c.StartDate,
            EndDate=c.EndDate,
            TotalAmount=c.TotalAmount,
            Status=c.Status,
            Notes=c.Notes,
        )
        for c in result
    ]


@router.post("", response_model=ContractRead, status_code=status.HTTP_201_CREATED)
def create_contract(payload: ContractCreate, db: Session = Depends(get_db)):
    new_contract = Contract(
        CustomerID=payload.customer_id,
        StartDate=payload.start_date,
        EndDate=payload.end_date,
        TotalAmount=payload.total_amount,
        Status=payload.status,
        Notes=payload.notes,
    )
    db.add(new_contract)
    db.commit()
    db.refresh(new_contract)
    return ContractRead(
        ContractID=new_contract.ContractID,
        CustomerID=new_contract.CustomerID,
        StartDate=new_contract.StartDate,
        EndDate=new_contract.EndDate,
        TotalAmount=new_contract.TotalAmount,
        Status=new_contract.Status,
        Notes=new_contract.Notes,
    )


@router.get("/{contract_id}", response_model=ContractRead)
def get_contract(contract_id: int, db: Session = Depends(get_db)):
    contract = db.get(Contract, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Không tìm thấy hợp đồng")
    return ContractRead(
        ContractID=contract.ContractID,
        CustomerID=contract.CustomerID,
        StartDate=contract.StartDate,
        EndDate=contract.EndDate,
        TotalAmount=contract.TotalAmount,
        Status=contract.Status,
        Notes=contract.Notes,
    )


@router.put("/{contract_id}", response_model=ContractRead)
def update_contract(contract_id: int, payload: ContractUpdate, db: Session = Depends(get_db)):
    contract = db.get(Contract, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Không tìm thấy hợp đồng")

    if payload.customer_id is not None:
        contract.CustomerID = payload.customer_id
    if payload.start_date is not None:
        contract.StartDate = payload.start_date
    if payload.end_date is not None:
        contract.EndDate = payload.end_date
    if payload.total_amount is not None:
        contract.TotalAmount = payload.total_amount
    if payload.status is not None:
        contract.Status = payload.status
    if payload.notes is not None:
        contract.Notes = payload.notes

    db.add(contract)
    db.commit()
    db.refresh(contract)

    return ContractRead(
        ContractID=contract.ContractID,
        CustomerID=contract.CustomerID,
        StartDate=contract.StartDate,
        EndDate=contract.EndDate,
        TotalAmount=contract.TotalAmount,
        Status=contract.Status,
        Notes=contract.Notes,
    )


@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contract(contract_id: int, db: Session = Depends(get_db)):
    contract = db.get(Contract, contract_id)
    if not contract:
        raise HTTPException(status_code=404, detail="Không tìm thấy hợp đồng")
    db.delete(contract)
    db.commit()
    return None


