from django.http import HttpResponse

def tenant_home(request):
    return HttpResponse(f'Hello {request.tenant}')