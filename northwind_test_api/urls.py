from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('categories', views.CategoriesList, basename='CategoriesList')
router.register('customer_customer_demo', views.CustomerCustomerDemoList, basename='CustomerCustomerDemoList')
router.register('customer_demographics', views.CustomerDemographicsList, basename='CustomerDemographicsList')
router.register('customers', views.CustomersList, basename='CustomersList')
router.register('employee_territories', views.EmployeeTerritoriesList, basename='EmployeeTerritoriesList')
router.register('employees', views.EmployeesList, basename='EmployeesList')
router.register('order_details', views.OrderDetailsList, basename='OrderDetailsList')
router.register('orders', views.OrdersList, basename='OrdersList')
router.register('products', views.ProductsList, basename='ProductsList')
router.register('region', views.RegionList, basename='RegionList')
router.register('shippers', views.ShippersList, basename='ShippersList')
router.register('suppliers', views.SuppliersList, basename='SuppliersList')
router.register('territories', views.TerritoriesList, basename='TerritoriesList')
router.register('us_states', views.UsStatesList, basename='UsStatesList')

urlpatterns = [
    path('', include(router.urls)),
    path('api_overview/', views.api_overview, name='api-overview'),
]
