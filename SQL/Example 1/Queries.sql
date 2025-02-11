
-- Step 1: Create a Table to Store User Data
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    signup_date DATE DEFAULT CURRENT_DATE,
    country VARCHAR(50),
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 2: Insert Example Data into the Users Table
INSERT INTO users (first_name, last_name, email, country, signup_date)
VALUES 
    ('John', 'Doe', 'john.doe@example.com', 'USA', '2023-01-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', 'Canada', '2023-02-15'),
    ('Carlos', 'Hernandez', 'carlos.h@example.com', 'Mexico', '2023-03-10');

-- Step 3: Query Data - Filter Users Who Signed Up in 2023
SELECT 
    user_id, 
    first_name, 
    last_name, 
    email, 
    country, 
    signup_date
FROM 
    users
WHERE 
    signup_date >= '2023-01-01'
ORDER BY 
    signup_date ASC;

-- Step 4: Aggregate Data - Count Users by Country
SELECT 
    country,
    COUNT(*) AS user_count
FROM 
    users
GROUP BY 
    country
ORDER BY 
    user_count DESC;

-- Step 5: Update a User's Last Login Timestamp
UPDATE users
SET last_login = CURRENT_TIMESTAMP
WHERE email = 'john.doe@example.com';

-- Step 6: Delete a User Record
DELETE FROM users
WHERE email = 'carlos.h@example.com';

-- Step 7: Create a View for Active Users
CREATE VIEW active_users AS
SELECT 
    user_id, 
    first_name, 
    last_name, 
    email, 
    last_login
FROM 
    users
WHERE 
    last_login > CURRENT_DATE - INTERVAL '30 days';

-- Step 8: Query the View
SELECT * FROM active_users;