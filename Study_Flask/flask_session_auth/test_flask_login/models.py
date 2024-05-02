from flask_login import UserMixin

"""
The class that you use to represent users needs to implement these properties and methods:

1. is_authenticated
This property should return True if the user is authenticated,
i.e. they have provided valid credentials. (Only authenticated users will fulfill the criteria of login_required.)

2. is_active
This property should return True if this is an active user - in addition to being authenticated,
they also have activated their account, not been suspended,
or any condition your application has for rejecting an account.
Inactive accounts may not log in (without being forced of course).

3. is_anonymous
This property should return True if this is an anonymous user. (Actual users should return False instead.)

4. get_id()
This method must return a str that uniquely identifies this user,
and can be used to load the user from the user_loader callback.
Note that this must be a str - if the ID is natively an int or some other type, you will need to convert it to str.

To make implementing a user class easier, you can inherit from UserMixin, which provides default implementations for all of these properties and methods. (It’s not required, though.)
"""

"""
To make implementing a user class easier, you can inherit from UserMixin, 
which provides default implementations for all of these properties and methods. 
(It’s not required, though.)
"""

users = {
    'admin': {
        'password': 'secret'
    },
    'admin2': {
        'password': 'secret'
    }
}


class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.password = password

    @staticmethod
    def get(user_id):
        user_data = users.get(user_id)
        if user_data:
            return User(user_id, user_data['password'])
        return None
