from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
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
        'Test Account': {
            'login': 'testuser',
            'password': 'testpassword'
        },
        'Token': {
            'get': "api/token/",
            'verify': 'api/token/verify/',
            'refresh': 'api/token/verify/'

        },
        'params': {
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
    }
    return Response(api_urls)


class CategoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    filterset_fields = ['category_id', 'category_name', 'description']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class CustomerCustomerDemoList(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerCustomerDemo.objects.all()
    serializer_class = CustomerCustomerDemoSerializer
    filterset_fields = ['customer_id', 'customer_type_id']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class CustomerDemographicsList(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerDemographics.objects.all()
    serializer_class = CustomerDemographicsSerializer
    filterset_fields = ['customer_type_id', 'customer_desc']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class CustomersList(viewsets.ReadOnlyModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    filterset_fields = ['customer_id',
                        'company_name',
                        'contact_name',
                        'contact_title',
                        'address',
                        'city',
                        'region',
                        'postal_code',
                        'country',
                        'phone',
                        'fax']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class EmployeeTerritoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = EmployeeTerritories.objects.all()
    serializer_class = EmployeeTerritoriesSerializer
    filterset_fields = ['employee_id', 'territory_id']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class EmployeesList(viewsets.ReadOnlyModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    filterset_fields = ['employee_id',
                        'last_name',
                        'first_name',
                        'title',
                        'title_of_courtesy',
                        'birth_date',
                        'hire_date',
                        'address',
                        'city',
                        'region',
                        'postal_code',
                        'country',
                        'home_phone',
                        'extension',
                        'notes',
                        'reports_to',
                        'photo_path']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class OrderDetailsList(viewsets.ReadOnlyModelViewSet):
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer
    filterset_fields = ['order_id',
                        'product_id',
                        'unit_price',
                        'quantity',
                        'discount']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class OrdersList(viewsets.ReadOnlyModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filterset_fields = ['order_id',
                        'customer_id',
                        'employee_id',
                        'order_date',
                        'required_date',
                        'shipped_date',
                        'ship_via',
                        'freight',
                        'ship_name',
                        'ship_address',
                        'ship_city',
                        'ship_region',
                        'ship_postal_code',
                        'ship_country']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class ProductsList(viewsets.ReadOnlyModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filterset_fields = ['product_id',
                        'product_name',
                        'supplier_id',
                        'category_id',
                        'quantity_per_unit',
                        'unit_price',
                        'units_in_stock',
                        'units_on_order',
                        'reorder_level',
                        'discontinued']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class RegionList(viewsets.ReadOnlyModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filterset_fields = ['region_id',
                        'region_description']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class ShippersList(viewsets.ReadOnlyModelViewSet):
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer
    filterset_fields = ['shipper_id',
                        'company_name',
                        'phone']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class SuppliersList(viewsets.ReadOnlyModelViewSet):
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    filterset_fields = ['supplier_id',
                        'company_name',
                        'contact_name',
                        'contact_title',
                        'address',
                        'city',
                        'region',
                        'postal_code',
                        'phone',
                        'country',
                        'fax',
                        'homepage']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class TerritoriesList(viewsets.ReadOnlyModelViewSet):
    queryset = Territories.objects.all()
    serializer_class = TerritoriesSerializer
    filterset_fields = ['territory_id',
                        'territory_description',
                        'region_id']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)


class UsStatesList(viewsets.ReadOnlyModelViewSet):
    queryset = UsStates.objects.all()
    serializer_class = UsStatesSerializer
    filterset_fields = ['state_id',
                        'state_name',
                        'state_abbr',
                        'state_region']
    ordering_fields = '__all__'
    permission_classes = (IsAuthenticated,)
