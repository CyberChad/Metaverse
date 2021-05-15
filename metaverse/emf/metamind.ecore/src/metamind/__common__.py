	class Metamindbase:
		"""
		Metamindbase is the base class of all elements in the metamind module.
		"""
		def __init__(self):
			pass
			self.__internal_resource__ = None
		
		def __eResource__(self):
			pass
	    	
	class Metamindrelationbase(list):
		"""
		Base class for relations
		"""
		pass
		
	class Metamindresource:
		"""
		The Metamindresource is responsible for model serialization.
		"""
		def __init__(self,uri):
			# type here your specific code
			self.__content__ =  []
			self.__uri__ = uri

		def load(self,options=dict()):
			pass
    
		def save(self,options=dict()):
			pass
	
	class Metamindresourcefactory:
		"""
		The Metamindresourcefactory is responsible for creating resource.
		"""
		def __init__(self):
			# type here your specific code
			pass

		def create(self,uri,options=dict()):
			pass
