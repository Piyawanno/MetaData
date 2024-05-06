from typing import get_type_hints
from enum import IntEnum

EXTRACTABLE = {int, float, str}

def extract(klass):
    klass.__meta__ = []
    for name, typed in get_type_hints(klass).items():
        if typed in EXTRACTABLE:
            klass.__meta__.append((name, typed))
    return klass

class PackageType (IntEnum):
    LETTER = 10
    REGULAR = 20
    EXPRESS = 30

@extract
class Package:
    weight: float
    price: float
    sender: str
    receiver: str
    packageType: PackageType

print(Package.__meta__)