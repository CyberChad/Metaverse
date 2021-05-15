
from .testPackage import getEClassifier, eClassifiers
from .testPackage import name, nsURI, nsPrefix, eClass


from . import testPackage
from .. import metamind


__all__ = []

eSubpackages = []
eSuperPackage = metamind
testPackage.eSubpackages = eSubpackages
testPackage.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
