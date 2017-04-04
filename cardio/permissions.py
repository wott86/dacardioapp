from rest_framework import permissions


class isStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff

class isOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user

class isStaffOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_staff