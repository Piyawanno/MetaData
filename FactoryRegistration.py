from enum import IntEnum

class PackageType (IntEnum):
    LETTER = 10
    REGULAR = 20
    EXPRESS = 30

class Package:
    packageTypeMap = {}
    type: PackageType

    @staticmethod
    def create(type) :
        klass = Package.packageTypeMap.get(type, None)
        klass.type = type
        if klass is not None:
            return klass()
        else:
            return None

def registerPackage(type):
    def register(klass):
        Package.packageTypeMap[type] = klass
    return register

@registerPackage(PackageType.LETTER)
class Letter(Package) :
    pass

@registerPackage(PackageType.REGULAR)
class RegularPackage(Package) :
    pass

@registerPackage(PackageType.EXPRESS)
class ExpressPackage(Package) :
    pass

p1 = Package.create(PackageType.EXPRESS)
print(p1, p1.type)