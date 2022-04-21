from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import *


# Create your tests here.


class AuthTestWithoutToken(APITestCase):

    def test_Categories(self):
        response = self.client.get(reverse('Categories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_CustomerCustomerDemo(self):
        response = self.client.get(reverse('CustomerCustomerDemo-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_CustomerDemographics(self):
        response = self.client.get(reverse('CustomerDemographics-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Customers(self):
        response = self.client.get(reverse('Customers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_EmployeeTerritories(self):
        response = self.client.get(reverse('EmployeeTerritories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Employees(self):
        response = self.client.get(reverse('Employees-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_OrderDetails(self):
        response = self.client.get(reverse('OrderDetails-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Orders(self):
        response = self.client.get(reverse('Orders-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Products(self):
        response = self.client.get(reverse('Products-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Region(self):
        response = self.client.get(reverse('Region-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Shippers(self):
        response = self.client.get(reverse('Shippers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Suppliers(self):
        response = self.client.get(reverse('Suppliers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_Territories(self):
        response = self.client.get(reverse('Territories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)

    def test_UsStates(self):
        response = self.client.get(reverse('UsStates-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.data), 1)


class AuthTestWithToken(APITestCase):

    def setUp(self):
        self.data = {
            "username": "testuser2",
            "password": "testpassword2"
        }

        # Create a test user
        user = User.objects.create_user(username=self.data['username'],
                                        email='testemail@gmail.com',
                                        password=self.data['password'])
        self.assertEqual(user.is_active, 1, 'Active User')

        # getting token
        response = self.client.post(reverse('token_obtain_pair'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(self.token))

    def test_Categories(self):
        response = self.client.get(reverse('Categories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Categories.objects.count())

    def test_CustomerCustomerDemo(self):
        response = self.client.get(reverse('CustomerCustomerDemo-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), CustomerCustomerDemo.objects.count())

    def test_CustomerDemographics(self):
        response = self.client.get(reverse('CustomerDemographics-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), CustomerDemographics.objects.count())

    def test_Customers(self):
        response = self.client.get(reverse('Customers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Customers.objects.count())

    def test_EmployeeTerritories(self):
        response = self.client.get(reverse('EmployeeTerritories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), EmployeeTerritories.objects.count())

    def test_Employees(self):
        response = self.client.get(reverse('Employees-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Employees.objects.count())

    def test_OrderDetails(self):
        response = self.client.get(reverse('OrderDetails-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), OrderDetails.objects.count())

    def test_Orders(self):
        response = self.client.get(reverse('Orders-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Orders.objects.count())

    def test_Products(self):
        response = self.client.get(reverse('Products-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Products.objects.count())

    def test_Region(self):
        response = self.client.get(reverse('Region-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Region.objects.count())

    def test_Shippers(self):
        response = self.client.get(reverse('Shippers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Shippers.objects.count())

    def test_Suppliers(self):
        response = self.client.get(reverse('Suppliers-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Suppliers.objects.count())

    def test_Territories(self):
        response = self.client.get(reverse('Territories-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Territories.objects.count())

    def test_UsStates(self):
        response = self.client.get(reverse('UsStates-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), UsStates.objects.count())


class FilteringTest(APITestCase):

    def setUp(self):
        self.data = {
            "username": "testuser2",
            "password": "testpassword2"
        }

        # Create a test user
        user = User.objects.create_user(username=self.data['username'],
                                        email='testemail@gmail.com',
                                        password=self.data['password'])
        self.assertEqual(user.is_active, 1, 'Active User')

        # getting token
        response = self.client.post(reverse('token_obtain_pair'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(self.token))

    def test_Categories(self):
        response = self.client.get(reverse('Categories-list') + '?category_id=2', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['category_id'], 2, dict(obj)['category_id'])

        response = self.client.get(reverse('Categories-list') + '?category_name=Confections', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['category_name'], 'Confections')

        response = self.client.get(reverse('Categories-list') + '?description=Cheeses', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['description'], 'Cheeses')

    def test_Customers(self):
        response = self.client.get(reverse('Customers-list') + '?customer_id=ANATR', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['customer_id'], 'ANATR')

        response = self.client.get(reverse('Customers-list') + '?company_name=Around the Horn', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['company_name'], 'Around the Horn')

        response = self.client.get(reverse('Customers-list') + '?contact_title=Sales Associate', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['contact_title'], 'Sales Associate')

        response = self.client.get(reverse('Customers-list') + '?city=Madrid', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['city'], 'Madrid')

        response = self.client.get(reverse('Customers-list') + '?country=France', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['country'], 'France')

    def test_Employees(self):

        response = self.client.get(reverse('Employees-list') + '?employee_id=4', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['employee_id'], 4)

        response = self.client.get(reverse('Employees-list') + '?last_name=Fuller', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['last_name'], 'Fuller')

        response = self.client.get(reverse('Employees-list') + '?first_name=Anne', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['first_name'], 'Anne')

        response = self.client.get(reverse('Employees-list') + '?title=Sales Representative', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['title'], 'Sales Representative')

        response = self.client.get(reverse('Employees-list') + '?country=USA', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['country'], 'USA')

    def test_OrderDetails(self):

        response = self.client.get(reverse('OrderDetails-list') + '?order=11077', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for obj in response.data:
            self.assertEqual(dict(obj)['order'], 11077)

        response = self.client.get(reverse('OrderDetails-list') + '?product=51', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['product'], 51)

        response = self.client.get(reverse('OrderDetails-list') + '?unit_price=10', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['unit_price'], 10)

        response = self.client.get(reverse('OrderDetails-list') + '?quantity=20', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['quantity'], 20)

    def test_Orders(self):
        response = self.client.get(reverse('Orders-list') + '?order_id=10258', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['order_id'], 10258)

        response = self.client.get(reverse('Orders-list') + '?customer=CENTC', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['customer'], 'CENTC')

        response = self.client.get(reverse('Orders-list') + '?employee=9', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['employee'], 9)

        response = self.client.get(reverse('Orders-list') + '?ship_via=3', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['ship_via'], 3)

        response = self.client.get(reverse('Orders-list') + '?ship_city=Bern', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['ship_city'], 'Bern')

        response = self.client.get(reverse('Orders-list') + '?ship_country=Mexico', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['ship_country'], 'Mexico')

    def test_Products(self):

        response = self.client.get(reverse('Products-list') + '?product_id=15', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['product_id'], 15)

        response = self.client.get(reverse('Products-list') + '?product_name=Tofu', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['product_name'], 'Tofu')

        response = self.client.get(reverse('Products-list') + '?supplier=8', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['supplier'], 8)

        response = self.client.get(reverse('Products-list') + '?category=3', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['category'], 3)

        response = self.client.get(reverse('Products-list') + '?units_in_stock=86', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['units_in_stock'], 86)

    def test_Suppliers(self):

        response = self.client.get(reverse('Suppliers-list') + '?supplier_id=10', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['supplier_id'], 10)

        response = self.client.get(reverse('Suppliers-list') + '?company_name=Pavlova, Ltd.', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['company_name'], 'Pavlova, Ltd.')

        response = self.client.get(reverse('Suppliers-list') + '?contact_name=Cheryl Saylor', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['contact_name'], 'Cheryl Saylor')

        response = self.client.get(reverse('Suppliers-list') + '?city=Zaandam', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['city'], 'Zaandam')

        response = self.client.get(reverse('Suppliers-list') + '?country=Australia', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for obj in response.data:
            self.assertEqual(dict(obj)['country'], 'Australia')


class SortingTest(APITestCase):
    def setUp(self):
        self.data = {
            "username": "testuser2",
            "password": "testpassword2"
        }

        # Create a test user
        user = User.objects.create_user(username=self.data['username'],
                                        email='testemail@gmail.com',
                                        password=self.data['password'])
        self.assertEqual(user.is_active, 1, 'Active User')

        # getting token
        response = self.client.post(reverse('token_obtain_pair'), self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        self.token = response.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(self.token))

    def test_Categories(self):

        list_of_fields = [field.name for field in Categories._meta.fields]
        for field in list_of_fields:
            if field == 'description':
                continue
            response = self.client.get(reverse('Categories-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = sorted(list_of_categories_values)
            self.assertEqual(list_of_categories_values, sorted_list_of_categories_values)

    def test_OrderDetails(self):
        list_of_fields = [field.name for field in OrderDetails._meta.fields]

        for field in list_of_fields:
            response = self.client.get(reverse('OrderDetails-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = sorted(list_of_categories_values)
            self.assertEqual(list_of_categories_values, sorted_list_of_categories_values)

    def test_Orders(self):
        list_of_fields = [field.name for field in Orders._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('Orders-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(Orders.objects.all().order_by(field).values_list(field, flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)

    def test_Products(self):
        list_of_fields = [field.name for field in Products._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('Products-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(Products.objects.all().order_by(field).values_list(field,
                                                                                                       flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)

    def test_Shippers(self):
        list_of_fields = [field.name for field in Shippers._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('Shippers-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(Shippers.objects.all().order_by(field).values_list(field,
                                                                                                       flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)

    def test_Suppliers(self):
        list_of_fields = [field.name for field in Suppliers._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('Suppliers-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(Suppliers.objects.all().order_by(field).values_list(field,
                                                                                                        flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)

    def test_Territories(self):
        list_of_fields = [field.name for field in Territories._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('Territories-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(Territories.objects.all().order_by(field).values_list(field,
                                                                                                          flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)

    def test_UsStates(self):
        list_of_fields = [field.name for field in UsStates._meta.fields]

        for field in list_of_fields:

            response = self.client.get(reverse('UsStates-list') + '?ordering={0}'.format(field), format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            list_of_categories_values = []
            for obj in response.data:
                list_of_categories_values.append(dict(obj)[field])
            sorted_list_of_categories_values = list(UsStates.objects.all().order_by(field).values_list(field,
                                                                                                          flat=True))
            self.assertEqual(sorted_list_of_categories_values, sorted_list_of_categories_values)
