"""Define custom permissions"""
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin


class IsStaff(UserPassesTestMixin):
    """Define test case"""

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "Only member of staff can create characters")
        return super().handle_no_permission()
