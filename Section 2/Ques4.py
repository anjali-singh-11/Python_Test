class UnderAgeError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class ageVerification:
    def set_age(self, age):
        try:
            if age < 0:
                raise ValueError("Age cannot be negative")
            elif age < 18:
                raise UnderAgeError("Access Denied: age must be atleast 18")
            elif age > 100:
                raise InvalidAgeError("Access Denied:age exceeds the valid maximum of 100")
            else:
                print('Valid age!')
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except UnderAgeError as uae:
            print(f"UnderAgeError: {uae}")
        except InvalidAgeError as iae:
            print(f"InvalidAgeError: {iae}")
        finally:
            print("Execution of set_age() completed.")