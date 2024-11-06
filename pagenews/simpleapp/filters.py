from django_filters import FilterSet
from .models import P

class PFilter(FilterSet):
    class Meta:
        model = P
        fields = {
            'title_p': ['icontains'],
            'cost_p': [
                'lt',
                'gt',
            ],
        }