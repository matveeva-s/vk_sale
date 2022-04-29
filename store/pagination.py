from rest_framework.pagination import PageNumberPagination


class ItemsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'paginate_by'
    max_page_size = 20
