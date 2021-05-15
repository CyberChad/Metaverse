"""Definition of meta model 'testPackage'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'testPackage'
nsURI = ''
nsPrefix = ''

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
