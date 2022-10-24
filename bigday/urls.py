from wedding.views import home
from django_distill import distill_path

urlpatterns = [
    distill_path('', home, name='home'),
]
