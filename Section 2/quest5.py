class AccountLockedError(Exception):   
    pass

class LoginSystem:
    def __init__(self):
        self.__password = 'python@123'
        self.__attempts = 3

    def login(self, password):
        try:
            if password != self.__password:
                self.__attempts -= 1
                print(f"Wrong password! Remaining attempts: {self.__attempts}")
                
                if self.__attempts == 0:
                    raise AccountLockedError("Account is locked due to too many failed attempts.")
            else:
                print("Login successful!")
                
        except AccountLockedError as e:
            print(f"Error: {e}")
            
        finally:
            print("Login process execution completed.")

# Example
system = LoginSystem()

print("Attempt 1")
system.login("wrong1")

print("\nAttempt 2")
system.login("wrong2")

print("\nAttempt 3")
system.login("wrong3")