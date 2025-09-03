from rest_framework.pagination import LimitOffsetPagination


class OptionalLimitOffsetPagination(LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get(self.limit_query_param) is None:
            return None
        return super().paginate_queryset(queryset, request, view)
