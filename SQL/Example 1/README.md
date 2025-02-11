# User Management Database Scripts

This repository contains SQL scripts designed to demonstrate basic ETL (Extract, Transform, Load) operations and data management tasks using a PostgreSQL database. The scripts showcase skills in creating and managing tables, inserting data, querying and filtering data, performing updates and deletions, and creating views for analysis.

---

## Features

1. **Table Creation**  
   - Creates a `users` table to store user information, including personal details, signup dates, countries, and last login timestamps.

2. **Data Insertion**  
   - Inserts example user data into the `users` table, simulating the initial loading of records.

3. **Data Querying**  
   - Filters users based on specific criteria (e.g., signup dates).
   - Orders results for easy readability.

4. **Data Aggregation**  
   - Groups user data by country and counts the number of users per country.

5. **Data Updates**  
   - Updates a user's `last_login` timestamp to reflect recent activity.

6. **Data Deletion**  
   - Removes a specific user's record from the database.

7. **View Creation**  
   - Defines a view (`active_users`) for users who logged in within the last 30 days, enabling efficient querying of active users.

8. **View Querying**  
   - Retrieves data from the `active_users` view to analyze recent user activity.

---

## Prerequisites

- **PostgreSQL**: Ensure you have PostgreSQL installed on your system.
- **Database Setup**: Set up a database where these scripts can be executed.

---

## Usage Instructions

### 1. Create the Users Table
Run the following script to create the `users` table:

```sql
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    signup_date DATE DEFAULT CURRENT_DATE,
    country VARCHAR(50),
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
