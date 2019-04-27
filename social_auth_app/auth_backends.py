from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class CustomBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_class = get_user_model()

        try:
            user = user_class.objects.filter(
                Q(username__iexact=username) | Q(email__iexact=username)
            ).distinct()
        except user_class.DoesNotExist:
            return None

        if user.exists():
            user_obj = user.first()
            if user_obj.check_password(password):
                return user_obj
            return None
        else:
            return None

    def get_user(self, user_id):
        user_class = get_user_model()
        try:
            return user_class.objects.get(pk=user_id)
        except user_class.DoesNotExist:
            return None
