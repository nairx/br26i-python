from user import User 


def test_greet():
    user = User("John")
    assert user.greet() == "Hello John"