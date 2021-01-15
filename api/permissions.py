from rest_framework import permissions


class UpdateOwnObjects(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return self.is_own_object(request, obj)


class UpdateOwnProfile(UpdateOwnObjects):
    def is_own_object(self, request, obj):
        return obj.id == request.user.id


class UpdateOwnStatus(UpdateOwnObjects):
    def is_own_object(self, request, obj):
        return obj.user.id == request.user.id
