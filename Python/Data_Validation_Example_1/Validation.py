import datetime

# Sample data to validate (a list of dictionaries simulating records)
data = [
    {"user_id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "signup_date": "2023-01-01", "country": "USA"},
    {"user_id": 2, "first_name": "", "last_name": "Smith", "email": "jane.smith@example.com", "signup_date": "2023-02-15", "country": "Canada"},
    {"user_id": 3, "first_name": "Carlos", "last_name": "Hernandez", "email": "carlos.h@example", "signup_date": "2023-03-10", "country": "Mexico"},
    {"user_id": "four", "first_name": "Anna", "last_name": "Lee", "email": "anna.lee@example.com", "signup_date": "2023-04-01", "country": "USA"},
]

# Validation function
def validate_data(records):
    errors = []
    for idx, record in enumerate(records):
        record_errors = []

        # Check that 'user_id' is an integer
        if not isinstance(record.get("user_id"), int):
            record_errors.append(f"'user_id' must be an integer, got {type(record.get('user_id'))}")

        # Check that 'first_name' is not empty
        if not record.get("first_name"):
            record_errors.append("'first_name' is required and cannot be empty")

        # Check that 'email' is valid
        email = record.get("email")
        if email:
            if "@" not in email or "." not in email.split("@")[-1]:
                record_errors.append(f"'email' is invalid: {email}")
        else:
            record_errors.append("'email' is required and cannot be empty")

        # Check that 'signup_date' is a valid date
        signup_date = record.get("signup_date")
        try:
            datetime.datetime.strptime(signup_date, "%Y-%m-%d")
        except (ValueError, TypeError):
            record_errors.append(f"'signup_date' must be in YYYY-MM-DD format, got: {signup_date}")

        # Collect errors for the record
        if record_errors:
            errors.append({"record_index": idx, "errors": record_errors})

    return errors

# Validate the data
validation_errors = validate_data(data)

# Output the results
if validation_errors:
    print("Validation Errors Found:")
    for error in validation_errors:
        print(f"Record Index {error['record_index']}:")
        for err in error["errors"]:
            print(f"  - {err}")
else:
    print("All records are valid!")
