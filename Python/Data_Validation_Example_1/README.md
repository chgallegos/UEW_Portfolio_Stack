# Python Data Validation Example

This repository contains a Python script that demonstrates basic data validation techniques. The example is particularly useful for ETL processes where incoming data needs to be validated before being loaded into a database or further processed.

---

## Features

1. **Sample Dataset**  
   - Simulates a dataset with user records.
   - Each record contains fields like `user_id`, `first_name`, `last_name`, `email`, `signup_date`, and `country`.

2. **Validation Checks**  
   - Ensures that `user_id` is an integer.
   - Verifies that `first_name` is not empty.
   - Checks that `email` has a valid structure.
   - Validates that `signup_date` is in the format `YYYY-MM-DD`.

3. **Error Reporting**  
   - Collects and reports errors for each invalid record.
   - Provides detailed messages for quick debugging.

---

## Prerequisites

- Python 3.6 or higher installed on your system.

---

## Usage Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
