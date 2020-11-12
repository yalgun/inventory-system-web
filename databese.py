from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, null
from sqlalchemy.orm import relationship

from app import db


class ProductModel(db.Model):
    __tablename__ = 'product'

    m_syscode = db.Column(db.Integer, primary_key=True)
    m_code = db.Column(db.String(15))
    m_name = db.Column(db.String(25))
    m_short_name = db.Column(db.String(10))
    m_parent_code = db.Column(db.String(15))
    m_abstract = db.Column(db.Integer)
    m_category = db.Column(db.String(12))
    is_active = db.Column(db.Integer)

    def __init__(self, m_code, m_name, m_short_name, m_parent_code, m_abstract, m_category, is_active):
        self.m_code = m_code
        self.m_name = m_name
        self.m_short_name = m_short_name
        self.m_parent_code = m_parent_code
        self.m_abstract = m_abstract
        self.m_category = m_category
        self.is_active = is_active


class FeaturesModel(db.Model):
    __tablename__ = 'features'

    feature_id = db.Column(db.Integer, primary_key=True)
    feature_name = db.Column(db.String(200))

    def __init__(self, feature_name):
        self.feature_name = feature_name


class UserModel(db.Model):
    __tablename__ = 'user'

    person_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(200))
    person_password = db.Column(db.String(200))

    def __init__(self, person_name, person_password):
        self.person_name = person_name
        self.person_password = person_password


class ProductFeaturesModel(db.Model):
    __tablename__ = 'product-features-model'

    m_syscode = db.Column(db.Integer, primary_key=True)
    feature_id = db.Column(db.Integer, ForeignKey('features.feature_id'), primary_key=True)
    minval = db.Column(db.Float)

    def __init__(self, m_syscode, feature_id, minval):
        self.m_syscode = m_syscode
        self.feature_id = feature_id
        self.minval = minval


class ManufacturersModel(db.Model):
    __tablename_ = 'manufacturer'

    manufacturer_id = db.Column(db.Integer, primary_key=True)
    manufacturer_name = db.Column(db.String(200))
    manufacturer_address = db.Column(db.String(200))
    city = db.Column(db.Integer, ForeignKey('country-city.city_id'))
    country = db.Column(db.String(2), ForeignKey('country.country_code'))

    def __init__(self, manufacturer_id, manufacturer_name, manufacturer_address, city, country):
        self.manufacturer_id = manufacturer_id
        self.manufacturer_name = manufacturer_name
        self.manufacturer_address = manufacturer_address
        self.city = city
        self.country = country


class ProductBrandsModel(db.Model):
    __tablename__ = 'product-brands-model'

    brand_barcode = db.Column(db.String(13), primary_key=True)
    m_syscode = db.Column(db.Integer, ForeignKey('product.m_syscode'), primary_key=True)
    manufacturer_id = db.Column(db.Integer)
    brand_name = db.Column(db.String(100))

    def __init__(self, brand_barcode, m_syscode, brand_name, manufacturer_id):
        self.brand_barcode = brand_barcode
        self.m_syscode = m_syscode
        self.brand_name = brand_name
        self.manufacturer_id = manufacturer_id


class OrganizationsModel(db.Model):
    __tablename__ = 'organizations'

    org_id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String())
    parent_org = db.Column(db.Integer)
    org_abstract = db.Column(db.Integer)
    org_Address = db.Column(db.String(200))
    org_City = db.Column(db.Integer)
    org_District = db.Column(db.String(50))
    org_Type = db.Column(db.Integer)

    def __init__(self, org_name, parent_org, org_abstract, org_Address, org_City, org_District, org_Type):
        self.org_name = org_name
        self.parent_org = parent_org
        self.org_abstract = org_abstract
        self.org_Address = org_Address
        self.org_City = org_City
        self.org_District = org_District
        self.org_Type = org_Type





    def __init__(self, org_name, parent_org, org_abstract, org_Address, org_City, org_District, org_Type):
        self.org_name = org_name
        self.parent_org = parent_org
        self.org_abstract = org_abstract
        self.org_Address = org_Address
        self.org_City = org_City
        self.org_District = org_District
        self.org_Type = org_Type

class BrandsOrgsModel(db.Model):
    __tablename_ = 'brands'

    lot_id = db.Column(db.Integer, primary_key=True)
    org_id = db.Column(db.Integer, ForeignKey('organizations.org_id'), primary_key=True)
    brand_barcode = db.Column(db.String(13), primary_key=True)  # Bunu da ekleyemedim !!!!!!!!!!!!!
    in_amount = db.Column(db.Integer)
    out_amount = db.Column(db.Integer)
    total_amount = db.Column(db.Integer)

    def __init__(self, lot_id, org_id, brand_barcode, in_amount, out_amount, total_amount):
        self.lot_id = lot_id
        self.org_id = org_id
        self.brand_barcode = brand_barcode
        self.in_amount = in_amount
        self.out_amount = out_amount
        self.total_amount = total_amount


class FlowModel(db.Model):
    __tablename__ = 'flow'

    source_lot_id = db.Column(db.Integer, primary_key=True)
    source_org_id = db.Column(db.Integer, primary_key=True)
    target_lot_id = db.Column(db.Integer, primary_key=True)
    target_org_id = db.Column(db.Integer, primary_key=True)
    brand_brandcode = db.Column(db.Integer, primary_key=True)  # Brand barcodları ekleyemiyorum !!!!!!!!!!!!!!!!!!!!

    def __init__(self, source_lot_id, source_org_id, target_lot_id, target_org_id, brand_brandcode):
        self.source_lot_id = source_lot_id
        self.source_org_id = source_org_id
        self.target_lot_id = target_lot_id
        self.target_org_id = target_org_id
        self.brand_brandcode = brand_brandcode


class AlternativeBrandsModel(db.Model):
    __tablename__ = 'alternative-brands'

    brand_barcode = db.Column(db.Integer, primary_key=True)
    alternative_brand_code = db.Column(db.Integer, primary_key=True)

    def __init__(self, brand_barcode, alternative_brand_code):
        self.brand_barcode = brand_barcode
        self.alternative_brand_code = alternative_brand_code


class CountryModel(db.Model):
    __tablename__ = 'country'

    country_code = db.Column(db.String(3), primary_key=True)
    country_name = db.Column(db.String(50))

    def __init__(self, country_code, country_name):
        self.country_code = country_code
        self.country_name = country_name


class CountryCityModel(db.Model):
    __tablename__ = 'country-city'

    city_id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100))

    def __init__(self, city_id, city_name):
        self.city_id = city_id
        self.city_name = city_name


db.create_all()
db.session.commit()
