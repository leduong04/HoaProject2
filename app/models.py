from datetime import date

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base


class Contract(Base):
    __tablename__ = "contract"

    ContractID: Mapped[int] = mapped_column("contractid", Integer, primary_key=True, index=True)
    CustomerID: Mapped[int] = mapped_column("customerid", Integer, ForeignKey("customer.customerid"), nullable=False)
    StartDate: Mapped[date | None] = mapped_column("startdate", Date, nullable=True)
    EndDate: Mapped[date | None] = mapped_column("enddate", Date, nullable=True)
    TotalAmount: Mapped[float | None] = mapped_column("totalamount", Numeric(15, 2), nullable=True)
    Status: Mapped[str | None] = mapped_column("status", String(100), nullable=True)
    Notes: Mapped[str | None] = mapped_column("notes", String(200), nullable=True)

    customer: Mapped["Customer"] = relationship(back_populates="contracts")

    __table_args__ = (
        CheckConstraint(
            "enddate IS NULL OR startdate IS NULL OR enddate >= startdate",
            name="ck_contract_date_range",
        ),
    )


class Customer(Base):
    __tablename__ = "customer"

    CustomerID: Mapped[int] = mapped_column("customerid", Integer, primary_key=True, index=True)
    FullName: Mapped[str] = mapped_column("fullname", String(100))
    Phone: Mapped[str | None] = mapped_column("phone", String(15), nullable=True)
    Email: Mapped[str | None] = mapped_column("email", String(100), nullable=True)
    Address: Mapped[str | None] = mapped_column("address", String(200), nullable=True)
    CitizenID: Mapped[str | None] = mapped_column("citizenid", String(12), nullable=True)
    RegistrationDate: Mapped[date | None] = mapped_column(
        "registrationdate", Date, server_default=text("CURRENT_DATE"), nullable=True
    )
    IsDeleted: Mapped[bool | None] = mapped_column("isdeleted", Boolean, server_default=text("FALSE"))

    contracts: Mapped[list["Contract"]] = relationship(back_populates="customer", cascade="all, delete-orphan")
