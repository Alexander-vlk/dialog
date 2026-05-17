from rest_framework.pagination import PageNumberPagination

class SecurePagination(PageNumberPagination):
    def get_next_link(self):
        url = super().get_next_link()
        if url:
            return url.replace('http://', 'https://')
        return url

    def get_previous_link(self):
        url = super().get_previous_link()
        if url:
            return url.replace('http://', 'https://')
        return url
