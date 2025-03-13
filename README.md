
### Pet Shop Project

This project implements a simple pet shop management system. It includes classes for `Cat` and `Dog`, a `Data` class to interact with a simulated database, unit tests for the `Cat` class, and a script to run and test the functionality.

#### File Structure

```
- Cat.py              # Contains the Cat class
- Dog.py              # Contains the Dog class
- Data.py             # Contains the Data class for database interaction
- petShop.py          # Script to perform pet shop operations
- homework.sql        # SQL file containing database schema and sample insert statements
- test_cat.py         # Unit tests for the Cat class
- README.md           # Project README file
```

#### How to Run

1. Make sure you have Python 3 installed on your system.
2. Ensure all the Python files (`Cat.py`, `Dog.py`, `Data.py`, `petShop.py`, `test_cat.py`) are in the same directory.
3. To run the unit tests, execute the following command in your terminal:

   ```bash
   python3 -m unittest test_cat.py
   ```
4. To run the pet shop script and see the execution results, execute:

   ```bash
   python3 petShop.py
   ```

#### Project Description

The project consists of the following components:

- `Cat` class: Represents a cat with attributes such as name, age, and favorite food. It includes methods to interact with the cat object, such as setting the name, retrieving the age, making the cat speak, and more.
- `Dog` class: Similar to the `Cat` class but represents a dog with similar attributes and methods.
- `Data` class: Simulates a data management system, mainly for database interaction. It includes methods for beginning a transaction, committing a transaction, rolling back a transaction, and inserting data into a simulated database.
- `petShop.py`: A script to perform pet shop operations. It includes functions to save pets to the database, create test cases, and log execution statistics.
- `homework.sql`: Contains SQL statements to create tables for storing `Cat` and `Dog` objects in a simulated database, along with sample insert statements.
- `test_cat.py`: Unit tests for the `Cat` class, ensuring the functionality of the class, including initial age assignment, speaking behavior, name handling, and age incrementing.

#### Approach

- **Object-oriented Design**: The project follows an object-oriented design, with separate classes for `Cat` and `Dog`, encapsulating their attributes and behavior.
- **Modularity**: Each class (`Cat`, `Dog`, `Data`) is defined in its own file, enhancing modularity and maintainability.
- **Unit Testing**: Unit tests are implemented using Python's built-in `unittest` framework to ensure the correctness of the `Cat` class's behavior.
- **Database Interaction**: A simple simulated database interaction is implemented using the `Data` class, enabling insertion of `Cat` and `Dog` objects into the database.

#### Feedback and Future Improvements

- **Database Integration**: Currently, the database interaction is simulated. Integrating with a real database engine such as SQLite, PostgreSQL, or MySQL would enhance the project's functionality.
- **Additional Functionality**: Additional methods and features could be added to the `Cat` and `Dog` classes, such as methods to update and delete pets, search functionality, and more.
- **Enhanced Logging**: Improved logging functionality could be implemented to provide more detailed and structured logs for better debugging and monitoring.
- **Error Handling**: Further error handling could be added, especially in database interactions, to handle exceptions and edge cases more gracefully.
- **Code Documentation**: Although the code is relatively simple, adding more comprehensive comments and docstrings would improve readability and maintainability.
