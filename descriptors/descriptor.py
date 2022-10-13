import sqlalchemy as sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


DESCRIPTOR_KEYS = {"__get__", "__set__", "__delete__"}
# & - intersaction operator for sets

def descriptor_keys(obj):
    return DESCRIPTOR_KEYS & set(dir(obj))

def print_obj_and_descriptor_keys(obj):
    print(obj)
    keys = descriptor_keys(obj)
    if keys:
        print(f"IS a descriptor, found: {keys}")
    else:
        print(f"IS NOT a descriptor, found: {keys}")

class User(Base):
    __tablename__ = "user_account"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)


def sqlalchemy_models():
    print_obj_and_descriptor_keys(User.__dict__["id"])
    print(User.__dict__["id"].__class__)
    print(sqlalchemy.orm.attributes.InstrumentedAttribute)

sqlalchemy_models()