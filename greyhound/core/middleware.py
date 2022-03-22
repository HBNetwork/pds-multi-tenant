class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.path_info.startswith('/admin/'):
            index = request.path_info.find('/', 1)

            tenant_name = request.path_info[1:index]
            request.tenant_name = tenant_name

            request.path_info = request.path_info[index:]

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response