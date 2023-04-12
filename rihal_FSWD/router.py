from studentsAPI.viewsets import ClassViewSet, CountryViewSet, StudentViewSet
from rest_framework import routers
# we will use routers to make it easy for us
# to define the URLs for your API, and to map the URLs to the designated viewsets.
router = routers.DefaultRouter()
router.register('class', ClassViewSet)
router.register('country',CountryViewSet)
router.register('student', StudentViewSet)
