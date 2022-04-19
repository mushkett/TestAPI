from rest_framework.serializers import ModelSerializer
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


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class CustomerCustomerDemoSerializer(ModelSerializer):
    class Meta:
        model = CustomerCustomerDemo
        fields = '__all__'


class CustomerDemographicsSerializer(ModelSerializer):
    class Meta:
        model = CustomerDemographics
        fields = '__all__'


class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class EmployeeTerritoriesSerializer(ModelSerializer):
    class Meta:
        model = EmployeeTerritories
        fields = '__all__'


class EmployeesSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class OrderDetailsSerializer(ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = '__all__'


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class ShippersSerializer(ModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__'


class SuppliersSerializer(ModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__'


class TerritoriesSerializer(ModelSerializer):
    class Meta:
        model = Territories
        fields = '__all__'


class UsStatesSerializer(ModelSerializer):
    class Meta:
        model = UsStates
        fields = '__all__'
