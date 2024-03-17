from django.core.exceptions import ValidationError

from rest_framework import permissions


class VendorPermission(permissions.BasePermission):
    """"""
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 1 and request.method in permissions.SAFE_METHODS:
            return True
        else:
            raise ValidationError("Not a Vendor!")


class CustomerPermission(permissions.BasePermission):
    """"""
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 2 and request.method in permissions.SAFE_METHODS:
            return True
        else:
            raise ValidationError("Not a Vendor!")
