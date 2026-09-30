# Python OOP Project: Employee Management System

## Project Overview

This is a simple Employee Management System created using Python Object-Oriented Programming (OOP).

This project demonstrates:

- Classes and Objects
- Constructors
- Inheritance
- Encapsulation
- Method Overriding
- Getters and Setters
- super() method

## Features

The program provides the following options:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

## OOP Concepts Used

### 1. Class

The project uses the Employee class as the main/base class.

### 2. Encapsulation

Employee ID and Salary are private attributes.

```python
self.__employee_id
self.__salary
````

Getter and Setter methods are used to access and modify private data.

### 3. Inheritance

Manager and Developer classes inherit from the Employee class.

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

### 4. Method Overriding

The `display()` method is overridden in the child classes.

```python
def display(self):
    super().display()
    print(self.department)
```

### 5. super() Method

The `super()` method is used to call the parent class constructor and methods.

```python
super().__init__(employee_id, name, age, salary)
```

## Project Structure

```text
Employee-Management-System/
│
├── main.py
├── output.png
└── README.md
```

## How to Run

### Step 1

Open the project folder in Visual Studio Code.

### Step 2

Open the VS Code terminal.

### Step 3

Run the Python program.

```bash
python main.py
```

## Program Menu

```text
--- Python OOP Project: Employee Management System ---

--- Choice another operation ---

Choice An Operation

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter Your Choice:-
```

## Example Output

```text
Employee name is Rahul
Employee age is 25
Employee ID is 101
Employee salary : 30000
```

## Technologies Used

* Python 3
* Visual Studio Code
* Object-Oriented Programming

## Learning Objective

The main objective of this project is to understand and practice Python OOP concepts by creating a simple real-world Employee Management System.

## OutPut

![programe Output](output.png)


## Author

Virendra Nakum

