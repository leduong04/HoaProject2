Team của tôi xây dựng 1 trang web quản lý cho thuê xe có mhiều chức năng và nhiệm vụ của tôi được liệt kê dười đây

```
# 🚀 Module: Quản lý hợp đồng thuê xe (CRUD)

## 🎯 Mục tiêu
Xây dựng module **CRUD hợp đồng thuê xe** trong hệ thống quản lý thuê xe máy.



---

## 🧩 Kiến trúc sử dụng
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL



---

## 🧱 Cơ sở dữ liệu PosgresSQL HoaDB5

-- 1. Role
CREATE TABLE Role (
    RoleID SERIAL PRIMARY KEY,
    RoleName VARCHAR(50) NOT NULL
);

-- 2. UserAccount
CREATE TABLE UserAccount (
    UserID SERIAL PRIMARY KEY,
    RoleID INT NOT NULL REFERENCES Role(RoleID),
    PasswordHash VARCHAR(100) NOT NULL
);

-- 3. Branch
CREATE TABLE Branch (
    BranchID SERIAL PRIMARY KEY,
    BranchName VARCHAR(100) NOT NULL,
    Address VARCHAR(200),
    Phone CHAR(15)
);

-- 4. Employee
CREATE TABLE Employee (
    EmployeeID SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    BirthDate DATE,
    Gender VARCHAR(10),
    Phone CHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(200),
    Salary DECIMAL(15,2),
    RoleID INT REFERENCES Role(RoleID),
    BranchID INT REFERENCES Branch(BranchID),
    IsDeleted BOOLEAN DEFAULT FALSE
);

-- 5. Customer
CREATE TABLE Customer (
    CustomerID SERIAL PRIMARY KEY,
    FullName VARCHAR(100) NOT NULL,
    Phone CHAR(15),
    Email VARCHAR(100),
    Address VARCHAR(200),
    CitizenID CHAR(12),
    RegistrationDate DATE DEFAULT CURRENT_DATE,
    IsDeleted BOOLEAN DEFAULT FALSE
);

-- 6. CarBrand
CREATE TABLE CarBrand (
    BrandID SERIAL PRIMARY KEY,
    BrandName VARCHAR(100) NOT NULL
);

-- 7. CarType
CREATE TABLE CarType (
    TypeID SERIAL PRIMARY KEY,
    TypeName VARCHAR(100),
    Description VARCHAR(200),
    RentalPrice DECIMAL(15,2)
);

-- 8. Car
CREATE TABLE Car (
    CarID SERIAL PRIMARY KEY,
    LicensePlate VARCHAR(20) UNIQUE NOT NULL,
    Color VARCHAR(50),
    ManufactureYear INT,
    Status VARCHAR(100),
    TypeID INT REFERENCES CarType(TypeID),
    BrandID INT REFERENCES CarBrand(BrandID),
    OwnerBranchID INT REFERENCES Branch(BranchID),
    IsDeleted BOOLEAN DEFAULT FALSE,
    Odometer FLOAT,
    DailyRate DECIMAL(15,2),
    HourlyRate DECIMAL(15,2)
);

-- 9. Contract
CREATE TABLE Contract (
    ContractID SERIAL PRIMARY KEY,
    CustomerID INT NOT NULL REFERENCES Customer(CustomerID),
    StartDate DATE,
    EndDate DATE,
    TotalAmount DECIMAL(15,2),
    Status VARCHAR(100),
    Notes VARCHAR(200)
);

-- 10. ContractCar
CREATE TABLE ContractCar (
    ContractCarID SERIAL PRIMARY KEY,
    ContractID INT NOT NULL REFERENCES Contract(ContractID),
    CarID INT REFERENCES Car(CarID),
    Amount DECIMAL(15,2),
    ReturnMileage INT,
    CarCondition VARCHAR(100)
);

-- 11. ContractPayment
CREATE TABLE ContractPayment (
    PaymentID SERIAL PRIMARY KEY,
    ContractID INT NOT NULL REFERENCES Contract(ContractID),
    PaymentMethod VARCHAR(100),
    Amount DECIMAL(15,2),
    PaymentDate DATE DEFAULT CURRENT_DATE,
    Notes VARCHAR(200),
    PaymentType INT
);

-- 12. DeliveryReceipt
CREATE TABLE DeliveryReceipt (
    DeliveryID SERIAL PRIMARY KEY,
    ContractID INT NOT NULL REFERENCES Contract(ContractID),
    DeliveryEmployeeID INT REFERENCES Employee(EmployeeID),
    ReceiverEmployeeID INT REFERENCES Employee(EmployeeID),
    DeliveryDate DATE,
    CarConditionAtDelivery VARCHAR(200),
    Notes VARCHAR(200)
);

-- 13. ReturnReceipt
CREATE TABLE ReturnReceipt (
    ReturnID SERIAL PRIMARY KEY,
    ContractID INT NOT NULL REFERENCES Contract(ContractID),
    ReceiverEmployeeID INT REFERENCES Employee(EmployeeID),
    ReceiverBranchID INT REFERENCES Branch(BranchID),
    ReturnDate DATE,
    Notes VARCHAR(200)
);

-- 14. Surcharge
CREATE TABLE Surcharge (
    SurchargeID SERIAL PRIMARY KEY,
    SurchargeName VARCHAR(100),
    UnitPrice DECIMAL(15,2),
    Description VARCHAR(200)
);

-- 15. ContractSurcharge
CREATE TABLE ContractSurcharge (
    ContractID INT NOT NULL REFERENCES Contract(ContractID),
    SurchargeID INT REFERENCES Surcharge(SurchargeID),
    UnitPrice DECIMAL(15,2),
    Quantity INT,
    PRIMARY KEY (ContractID, SurchargeID)
);


---

## ⚙️ API cần tạo (FastAPI Router: `/contracts`)

| Method | Endpoint | Mô tả |
|--------|-----------|-------|
| `GET` | `/contracts` | Lấy danh sách hợp đồng |
| `POST` | `/contracts` | Tạo hợp đồng mới  |
| `GET` | `/contracts/{id}` | Xem chi tiết hợp đồng |
| `PUT` | `/contracts/{id}` | Cập nhật hợp đồng |
| `DELETE` | `/contracts/{id}` | Xoá hợp đồng |


---

