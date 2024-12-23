import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        x = category_factory(name='test_cat')
        print(x)
        assert x.name == 'test_cat'


class TestBrandModel:
    def test_str_method(self, brand_factory):
        x = brand_factory(name='test_brand')
        assert x.__str__() == 'test_brand'


class TestProductModel:
    def test_str_method(self, product_factory):
        x = product_factory(name='test_product')
        assert x.__str__() == 'test_product'
        assert x.description == 'test description'
        assert x.is_digital == True
        assert 'Category' in x.category.name
        assert x.brand.__str__() == 'test_brand'
