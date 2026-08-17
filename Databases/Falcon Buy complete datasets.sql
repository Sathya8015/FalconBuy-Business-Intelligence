-- PROJECT FALCON BUY 

create database Falconbuy;
use Falconbuy;
show tables;

-- TABLE OF CUSTOMERS(1) :
CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_Code VARCHAR(20) NOT NULL UNIQUE,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Gender ENUM('Male','Female','Other') NOT NULL,
    Date_of_Birth DATE,
    Email VARCHAR(100) UNIQUE,
    Phone_Number VARCHAR(15),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    Postal_Code VARCHAR(10),
    Country VARCHAR(50),
    Region_ID INT,
    Occupation VARCHAR(100),
    Annual_Income DECIMAL(12,2),
    Marital_Status ENUM('Single','Married','Divorced','Widowed'),
    Join_Date DATE,
    Customer_Status ENUM('Active','Inactive') DEFAULT 'Active',
    Preferred_Channel ENUM('Website','Mobile App','Store'),
    Preferred_Payment_Method VARCHAR(30),
    Customer_Segment ENUM('Bronze','Silver','Gold','Platinum'),
    Referral_Source VARCHAR(100),
    Last_Login_Date DATETIME,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from customers;

-- TABLE OF CATRGORIES(2) :
CREATE TABLE Categories (
    Category_ID INT PRIMARY KEY AUTO_INCREMENT,
    Category_Code VARCHAR(20) NOT NULL UNIQUE,
    Category_Name VARCHAR(100) NOT NULL,
    Department_Name VARCHAR(100),
    Category_Description VARCHAR(255),
    Status ENUM('Active','Inactive') DEFAULT 'Active',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

select * from categories;

-- TABLE OF SUPPLIERS(3) :
CREATE TABLE Suppliers (
    Supplier_ID INT PRIMARY KEY AUTO_INCREMENT,
    Supplier_Code VARCHAR(20) NOT NULL UNIQUE,
    Supplier_Name VARCHAR(100) NOT NULL,
    Contact_Person VARCHAR(100),
    Email VARCHAR(100) UNIQUE,
    Phone_Number VARCHAR(15),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50),
    Supplier_Rating DECIMAL(2,1),
    Contract_Start_Date DATE,
    Status ENUM('Active','Inactive') DEFAULT 'Active',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from suppliers;

-- TABLE OF PRODUCTS(4) :
CREATE TABLE Products (
    Product_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_Code VARCHAR(20) NOT NULL UNIQUE,
    Product_Name VARCHAR(150) NOT NULL,
    Category_ID INT,
    Supplier_ID INT,
    Brand VARCHAR(100),
    Cost_Price DECIMAL(10,2),
    Selling_Price DECIMAL(10,2),
    Profit_Margin DECIMAL(5,2),
    Product_Status ENUM('Available','Out of Stock','Discontinued')
        DEFAULT 'Available',
    Launch_Date DATE,
    Warranty_Months INT,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from products;

-- TABLE OF REGIONS(5) :
CREATE TABLE Regions (
    Region_ID INT PRIMARY KEY AUTO_INCREMENT,
    Region_Name VARCHAR(100) NOT NULL,
    Country VARCHAR(50),
    State VARCHAR(50),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from regions;

-- TABLE OF STORES(6) :
CREATE TABLE Stores (
    Store_ID INT PRIMARY KEY AUTO_INCREMENT,
    Store_Code VARCHAR(20) NOT NULL UNIQUE,
    Store_Name VARCHAR(100) NOT NULL,
    Region_ID INT,
    City VARCHAR(50),
    Manager_Name VARCHAR(100),
    Store_Type ENUM('Retail','Warehouse','Flagship','Franchise'),
    Opening_Date DATE,
    Status ENUM('Open','Closed') DEFAULT 'Open',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from stores;

-- TABLE OF DEPARTMENTS(7) :
CREATE TABLE Departments (
    Department_ID INT PRIMARY KEY AUTO_INCREMENT,
    Department_Name VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select  * from departments;

-- TABLE OF EMPLOYEES(8) :
CREATE TABLE Employees (
    Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
    Employee_Code VARCHAR(20) NOT NULL UNIQUE,
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Department_ID INT,
    Store_ID INT,
    Email VARCHAR(100),
    Phone_Number VARCHAR(15),
    Designation VARCHAR(100),
    Salary DECIMAL(10,2),
    Hire_Date DATE,
    Status ENUM('Active','Inactive') DEFAULT 'Active',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from employees;

-- TABLE OF  WAREHOUSES(9) :
CREATE TABLE Warehouses (
    Warehouse_ID INT PRIMARY KEY AUTO_INCREMENT,
    Warehouse_Code VARCHAR(20) NOT NULL UNIQUE,
    Warehouse_Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    Country VARCHAR(50),
    Capacity INT,
    Manager_Name VARCHAR(100),
    Contact_Number VARCHAR(15),
    Status ENUM('Active','Inactive') DEFAULT 'Active',
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Warehouses;

-- TABLE OF INVENTORY(10) :
CREATE TABLE Inventory (
    Inventory_ID INT PRIMARY KEY AUTO_INCREMENT,
    Product_ID INT,
    Warehouse_ID INT,
    Stock_Quantity INT,
    Reorder_Level INT,
    Maximum_Stock INT,
    Stock_Status ENUM('In Stock','Low Stock','Out of Stock'),
    Last_Stock_Update DATE,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Inventory;


-- TABLE OF ORDERS(11) :
CREATE TABLE Orders (
    Order_ID INT PRIMARY KEY AUTO_INCREMENT,
    Order_Number VARCHAR(20) NOT NULL UNIQUE,
    Customer_ID INT,
    Store_ID INT,
    Coupon_ID INT,
    Order_Date DATETIME,
    Order_Status ENUM('Pending','Confirmed','Shipped','Delivered','Cancelled','Returned'),
    Payment_Status ENUM('Pending','Paid','Failed','Refunded'),
    Order_Total DECIMAL(12,2),
    Tax_Amount DECIMAL(10,2),
    Shipping_Charge DECIMAL(10,2),
    Net_Amount DECIMAL(12,2),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Orders;

-- TABLE OF ORDER DETAILS(12) :
CREATE TABLE Order_Details (
    Order_Detail_ID INT PRIMARY KEY AUTO_INCREMENT,
    Order_ID INT,
    Product_ID INT,
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Discount DECIMAL(10,2),
    Line_Total DECIMAL(12,2),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Order_Details;

-- TABLE OF PAYMENTS(13) :
CREATE TABLE Payments (
    Payment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Order_ID INT,
    Transaction_ID VARCHAR(100),
    Payment_Method ENUM('Cash','Credit Card','Debit Card','UPI','Net Banking','Wallet'),
    Payment_Date DATETIME,
    Amount DECIMAL(12,2),
    Payment_Status ENUM('Success','Pending','Failed','Refunded'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Payments;

-- TABLE OF DELIVERY PARTNERS(14) :
CREATE TABLE Delivery_Partners (
    Delivery_Partner_ID INT PRIMARY KEY AUTO_INCREMENT,
    Partner_Name VARCHAR(100),
    Contact_Number VARCHAR(15),
    Email VARCHAR(100),
    Service_Area VARCHAR(100),
    Rating DECIMAL(2,1),
    Status ENUM('Active','Inactive'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Delivery_Partners;


-- TABLE OF SHIPMENTS(15) :
CREATE TABLE Shipments (
    Shipment_ID INT PRIMARY KEY AUTO_INCREMENT,
    Order_ID INT,
    Delivery_Partner_ID INT,
    Tracking_Number VARCHAR(100),
    Shipment_Date DATE,
    Delivery_Date DATE,
    Delivery_Status ENUM('Pending','Shipped','In Transit','Delivered','Returned'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Shipments;


-- TABLE OF RETURNS(16) :
CREATE TABLE Returns (
    Return_ID INT PRIMARY KEY AUTO_INCREMENT,
    Order_ID INT,
    Product_ID INT,
    Return_Date DATE,
    Return_Reason VARCHAR(255),
    Refund_Amount DECIMAL(10,2),
    Return_Status ENUM('Requested','Approved','Rejected','Completed'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Returns;

-- TABLE OF MARKETING CAMPAIGNS(17) :
CREATE TABLE Marketing_Campaigns (
    Campaign_ID INT PRIMARY KEY AUTO_INCREMENT,
    Campaign_Name VARCHAR(100),
    Campaign_Type VARCHAR(50),
    Start_Date DATE,
    End_Date DATE,
    Budget DECIMAL(12,2),
    Revenue_Generated DECIMAL(12,2),
    ROI DECIMAL(10,2),
    Status ENUM('Planned','Active','Completed'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Marketing_Campaigns;

-- TABLE OF COUPONS(18) :
CREATE TABLE Coupons (
    Coupon_ID INT PRIMARY KEY AUTO_INCREMENT,
    Coupon_Code VARCHAR(30) UNIQUE,
    Discount_Type ENUM('Percentage','Fixed'),
    Discount_Value DECIMAL(10,2),
    Minimum_Order_Value DECIMAL(10,2),
    Expiry_Date DATE,
    Status ENUM('Active','Expired','Disabled'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Coupons;

-- TABLE OF LOYALTY PROGRAM(19) :
CREATE TABLE Loyalty_Program (
    Loyalty_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_ID INT,
    Membership_Level ENUM('Bronze','Silver','Gold','Platinum'),
    Reward_Points INT,
    Join_Date DATE,
    Expiry_Date DATE,
    Status ENUM('Active','Inactive'),
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Loyalty_Program;

-- TABLE OF PRODUCT REVIEWS(20) :
CREATE TABLE Product_Reviews (
    Review_ID INT PRIMARY KEY AUTO_INCREMENT,
    Customer_ID INT,
    Product_ID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Review_Title VARCHAR(150),
    Review_Text TEXT,
    Review_Date DATE,
    Created_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Updated_At TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);
select * from Product_Reviews;

-- FOREIGN KEY INSERTION :
-- CUSTOMER TABLE --
ALTER TABLE Customers
ADD CONSTRAINT FK_Customers_Regions
FOREIGN KEY (Region_ID)
REFERENCES Regions(Region_ID);

-- PRODUCTS TABLE --
ALTER TABLE Products
ADD CONSTRAINT FK_Products_Categories
FOREIGN KEY (Category_ID)
REFERENCES Categories(Category_ID);

ALTER TABLE Products
ADD CONSTRAINT FK_Products_Suppliers
FOREIGN KEY (Supplier_ID)
REFERENCES Suppliers(Supplier_ID);

-- STORES TABLE -- 
ALTER TABLE Stores
ADD CONSTRAINT FK_Stores_Regions
FOREIGN KEY (Region_ID)
REFERENCES Regions(Region_ID);

-- EMPLOYEES TABLE -- 
ALTER TABLE Employees
ADD CONSTRAINT FK_Employees_Departments
FOREIGN KEY (Department_ID)
REFERENCES Departments(Department_ID);

ALTER TABLE Employees
ADD CONSTRAINT FK_Employees_Stores
FOREIGN KEY (Store_ID)
REFERENCES Stores(Store_ID);

-- INVENTORY TABLE -- 
ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Products
FOREIGN KEY (Product_ID)
REFERENCES Products(Product_ID);

ALTER TABLE Inventory
ADD CONSTRAINT FK_Inventory_Warehouses
FOREIGN KEY (Warehouse_ID)
REFERENCES Warehouses(Warehouse_ID);

-- ORDERS TABLE -- 
ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Customers
FOREIGN KEY (Customer_ID)
REFERENCES Customers(Customer_ID);

ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Stores
FOREIGN KEY (Store_ID)
REFERENCES Stores(Store_ID);

ALTER TABLE Orders
ADD CONSTRAINT FK_Orders_Coupons
FOREIGN KEY (Coupon_ID)
REFERENCES Coupons(Coupon_ID);

-- ORDER DETAILS TABLE -- 
ALTER TABLE Order_Details
ADD CONSTRAINT FK_OrderDetails_Orders
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

ALTER TABLE Order_Details
ADD CONSTRAINT FK_OrderDetails_Products
FOREIGN KEY (Product_ID)
REFERENCES Products(Product_ID);

--  PAYEMENTS TABLE -- 
ALTER TABLE Payments
ADD CONSTRAINT FK_Payments_Orders
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

-- SHIPMENT TABLE -- 
ALTER TABLE Shipments
ADD CONSTRAINT FK_Shipments_Orders
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

ALTER TABLE Shipments
ADD CONSTRAINT FK_Shipments_DeliveryPartners
FOREIGN KEY (Delivery_Partner_ID)
REFERENCES Delivery_Partners(Delivery_Partner_ID);

-- RETURNS TABLE -- 
ALTER TABLE Returns
ADD CONSTRAINT FK_Returns_Orders
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

ALTER TABLE Returns
ADD CONSTRAINT FK_Returns_Products
FOREIGN KEY (Product_ID)
REFERENCES Products(Product_ID);

-- LOYALTY PROGRAM -- 
ALTER TABLE Loyalty_Program
ADD CONSTRAINT FK_Loyalty_Customers
FOREIGN KEY (Customer_ID)
REFERENCES Customers(Customer_ID);

-- PRODUCT REVIEWS --
ALTER TABLE Product_Reviews
ADD CONSTRAINT FK_Reviews_Customers
FOREIGN KEY (Customer_ID)
REFERENCES Customers(Customer_ID);

ALTER TABLE Product_Reviews
ADD CONSTRAINT FK_Reviews_Products
FOREIGN KEY (Product_ID)
REFERENCES Products(Product_ID);

/*
| Parent Table      | Child Table     |
| ----------------- | --------------- |
| Regions           | Customers       |
| Regions           | Stores          |
| Loyalty_Program   | Customers       |
| Categories        | Products        |
| Suppliers         | Products        |
| Departments       | Employees       |
| Stores            | Employees       |
| Warehouses        | Inventory       |
| Products          | Inventory       |
| Customers         | Orders          |
| Stores            | Orders          |
| Coupons           | Orders          |
| Orders            | Order_Details   |
| Products          | Order_Details   |
| Orders            | Payments        |
| Orders            | Shipments       |
| Delivery_Partners | Shipments       |
| Orders            | Returns         |
| Products          | Returns         |
| Customers         | Loyalty_Program |
| Customers         | Product_Reviews |
| Products          | Product_Reviews |
*/

-- MASTER TABLE 1 -- 
insert into  Regions (Region_Name, Country, State)values
('South Zone', 'India', 'Tamil Nadu'),
('South Zone', 'India', 'Karnataka'),
('South Zone', 'India', 'Kerala'),
('South Zone', 'India', 'Telangana'),
('West Zone', 'India', 'Maharashtra'),
('West Zone', 'India', 'Gujarat'),
('North Zone', 'India', 'Delhi'),
('North Zone', 'India', 'Punjab'),
('East Zone', 'India', 'West Bengal'),
('Central Zone', 'India', 'Madhya Pradesh');
select * from regions;

-- MASTER TABLE 2 --
insert into Categories(Category_Code, Category_Name, Department_Name, Category_Description)values
('CAT001','Electronics','Technology','Smart devices and electronic gadgets'),
('CAT002','Mobile Phones','Technology','Smartphones and accessories'),
('CAT003','Computers','Technology','Laptops, desktops and peripherals'),
('CAT004','Home Appliances','Home','Kitchen and home appliances'),
('CAT005','Furniture','Home','Home and office furniture'),
('CAT006','Fashion','Lifestyle','Clothing and apparel'),
('CAT007','Footwear','Lifestyle','Shoes, sandals and sneakers'),
('CAT008','Beauty','Lifestyle','Cosmetics and personal care'),
('CAT009','Health','Healthcare','Health and wellness products'),
('CAT010','Groceries','Food','Daily grocery essentials'),
('CAT011','Beverages','Food','Soft drinks and beverages'),
('CAT012','Sports','Lifestyle','Sports equipment and fitness'),
('CAT013','Books','Education','Books and stationery'),
('CAT014','Toys','Kids','Toys and games'),
('CAT015','Baby Care','Kids','Baby products'),
('CAT016','Jewellery','Luxury','Gold, silver and fashion jewellery'),
('CAT017','Automotive','Automobile','Vehicle accessories'),
('CAT018','Pet Supplies','Lifestyle','Pet food and accessories'),
('CAT019','Office Supplies','Business','Office essentials'),
('CAT020','Garden','Home','Gardening tools and accessories');
select * from categories;

-- MASTER TABLE 3 -- 
insert into  Suppliers
(Supplier_Code, Supplier_Name, Contact_Person, Email, Phone_Number,Address, City, State, Country, Supplier_Rating, Contract_Start_Date)values

('SUP001','Samsung India Pvt Ltd','Rajesh Kumar','contact@samsungsupplier.com','9876543201',
'Electronic City','Bengaluru','Karnataka','India',4.9,'2022-01-10'),

('SUP002','Apple Distribution India','Anita Sharma','sales@appledist.in','9876543202',
'BKC','Mumbai','Maharashtra','India',4.8,'2021-08-15'),

('SUP003','HP India','Vikram Patel','info@hpindia.com','9876543203',
'Whitefield','Bengaluru','Karnataka','India',4.7,'2020-05-22'),

('SUP004','Dell Technologies India','Kiran Rao','support@dellindia.com','9876543204',
'HITEC City','Hyderabad','Telangana','India',4.8,'2021-02-18'),

('SUP005','Nike India','Arjun Singh','sales@nikeindia.com','9876543205',
'DLF Cyber City','Gurugram','Haryana','India',4.6,'2023-03-12'),

('SUP006','Adidas India','Sneha Gupta','contact@adidasindia.com','9876543206',
'Connaught Place','New Delhi','Delhi','India',4.5,'2022-06-20'),

('SUP007','LG Electronics India','Rahul Mehta','support@lgindia.com','9876543207',
'Noida Sector 62','Noida','Uttar Pradesh','India',4.7,'2021-10-01'),

('SUP008','Sony India','Amit Verma','info@sonyindia.com','9876543208',
'Andheri East','Mumbai','Maharashtra','India',4.8,'2020-12-14'),

('SUP009','Lenovo India','Priya Nair','sales@lenovoindia.com','9876543209',
'Electronic City','Bengaluru','Karnataka','India',4.6,'2022-09-05'),

('SUP010','Boat Lifestyle','Rohit Agarwal','business@boat.com','9876543210',
'Okhla','New Delhi','Delhi','India',4.5,'2023-01-11');
select * from suppliers;

-- MASTER TABLE 4 --
insert into  Warehouses
(Warehouse_Code, Warehouse_Name, Address, City, State, Country,Capacity, Manager_Name, Contact_Number)values

('WH001','Chennai Central Warehouse',
'SIPCOT Industrial Park','Chennai','Tamil Nadu','India',
50000,'Arun Kumar','9876501001'),

('WH002','Bengaluru Distribution Center',
'Electronic City Phase 2','Bengaluru','Karnataka','India',
60000,'Ramesh Gowda','9876501002'),

('WH003','Mumbai Logistics Hub',
'Navi Mumbai MIDC','Mumbai','Maharashtra','India',
75000,'Vikas Sharma','9876501003'),

('WH004','Hyderabad Fulfillment Center',
'HITEC City','Hyderabad','Telangana','India',
55000,'Sai Krishna','9876501004'),

('WH005','Delhi North Warehouse',
'Okhla Industrial Area','New Delhi','Delhi','India',
70000,'Rahul Verma','9876501005'),

('WH006','Kolkata Distribution Hub',
'Salt Lake Sector V','Kolkata','West Bengal','India',
45000,'Sourav Das','9876501006'),

('WH007','Ahmedabad Warehouse',
'SG Highway','Ahmedabad','Gujarat','India',
40000,'Ketan Patel','9876501007'),

('WH008','Pune Fulfillment Center',
'Hinjewadi Phase 1','Pune','Maharashtra','India',
50000,'Nikhil Joshi','9876501008'),

('WH009','Lucknow Distribution Center',
'Transport Nagar','Lucknow','Uttar Pradesh','India',
35000,'Anil Mishra','9876501009'),

('WH010','Coimbatore Warehouse',
'SIDCO Industrial Estate','Coimbatore','Tamil Nadu','India',
45000,'Prakash Raj','9876501010');
select * from warehouses;

-- MASTER TABLE 5 --
insert into  Stores(Store_Code, Store_Name, Region_ID, City, Manager_Name, Store_Type, Opening_Date)values
('STR001','FalconBuy Chennai Central',1,'Chennai','Arun Kumar','Flagship','2021-01-15'),
('STR002','FalconBuy Bengaluru East',2,'Bengaluru','Ramesh Gowda','Flagship','2021-03-12'),
('STR003','FalconBuy Kochi Mall',3,'Kochi','Anand Nair','Retail','2022-04-20'),
('STR004','FalconBuy Hyderabad Tech',4,'Hyderabad','Sai Krishna','Retail','2022-06-10'),
('STR005','FalconBuy Mumbai Premium',5,'Mumbai','Vikas Sharma','Flagship','2020-08-18'),
('STR006','FalconBuy Ahmedabad Plaza',6,'Ahmedabad','Ketan Patel','Retail','2022-01-11'),
('STR007','FalconBuy Delhi Elite',7,'New Delhi','Rahul Verma','Flagship','2019-12-05'),
('STR008','FalconBuy Chandigarh Square',8,'Chandigarh','Amit Singh','Retail','2023-02-08'),
('STR009','FalconBuy Kolkata Central',9,'Kolkata','Sourav Das','Retail','2021-11-17'),
('STR010','FalconBuy Bhopal City',10,'Bhopal','Manish Tiwari','Retail','2022-09-30'),

('STR011','FalconBuy Pune Metro',5,'Pune','Nikhil Joshi','Flagship','2021-06-15'),
('STR012','FalconBuy Coimbatore Hub',1,'Coimbatore','Prakash Raj','Retail','2022-08-21'),
('STR013','FalconBuy Jaipur Center',7,'Jaipur','Deepak Sharma','Retail','2020-11-10'),
('STR014','FalconBuy Lucknow Plaza',10,'Lucknow','Anil Mishra','Retail','2023-01-05'),
('STR015','FalconBuy Indore Mall',10,'Indore','Rohit Soni','Retail','2021-12-18'),
('STR016','FalconBuy Bhubaneswar Square',9,'Bhubaneswar','Sanjay Das','Retail','2022-05-22'),
('STR017','FalconBuy Visakhapatnam Port',4,'Visakhapatnam','Karthik Rao','Retail','2020-09-14'),
('STR018','FalconBuy Nagpur Central',5,'Nagpur','Ashish Patil','Retail','2021-07-19'),
('STR019','FalconBuy Surat Prime',6,'Surat','Jignesh Patel','Retail','2022-02-25'),
('STR020','FalconBuy Patna City',10,'Patna','Ravi Kumar','Retail','2023-04-03'),

('STR021','FalconBuy Vijayawada Hub',4,'Vijayawada','Harish Reddy','Retail','2021-10-08'),
('STR022','FalconBuy Mysuru Mall',2,'Mysuru','Mahesh Gowda','Retail','2022-06-28'),
('STR023','FalconBuy Madurai Junction',1,'Madurai','Suresh Kumar','Retail','2020-05-12'),
('STR024','FalconBuy Guwahati Plaza',9,'Guwahati','Bikash Deka','Retail','2023-03-18'),
('STR025','FalconBuy Noida Tech Square',7,'Noida','Pankaj Tyagi','Flagship','2021-09-27');
select * from stores;

-- MASTER TABLE 6 --
insert into  Departments(Department_Name, Description)values

('Sales',
'Handles customer sales and revenue generation.'),

('Marketing',
'Manages advertising, promotions and customer acquisition.'),

('Human Resources',
'Responsible for recruitment, training and employee welfare.'),

('Finance',
'Handles accounting, budgeting and financial reporting.'),

('Information Technology',
'Maintains software, hardware and cybersecurity.'),

('Operations',
'Oversees daily business operations and process management.'),

('Supply Chain',
'Manages procurement, inventory and logistics.'),

('Customer Support',
'Handles customer queries, complaints and after-sales service.'),

('Business Intelligence',
'Analyzes business data and creates reports and dashboards.'),

('Research & Development',
'Develops new business strategies and innovative solutions.');
select * from departments;

-- MASTER TABLE 7 --
insert into  Delivery_Partners(Partner_Name, Contact_Number, Email, Service_Area, Rating, Status)values

('Blue Dart Express','9876502001','support@bluedart.com','Pan India',4.8,'Active'),

('Delhivery','9876502002','support@delhivery.com','Pan India',4.7,'Active'),

('DTDC Express','9876502003','support@dtdc.com','Pan India',4.5,'Active'),

('Ecom Express','9876502004','support@ecomexpress.com','Pan India',4.6,'Active'),

('Xpressbees','9876502005','support@xpressbees.com','Pan India',4.7,'Active'),

('India Post','9876502006','support@indiapost.gov.in','Pan India',4.3,'Active'),

('Shadowfax','9876502007','support@shadowfax.in','South & West India',4.5,'Active'),

('Ekart Logistics','9876502008','support@ekartlogistics.com','Pan India',4.8,'Active'),

('DHL Express India','9876502009','support@dhl.com','International & Metro Cities',4.9,'Active'),

('FedEx India','9876502010','support@fedex.com','International & Pan India',4.8,'Active');
select * from delivery_partners;

-- MASTER TABLE 8 --
insert into Coupons(Coupon_Code, Discount_Type, Discount_Value, Minimum_Order_Value, Expiry_Date, Status)values

('WELCOME10','Percentage',10,500,'2027-12-31','Active'),
('WELCOME20','Percentage',20,1000,'2027-12-31','Active'),
('NEWUSER500','Fixed',500,3000,'2027-12-31','Active'),
('FESTIVE15','Percentage',15,2000,'2027-11-15','Active'),
('DIWALI25','Percentage',25,5000,'2027-11-10','Active'),
('HOLI10','Percentage',10,1000,'2027-03-20','Active'),
('SUMMER500','Fixed',500,4000,'2027-06-30','Active'),
('WINTER15','Percentage',15,2500,'2027-12-20','Active'),
('BIGSALE30','Percentage',30,8000,'2027-10-31','Active'),
('SAVE1000','Fixed',1000,10000,'2027-12-31','Active'),

('FREESHIP','Fixed',200,1000,'2027-12-31','Active'),
('ELECTRO15','Percentage',15,5000,'2027-09-30','Active'),
('FASHION20','Percentage',20,3000,'2027-08-31','Active'),
('HOME500','Fixed',500,5000,'2027-07-31','Active'),
('GROCERY10','Percentage',10,1500,'2027-12-31','Active'),
('BOOK100','Fixed',100,800,'2027-12-31','Active'),
('SPORTS15','Percentage',15,2500,'2027-12-31','Active'),
('BEAUTY20','Percentage',20,2000,'2027-12-31','Active'),
('FLASH50','Percentage',50,15000,'2027-05-31','Active'),
('YEAREND25','Percentage',25,6000,'2027-12-31','Active');
select * from coupons;

-- TOTAL RECORDS IN MASTER TABLES (8 + 12) -- 
use falconbuy;
select * from categories;   -- 20 records
select count(*) from  Categories;

select * from coupons;    -- 20 records
select count(*) from  Coupons;

select * from customers;	-- 5000 records
select count(*) from customers;

select * from delivery_partners; 	-- 20 records
select count(*)  from delivery_partners;

select * from Departments;		-- 10 records
select count(*) from  Departments;

select * from employees;		-- 250 records
select count(*) from employees;

select * from inventory;		-- 5000 records
select count(*) from inventory;

select * from loyalty_program;  	-- 5000 records
select count(*)  from loyalty_program;

select * from marketing_campaigns;		-- 100 records
select count(*) from marketing_campaigns;

select * from order_details;		-- 80000 records
select count(*) from order_details;

select * from orders;			-- 20000 records
select count(*) from orders;

select * from payments;			-- 20000 records
select count(*) from payments;

select * from product_reviews;		-- 10000 records
select count(*) from product_reviews;

select * from products;			-- 500 records
select count(*) from products;

select * from Regions;			-- 10 records
select count(*) from Regions;

select * from returns;			-- 3000 records
select count(*) from returns;

select * from shipments;		-- 20000 records
select count(*) from shipments;

select * from Stores;			-- 20 records
select count(*) from  Stores;

select * from Suppliers;		-- 10 records
select count(*) from  Suppliers;

select * from warehouses;		-- 10 records
select count(*) from  Warehouses;

-- CALL PROCEDURES 1 :
delimiter $$
create procedure alltable()
begin

select * from Customers;
select * from Categories;
select * from Suppliers;
select * from Products;
select * from Regions;
select * from Stores;
select * from Departments;
select * from Employees;
select * from Warehouses;
select * from Inventory;
select * from Orders;
select * from Order_Details;
select * from Payments;
select * from Delivery_Partners;
select * from Shipments;
select * from Returns;
select * from Marketing_Campaigns;
select * from Coupons;
select * from Loyalty_Program;
select * from Product_Reviews;

end  $$
delimiter ;
call alltable();

-- CALL PROCEDURES 2 :
delimiter $$
create procedure tablecounts()
begin
SELECT 'CUSTOMERS'as "TABLE NAMES", COUNT(*) as "TABLE TOTAL RECORDS" FROM Customers union all
SELECT 'PRODUCTS', COUNT(*) FROM Products union all
SELECT 'CATEGORIES', COUNT(*) FROM Categories union all
SELECT 'SUPPLIERS', COUNT(*) FROM Suppliers union all
SELECT 'INVENTORY', COUNT(*) FROM Inventory union all
SELECT 'STORES', COUNT(*) FROM Stores union all
SELECT 'EMPLOYEES', COUNT(*) FROM Employees union all
SELECT 'ORDERS', COUNT(*) FROM Orders union all
SELECT 'ORDER_DETAILS', COUNT(*) FROM Order_details union all
SELECT 'PAYMENTS', COUNT(*) FROM Payments union all
SELECT 'SHIPMENTS', COUNT(*) FROM Shipments union all
SELECT 'RETURNS', COUNT(*) FROM Returns union all
SELECT 'PRODUCT_REVIEWS', COUNT(*) FROM product_Reviews union all
SELECT 'MARKETING_CAMPAIGNS', COUNT(*) FROM Marketing_Campaigns union all
SELECT 'COUPONS', COUNT(*) FROM coupons union all
SELECT 'REGIONS', COUNT(*) FROM regions union all
SELECT 'WAREHOUSES', COUNT(*) FROM warehouses union all
SELECT 'DELIVERY_PARTNERS', COUNT(*) FROM delivery_partners union all
SELECT 'DEPARTMENTS', COUNT(*) FROM departments union all
SELECT 'LOYALTY_PROGRAM', COUNT(*) FROM loyalty_program;
end $$
delimiter ;
call tablecounts();