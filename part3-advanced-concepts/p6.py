#Nested Decorator
def login_required(func):
    def wrapper(*args,**kwards):
        print("Checking Login")
        print("User is logged in")
        return func(*args,**kwards)
    return wrapper

def log_activity(func):
    def wrapper(*args,**kwargs):
        print("Logging activity")
        result = func(*args,**kwargs)
        print("Activity Completed")
        return result
    return wrapper

@login_required
@log_activity
def view_profile():
    print("Display User Profile")

view_profile()