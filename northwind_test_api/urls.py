from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', views.CategoriesList, basename='Categories')
router.register('customer_customer_demo', views.CustomerCustomerDemoList, basename='CustomerCustomerDemo')
router.register('customer_demographics', views.CustomerDemographicsList, basename='CustomerDemographics')
router.register('customers', views.CustomersList, basename='Customers')
router.register('employee_territories', views.EmployeeTerritoriesList, basename='EmployeeTerritories')
router.register('employees', views.EmployeesList, basename='Employees')
router.register('order_details', views.OrderDetailsList, basename='OrderDetails')
router.register('orders', views.OrdersList, basename='Orders')
router.register('products', views.ProductsList, basename='Products')
router.register('region', views.RegionList, basename='Region')
router.register('shippers', views.ShippersList, basename='Shippers')
router.register('suppliers', views.SuppliersList, basename='Suppliers')
router.register('territories', views.TerritoriesList, basename='Territories')
router.register('us_states', views.UsStatesList, basename='UsStates')

urlpatterns = [
    path('', include(router.urls)),
    path('api_overview/', views.api_overview, name='api-overview'),
]
