from django.contrib.auth.models import User


def create_user(email, firstName, password):
    user = User.objects.create(username=email, email=email, first_name=firstName)
    user.set_password(password)
    user.save()
    return user
