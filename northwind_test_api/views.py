from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (Categories,
                     CustomerCustomerDemo,
                     CustomerDemographics,
                     Customers,
                     EmployeeTerritories,
                     Employees,
                     OrderDetails,
                     Orders,
                     Products,
                     Region,
                     Shippers,
                     Suppliers,
                     Territories,
                     UsStates)

from .serializers import (CategoriesSerializer,
                          CustomerCustomerDemoSerializer,
                          CustomerDemographicsSerializer,
                          CustomersSerializer,
                          EmployeeTerritoriesSerializer,
                          EmployeesSerializer,
                          OrderDetailsSerializer,
                          OrdersSerializer,
                          ProductsSerializer,
                          RegionSerializer,
                          ShippersSerializer,
                          SuppliersSerializer,
                          TerritoriesSerializer,
                          UsStatesSerializer)
# Create your views here.


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Categories': 'categories/',
        'CustomerCustomerDemo': 'customer_customer_demo/',
        'CustomerDemographics': 'customer_demographics/',
        'Customers': 'customers/',
        'EmployeeTerritories': 'employee_territories/',
        'Employees': 'employees/',
        'OrderDetails': 'order_details/',
        'Orders': 'orders/',
        'Products': 'products/',
        'Region': 'region/',
        'Shippers': 'shippers/',
        'Suppliers': 'suppliers/',
        'Territories': 'territories/',
        'UsStates': 'us_states/'
    }
    return Response(api_urls)


class CategoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class CustomerCustomerDemoList(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerCustomerDemo.objects.all()
    serializer_class = CustomerCustomerDemoSerializer


class CustomerDemographicsList(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerDemographics.objects.all()
    serializer_class = CustomerDemographicsSerializer


class CustomersList(viewsets.ReadOnlyModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer


class EmployeeTerritoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeTerritories.objects.all()
    serializer_class = EmployeeTerritoriesSerializer


class EmployeesList(viewsets.ReadOnlyModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class OrderDetailsList(viewsets.ReadOnlyModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class OrdersList(viewsets.ReadOnlyModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ProductsList(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class RegionList(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class ShippersList(viewsets.ReadOnlyModelViewSet):
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer


class SuppliersList(viewsets.ReadOnlyModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer


class TerritoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = Territories.objects.all()
    serializer_class = TerritoriesSerializer


class UsStatesList(viewsets.ReadOnlyModelViewSet):
    queryset = UsStates.objects.all()
    serializer_class = UsStatesSerializer
