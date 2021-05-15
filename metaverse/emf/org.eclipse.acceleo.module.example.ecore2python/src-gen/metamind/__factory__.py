	from metamind import Model
	from metamind import Buffer
	from metamind import Motor
	from metamind import Visual
	from metamind import Rule
	from metamind import Chunk
	from metamind import Condition
	from metamind import Environment
	from metamind import Action
	from metamind import Slot
		class Metamindfactory:  
			""" Factory to create elements from metamind
			"""  
	
		def create(self,name):
			""" generic method to create elements.
			This method is able to create:
			Model
			Buffer
			Motor
			Visual
			Rule
			Chunk
			Condition
			Environment
			Action
			Slot
	
			"""
			f = getattr(self,"create%s" % name)
			return f()
	    
		def createModel(self):
			"""
			Create an instance of Model.
			"""
			instance = Model()
			# type here special initialization code
			return instance
		def createBuffer(self):
			"""
			Create an instance of Buffer.
			"""
			instance = Buffer()
			# type here special initialization code
			return instance
		def createMotor(self):
			"""
			Create an instance of Motor.
			"""
			instance = Motor()
			# type here special initialization code
			return instance
		def createVisual(self):
			"""
			Create an instance of Visual.
			"""
			instance = Visual()
			# type here special initialization code
			return instance
		def createRule(self):
			"""
			Create an instance of Rule.
			"""
			instance = Rule()
			# type here special initialization code
			return instance
		def createChunk(self):
			"""
			Create an instance of Chunk.
			"""
			instance = Chunk()
			# type here special initialization code
			return instance
		def createCondition(self):
			"""
			Create an instance of Condition.
			"""
			instance = Condition()
			# type here special initialization code
			return instance
		def createEnvironment(self):
			"""
			Create an instance of Environment.
			"""
			instance = Environment()
			# type here special initialization code
			return instance
		def createAction(self):
			"""
			Create an instance of Action.
			"""
			instance = Action()
			# type here special initialization code
			return instance
		def createSlot(self):
			"""
			Create an instance of Slot.
			"""
			instance = Slot()
			# type here special initialization code
			return instance
	
		import unittest
	
		class Test_metamind_factory(unittest.TestCase):  
		def testModelCreation(self):
			"""
			Test the direct instanciation of a Model.
			"""
			d = Model()
			self.assertTrue(d!=None)
	
		def testModelCreationFactory(self):
			"""
			Test the instanciation of a Model through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Model")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Model))
		def testBufferCreation(self):
			"""
			Test the direct instanciation of a Buffer.
			"""
			d = Buffer()
			self.assertTrue(d!=None)
	
		def testBufferCreationFactory(self):
			"""
			Test the instanciation of a Buffer through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Buffer")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Buffer))
		def testMotorCreation(self):
			"""
			Test the direct instanciation of a Motor.
			"""
			d = Motor()
			self.assertTrue(d!=None)
	
		def testMotorCreationFactory(self):
			"""
			Test the instanciation of a Motor through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Motor")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Motor))
		def testVisualCreation(self):
			"""
			Test the direct instanciation of a Visual.
			"""
			d = Visual()
			self.assertTrue(d!=None)
	
		def testVisualCreationFactory(self):
			"""
			Test the instanciation of a Visual through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Visual")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Visual))
		def testRuleCreation(self):
			"""
			Test the direct instanciation of a Rule.
			"""
			d = Rule()
			self.assertTrue(d!=None)
	
		def testRuleCreationFactory(self):
			"""
			Test the instanciation of a Rule through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Rule")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Rule))
		def testChunkCreation(self):
			"""
			Test the direct instanciation of a Chunk.
			"""
			d = Chunk()
			self.assertTrue(d!=None)
	
		def testChunkCreationFactory(self):
			"""
			Test the instanciation of a Chunk through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Chunk")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Chunk))
		def testConditionCreation(self):
			"""
			Test the direct instanciation of a Condition.
			"""
			d = Condition()
			self.assertTrue(d!=None)
	
		def testConditionCreationFactory(self):
			"""
			Test the instanciation of a Condition through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Condition")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Condition))
		def testEnvironmentCreation(self):
			"""
			Test the direct instanciation of a Environment.
			"""
			d = Environment()
			self.assertTrue(d!=None)
	
		def testEnvironmentCreationFactory(self):
			"""
			Test the instanciation of a Environment through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Environment")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Environment))
		def testActionCreation(self):
			"""
			Test the direct instanciation of a Action.
			"""
			d = Action()
			self.assertTrue(d!=None)
	
		def testActionCreationFactory(self):
			"""
			Test the instanciation of a Action through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Action")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Action))
		def testSlotCreation(self):
			"""
			Test the direct instanciation of a Slot.
			"""
			d = Slot()
			self.assertTrue(d!=None)
	
		def testSlotCreationFactory(self):
			"""
			Test the instanciation of a Slot through the factory.
			"""
			factory = Metamindfactory()
			d = factory.create("Slot")
			self.assertTrue(d != None)
			self.assertTrue(isinstance(d, Slot))
	
		if __name__ == '__main__':
			unittest.main()
