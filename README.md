# Python CRUD Application for 'Employees Data' in the Company

A comprehensive Python application for managing 'Employees Data' in the Company with Create, Read, Update, and Delete (CRUD) operations.

## Business Understanding

This project focused on the process of recruiting new employees in the company, specifically addressing the need to manage employee data efficiently. With this program, a company's Human Resource Development will find it easy to access and update data by processing the identity data of prospective new employees.

**Benefits:**

* Improved data accuracy and consistency
* Streamlined data management processes
* Enhanced decision-making through readily available data
* Make it easier for companies to access data

**Target Users:**

This application is designed for company's Human Resource Development to facilitate their division's work program related to the process of recruiting new employees at the company.

## Features

* **Create:**
    * Add new employees data entries with essential details data identity like NIK, name, age, gender, domicile, and position applied for resource development in the recruitment process of a company.
    * Implement validation rules to ensure data integrity such as checking data types and catching errors in programs.
* **Read:**
    * Search and retrieve specific new employees data records by applying filters based on NIK as primary key.
    * Display comprehensive information for each new employee in a user-friendly format.
* **Update:**
    * Modify existing new employee data to reflect changes in NIK, name, age, gender, domicile and position applied.
    * Provide clear confirmation or error messages based on update success or failure.
* **Delete:**
    * Allow for the removal of unwanted new employees data records with appropriate authorization checks.

## Installation

1. **Prerequisites:**
    * Python version 3.12.5.

2. **Installation:**
    ```bash
    git clone https://github.com/melinayu>/Python-CRUD-Program.git
    cd Python-CRUD-Program
    ```

## Usage

1. **Run the application:**
    ```bash
    python main.py
    ```

2. **CRUD Operations:**
    * **Create:** Add a new employees data record, for example there is a new employee in a particular division, providing details like NIK, name, age, gender, domicile, and position applied.
    * **Read:** Search and retrieve employee information by NIK, name, age, gender, domicile, and position applied.
    * **Update:** Modify existing new employee data details, such as updating their age or position details.
    * **Delete:** Remove a employee record from the system for those who fail to reach the final stage.

## Data Model
This project utilizes a dictionary in list on python to represent new employees data. The following fields are typically stored:
   * NIK: (int) - Primary key in new employees data and to describe the identity of the new employee.
   * Name: (str) -  The name of the new employee.
   * Age: (int) -  The age of the new employee (up to 2 digits and less than 31).
   * Gender: (str) -  The gender of the new employee (male/female).
   * Domicile: (str) -  The current residence address of the new employee.
   * Position: (str) -  Parts of work units within the company that have different duties and responsibilities.

## Contributing
We welcome contributions to this project! Please feel free to open a pull request, sent to melinayusafitri@gmail.com or submit an issue if you encounter any problems or have suggestions for improvements.

