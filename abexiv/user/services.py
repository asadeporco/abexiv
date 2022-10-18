from user.models import User


class UserService:
    def __init__(self):
        pass

    def insert(self, user, request_params):
        user.username = request_params.get("username")
        user.first_name = request_params.get("first_name")
        user.last_name = request_params.get("last_name")
        user.save()


