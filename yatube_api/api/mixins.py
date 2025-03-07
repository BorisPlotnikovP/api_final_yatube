from rest_framework.viewsets import mixins, GenericViewSet, ModelViewSet

from .permissions import AuthorOrReadOnly, ReadOnly


# Кастомные вьюсеты с необходимыми действиями.
class ListCreateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                        GenericViewSet):
    pass


class ListRetrieveViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                          GenericViewSet):
    pass


# Класс для наследования базовой настройки прав доступа.
class DefaultPermissionMixin(ModelViewSet):
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()
