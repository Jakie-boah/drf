import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory(name='test_cat')
        print(x)
        assert x.name == 'test_cat'


class TestBrandModel:
    def test_str_method(self, brand_factory):
        x = brand_factory(name='test_brand')
        assert x.name == 'test_brand'


class TestProductModel:
    def test_str_method(self, product_factory):
        x = product_factory(name='test_product')
        assert x.name == 'test_product'
        assert x.description == 'test description'
        assert x.is_digital == True
        assert 'Category' in x.category.name
        assert 'Brand' in x.brand.name


class TestProductLineModel:
    def test_str_method(self, product_line_factory):
        obj = product_line_factory(sku='1234')
        assert obj.__str__() == '1234'

    def test_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)

        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()
