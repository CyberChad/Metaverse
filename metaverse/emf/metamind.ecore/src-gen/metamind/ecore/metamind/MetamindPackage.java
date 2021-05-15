/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.ecore.EAttribute;
import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EOperation;
import org.eclipse.emf.ecore.EPackage;
import org.eclipse.emf.ecore.EReference;

/**
 * <!-- begin-user-doc -->
 * The <b>Package</b> for the model.
 * It contains accessors for the meta objects to represent
 * <ul>
 *   <li>each class,</li>
 *   <li>each feature of each class,</li>
 *   <li>each operation of each class,</li>
 *   <li>each enum,</li>
 *   <li>and each data type</li>
 * </ul>
 * <!-- end-user-doc -->
 * @see metamind.ecore.metamind.MetamindFactory
 * @model kind="package"
 * @generated
 */
public interface MetamindPackage extends EPackage {
	/**
	 * The package name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNAME = "metamind";

	/**
	 * The package namespace URI.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_URI = "http://www.chadpeters.net/metamind";

	/**
	 * The package namespace name.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	String eNS_PREFIX = "metamind";

	/**
	 * The singleton instance of the package.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	MetamindPackage eINSTANCE = metamind.ecore.metamind.impl.MetamindPackageImpl.init();

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ModelImpl <em>Model</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ModelImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getModel()
	 * @generated
	 */
	int MODEL = 0;

	/**
	 * The feature id for the '<em><b>Modules</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODEL__MODULES = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODEL__NAME = 1;

	/**
	 * The feature id for the '<em><b>Environment</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODEL__ENVIRONMENT = 2;

	/**
	 * The number of structural features of the '<em>Model</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODEL_FEATURE_COUNT = 3;

	/**
	 * The number of operations of the '<em>Model</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODEL_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ModuleImpl <em>Module</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ModuleImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getModule()
	 * @generated
	 */
	int MODULE = 1;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODULE__NAME = 0;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODULE__BUFFER = 1;

	/**
	 * The number of structural features of the '<em>Module</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODULE_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Module</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MODULE_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.BufferImpl <em>Buffer</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.BufferImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getBuffer()
	 * @generated
	 */
	int BUFFER = 2;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int BUFFER__NAME = 0;

	/**
	 * The feature id for the '<em><b>Bufferchunk</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int BUFFER__BUFFERCHUNK = 1;

	/**
	 * The number of structural features of the '<em>Buffer</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int BUFFER_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Buffer</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int BUFFER_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.DeclarativeMemoryImpl <em>Declarative Memory</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.DeclarativeMemoryImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getDeclarativeMemory()
	 * @generated
	 */
	int DECLARATIVE_MEMORY = 3;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY__NAME = MODULE__NAME;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY__BUFFER = MODULE__BUFFER;

	/**
	 * The feature id for the '<em><b>Dmchunks</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY__DMCHUNKS = MODULE_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>Declarative Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY_FEATURE_COUNT = MODULE_FEATURE_COUNT + 1;

	/**
	 * The operation id for the '<em>Request</em>' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY___REQUEST = MODULE_OPERATION_COUNT + 0;

	/**
	 * The number of operations of the '<em>Declarative Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int DECLARATIVE_MEMORY_OPERATION_COUNT = MODULE_OPERATION_COUNT + 1;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ProceduralMemoryImpl <em>Procedural Memory</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ProceduralMemoryImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getProceduralMemory()
	 * @generated
	 */
	int PROCEDURAL_MEMORY = 4;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCEDURAL_MEMORY__NAME = MODULE__NAME;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCEDURAL_MEMORY__BUFFER = MODULE__BUFFER;

	/**
	 * The feature id for the '<em><b>Rules</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCEDURAL_MEMORY__RULES = MODULE_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>Procedural Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCEDURAL_MEMORY_FEATURE_COUNT = MODULE_FEATURE_COUNT + 1;

	/**
	 * The number of operations of the '<em>Procedural Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int PROCEDURAL_MEMORY_OPERATION_COUNT = MODULE_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.MotorImpl <em>Motor</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.MotorImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getMotor()
	 * @generated
	 */
	int MOTOR = 5;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MOTOR__NAME = MODULE__NAME;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MOTOR__BUFFER = MODULE__BUFFER;

	/**
	 * The number of structural features of the '<em>Motor</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MOTOR_FEATURE_COUNT = MODULE_FEATURE_COUNT + 0;

	/**
	 * The number of operations of the '<em>Motor</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int MOTOR_OPERATION_COUNT = MODULE_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.VisualImpl <em>Visual</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.VisualImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getVisual()
	 * @generated
	 */
	int VISUAL = 6;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VISUAL__NAME = MODULE__NAME;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VISUAL__BUFFER = MODULE__BUFFER;

	/**
	 * The number of structural features of the '<em>Visual</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VISUAL_FEATURE_COUNT = MODULE_FEATURE_COUNT + 0;

	/**
	 * The number of operations of the '<em>Visual</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int VISUAL_OPERATION_COUNT = MODULE_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.RuleImpl <em>Rule</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.RuleImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getRule()
	 * @generated
	 */
	int RULE = 7;

	/**
	 * The feature id for the '<em><b>Conditions</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RULE__CONDITIONS = 0;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RULE__NAME = 1;

	/**
	 * The feature id for the '<em><b>Actions</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RULE__ACTIONS = 2;

	/**
	 * The number of structural features of the '<em>Rule</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RULE_FEATURE_COUNT = 3;

	/**
	 * The number of operations of the '<em>Rule</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int RULE_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ChunkImpl <em>Chunk</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ChunkImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getChunk()
	 * @generated
	 */
	int CHUNK = 8;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CHUNK__NAME = 0;

	/**
	 * The feature id for the '<em><b>Slot</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CHUNK__SLOT = 1;

	/**
	 * The number of structural features of the '<em>Chunk</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CHUNK_FEATURE_COUNT = 2;

	/**
	 * The number of operations of the '<em>Chunk</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CHUNK_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ConditionImpl <em>Condition</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ConditionImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getCondition()
	 * @generated
	 */
	int CONDITION = 9;

	/**
	 * The feature id for the '<em><b>LH Sbuffers</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CONDITION__LH_SBUFFERS = 0;

	/**
	 * The number of structural features of the '<em>Condition</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CONDITION_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Condition</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int CONDITION_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.EnvironmentImpl <em>Environment</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.EnvironmentImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getEnvironment()
	 * @generated
	 */
	int ENVIRONMENT = 10;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ENVIRONMENT__NAME = 0;

	/**
	 * The number of structural features of the '<em>Environment</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ENVIRONMENT_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Environment</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ENVIRONMENT_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.ActionImpl <em>Action</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.ActionImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getAction()
	 * @generated
	 */
	int ACTION = 11;

	/**
	 * The feature id for the '<em><b>RH Sbuffers</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ACTION__RH_SBUFFERS = 0;

	/**
	 * The number of structural features of the '<em>Action</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ACTION_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Action</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int ACTION_OPERATION_COUNT = 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.WorkingMemoryImpl <em>Working Memory</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.WorkingMemoryImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getWorkingMemory()
	 * @generated
	 */
	int WORKING_MEMORY = 12;

	/**
	 * The feature id for the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORKING_MEMORY__NAME = MODULE__NAME;

	/**
	 * The feature id for the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORKING_MEMORY__BUFFER = MODULE__BUFFER;

	/**
	 * The feature id for the '<em><b>Wmchunks</b></em>' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORKING_MEMORY__WMCHUNKS = MODULE_FEATURE_COUNT + 0;

	/**
	 * The number of structural features of the '<em>Working Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORKING_MEMORY_FEATURE_COUNT = MODULE_FEATURE_COUNT + 1;

	/**
	 * The number of operations of the '<em>Working Memory</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int WORKING_MEMORY_OPERATION_COUNT = MODULE_OPERATION_COUNT + 0;

	/**
	 * The meta object id for the '{@link metamind.ecore.metamind.impl.SlotImpl <em>Slot</em>}' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see metamind.ecore.metamind.impl.SlotImpl
	 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getSlot()
	 * @generated
	 */
	int SLOT = 13;

	/**
	 * The feature id for the '<em><b>Value</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int SLOT__VALUE = 0;

	/**
	 * The number of structural features of the '<em>Slot</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int SLOT_FEATURE_COUNT = 1;

	/**
	 * The number of operations of the '<em>Slot</em>' class.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 * @ordered
	 */
	int SLOT_OPERATION_COUNT = 0;

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Model <em>Model</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Model</em>'.
	 * @see metamind.ecore.metamind.Model
	 * @generated
	 */
	EClass getModel();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.Model#getModules <em>Modules</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Modules</em>'.
	 * @see metamind.ecore.metamind.Model#getModules()
	 * @see #getModel()
	 * @generated
	 */
	EReference getModel_Modules();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Model#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Model#getName()
	 * @see #getModel()
	 * @generated
	 */
	EAttribute getModel_Name();

	/**
	 * Returns the meta object for the containment reference '{@link metamind.ecore.metamind.Model#getEnvironment <em>Environment</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference '<em>Environment</em>'.
	 * @see metamind.ecore.metamind.Model#getEnvironment()
	 * @see #getModel()
	 * @generated
	 */
	EReference getModel_Environment();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Module <em>Module</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Module</em>'.
	 * @see metamind.ecore.metamind.Module
	 * @generated
	 */
	EClass getModule();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Module#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Module#getName()
	 * @see #getModule()
	 * @generated
	 */
	EAttribute getModule_Name();

	/**
	 * Returns the meta object for the containment reference '{@link metamind.ecore.metamind.Module#getBuffer <em>Buffer</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference '<em>Buffer</em>'.
	 * @see metamind.ecore.metamind.Module#getBuffer()
	 * @see #getModule()
	 * @generated
	 */
	EReference getModule_Buffer();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Buffer <em>Buffer</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Buffer</em>'.
	 * @see metamind.ecore.metamind.Buffer
	 * @generated
	 */
	EClass getBuffer();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Buffer#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Buffer#getName()
	 * @see #getBuffer()
	 * @generated
	 */
	EAttribute getBuffer_Name();

	/**
	 * Returns the meta object for the containment reference '{@link metamind.ecore.metamind.Buffer#getBufferchunk <em>Bufferchunk</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference '<em>Bufferchunk</em>'.
	 * @see metamind.ecore.metamind.Buffer#getBufferchunk()
	 * @see #getBuffer()
	 * @generated
	 */
	EReference getBuffer_Bufferchunk();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.DeclarativeMemory <em>Declarative Memory</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Declarative Memory</em>'.
	 * @see metamind.ecore.metamind.DeclarativeMemory
	 * @generated
	 */
	EClass getDeclarativeMemory();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.DeclarativeMemory#getDmchunks <em>Dmchunks</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Dmchunks</em>'.
	 * @see metamind.ecore.metamind.DeclarativeMemory#getDmchunks()
	 * @see #getDeclarativeMemory()
	 * @generated
	 */
	EReference getDeclarativeMemory_Dmchunks();

	/**
	 * Returns the meta object for the '{@link metamind.ecore.metamind.DeclarativeMemory#request() <em>Request</em>}' operation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the '<em>Request</em>' operation.
	 * @see metamind.ecore.metamind.DeclarativeMemory#request()
	 * @generated
	 */
	EOperation getDeclarativeMemory__Request();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.ProceduralMemory <em>Procedural Memory</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Procedural Memory</em>'.
	 * @see metamind.ecore.metamind.ProceduralMemory
	 * @generated
	 */
	EClass getProceduralMemory();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.ProceduralMemory#getRules <em>Rules</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Rules</em>'.
	 * @see metamind.ecore.metamind.ProceduralMemory#getRules()
	 * @see #getProceduralMemory()
	 * @generated
	 */
	EReference getProceduralMemory_Rules();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Motor <em>Motor</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Motor</em>'.
	 * @see metamind.ecore.metamind.Motor
	 * @generated
	 */
	EClass getMotor();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Visual <em>Visual</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Visual</em>'.
	 * @see metamind.ecore.metamind.Visual
	 * @generated
	 */
	EClass getVisual();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Rule <em>Rule</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Rule</em>'.
	 * @see metamind.ecore.metamind.Rule
	 * @generated
	 */
	EClass getRule();

	/**
	 * Returns the meta object for the containment reference '{@link metamind.ecore.metamind.Rule#getConditions <em>Conditions</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference '<em>Conditions</em>'.
	 * @see metamind.ecore.metamind.Rule#getConditions()
	 * @see #getRule()
	 * @generated
	 */
	EReference getRule_Conditions();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Rule#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Rule#getName()
	 * @see #getRule()
	 * @generated
	 */
	EAttribute getRule_Name();

	/**
	 * Returns the meta object for the containment reference '{@link metamind.ecore.metamind.Rule#getActions <em>Actions</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference '<em>Actions</em>'.
	 * @see metamind.ecore.metamind.Rule#getActions()
	 * @see #getRule()
	 * @generated
	 */
	EReference getRule_Actions();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Chunk <em>Chunk</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Chunk</em>'.
	 * @see metamind.ecore.metamind.Chunk
	 * @generated
	 */
	EClass getChunk();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Chunk#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Chunk#getName()
	 * @see #getChunk()
	 * @generated
	 */
	EAttribute getChunk_Name();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.Chunk#getSlot <em>Slot</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Slot</em>'.
	 * @see metamind.ecore.metamind.Chunk#getSlot()
	 * @see #getChunk()
	 * @generated
	 */
	EReference getChunk_Slot();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Condition <em>Condition</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Condition</em>'.
	 * @see metamind.ecore.metamind.Condition
	 * @generated
	 */
	EClass getCondition();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.Condition#getLHSbuffers <em>LH Sbuffers</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>LH Sbuffers</em>'.
	 * @see metamind.ecore.metamind.Condition#getLHSbuffers()
	 * @see #getCondition()
	 * @generated
	 */
	EReference getCondition_LHSbuffers();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Environment <em>Environment</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Environment</em>'.
	 * @see metamind.ecore.metamind.Environment
	 * @generated
	 */
	EClass getEnvironment();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Environment#getName <em>Name</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Name</em>'.
	 * @see metamind.ecore.metamind.Environment#getName()
	 * @see #getEnvironment()
	 * @generated
	 */
	EAttribute getEnvironment_Name();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Action <em>Action</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Action</em>'.
	 * @see metamind.ecore.metamind.Action
	 * @generated
	 */
	EClass getAction();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.Action#getRHSbuffers <em>RH Sbuffers</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>RH Sbuffers</em>'.
	 * @see metamind.ecore.metamind.Action#getRHSbuffers()
	 * @see #getAction()
	 * @generated
	 */
	EReference getAction_RHSbuffers();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.WorkingMemory <em>Working Memory</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Working Memory</em>'.
	 * @see metamind.ecore.metamind.WorkingMemory
	 * @generated
	 */
	EClass getWorkingMemory();

	/**
	 * Returns the meta object for the containment reference list '{@link metamind.ecore.metamind.WorkingMemory#getWmchunks <em>Wmchunks</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the containment reference list '<em>Wmchunks</em>'.
	 * @see metamind.ecore.metamind.WorkingMemory#getWmchunks()
	 * @see #getWorkingMemory()
	 * @generated
	 */
	EReference getWorkingMemory_Wmchunks();

	/**
	 * Returns the meta object for class '{@link metamind.ecore.metamind.Slot <em>Slot</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for class '<em>Slot</em>'.
	 * @see metamind.ecore.metamind.Slot
	 * @generated
	 */
	EClass getSlot();

	/**
	 * Returns the meta object for the attribute '{@link metamind.ecore.metamind.Slot#getValue <em>Value</em>}'.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the meta object for the attribute '<em>Value</em>'.
	 * @see metamind.ecore.metamind.Slot#getValue()
	 * @see #getSlot()
	 * @generated
	 */
	EAttribute getSlot_Value();

	/**
	 * Returns the factory that creates the instances of the model.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the factory that creates the instances of the model.
	 * @generated
	 */
	MetamindFactory getMetamindFactory();

	/**
	 * <!-- begin-user-doc -->
	 * Defines literals for the meta objects that represent
	 * <ul>
	 *   <li>each class,</li>
	 *   <li>each feature of each class,</li>
	 *   <li>each operation of each class,</li>
	 *   <li>each enum,</li>
	 *   <li>and each data type</li>
	 * </ul>
	 * <!-- end-user-doc -->
	 * @generated
	 */
	interface Literals {
		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ModelImpl <em>Model</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ModelImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getModel()
		 * @generated
		 */
		EClass MODEL = eINSTANCE.getModel();

		/**
		 * The meta object literal for the '<em><b>Modules</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MODEL__MODULES = eINSTANCE.getModel_Modules();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MODEL__NAME = eINSTANCE.getModel_Name();

		/**
		 * The meta object literal for the '<em><b>Environment</b></em>' containment reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MODEL__ENVIRONMENT = eINSTANCE.getModel_Environment();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ModuleImpl <em>Module</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ModuleImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getModule()
		 * @generated
		 */
		EClass MODULE = eINSTANCE.getModule();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute MODULE__NAME = eINSTANCE.getModule_Name();

		/**
		 * The meta object literal for the '<em><b>Buffer</b></em>' containment reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference MODULE__BUFFER = eINSTANCE.getModule_Buffer();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.BufferImpl <em>Buffer</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.BufferImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getBuffer()
		 * @generated
		 */
		EClass BUFFER = eINSTANCE.getBuffer();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute BUFFER__NAME = eINSTANCE.getBuffer_Name();

		/**
		 * The meta object literal for the '<em><b>Bufferchunk</b></em>' containment reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference BUFFER__BUFFERCHUNK = eINSTANCE.getBuffer_Bufferchunk();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.DeclarativeMemoryImpl <em>Declarative Memory</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.DeclarativeMemoryImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getDeclarativeMemory()
		 * @generated
		 */
		EClass DECLARATIVE_MEMORY = eINSTANCE.getDeclarativeMemory();

		/**
		 * The meta object literal for the '<em><b>Dmchunks</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference DECLARATIVE_MEMORY__DMCHUNKS = eINSTANCE.getDeclarativeMemory_Dmchunks();

		/**
		 * The meta object literal for the '<em><b>Request</b></em>' operation.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EOperation DECLARATIVE_MEMORY___REQUEST = eINSTANCE.getDeclarativeMemory__Request();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ProceduralMemoryImpl <em>Procedural Memory</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ProceduralMemoryImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getProceduralMemory()
		 * @generated
		 */
		EClass PROCEDURAL_MEMORY = eINSTANCE.getProceduralMemory();

		/**
		 * The meta object literal for the '<em><b>Rules</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference PROCEDURAL_MEMORY__RULES = eINSTANCE.getProceduralMemory_Rules();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.MotorImpl <em>Motor</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.MotorImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getMotor()
		 * @generated
		 */
		EClass MOTOR = eINSTANCE.getMotor();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.VisualImpl <em>Visual</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.VisualImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getVisual()
		 * @generated
		 */
		EClass VISUAL = eINSTANCE.getVisual();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.RuleImpl <em>Rule</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.RuleImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getRule()
		 * @generated
		 */
		EClass RULE = eINSTANCE.getRule();

		/**
		 * The meta object literal for the '<em><b>Conditions</b></em>' containment reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference RULE__CONDITIONS = eINSTANCE.getRule_Conditions();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute RULE__NAME = eINSTANCE.getRule_Name();

		/**
		 * The meta object literal for the '<em><b>Actions</b></em>' containment reference feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference RULE__ACTIONS = eINSTANCE.getRule_Actions();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ChunkImpl <em>Chunk</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ChunkImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getChunk()
		 * @generated
		 */
		EClass CHUNK = eINSTANCE.getChunk();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute CHUNK__NAME = eINSTANCE.getChunk_Name();

		/**
		 * The meta object literal for the '<em><b>Slot</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference CHUNK__SLOT = eINSTANCE.getChunk_Slot();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ConditionImpl <em>Condition</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ConditionImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getCondition()
		 * @generated
		 */
		EClass CONDITION = eINSTANCE.getCondition();

		/**
		 * The meta object literal for the '<em><b>LH Sbuffers</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference CONDITION__LH_SBUFFERS = eINSTANCE.getCondition_LHSbuffers();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.EnvironmentImpl <em>Environment</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.EnvironmentImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getEnvironment()
		 * @generated
		 */
		EClass ENVIRONMENT = eINSTANCE.getEnvironment();

		/**
		 * The meta object literal for the '<em><b>Name</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute ENVIRONMENT__NAME = eINSTANCE.getEnvironment_Name();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.ActionImpl <em>Action</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.ActionImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getAction()
		 * @generated
		 */
		EClass ACTION = eINSTANCE.getAction();

		/**
		 * The meta object literal for the '<em><b>RH Sbuffers</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference ACTION__RH_SBUFFERS = eINSTANCE.getAction_RHSbuffers();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.WorkingMemoryImpl <em>Working Memory</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.WorkingMemoryImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getWorkingMemory()
		 * @generated
		 */
		EClass WORKING_MEMORY = eINSTANCE.getWorkingMemory();

		/**
		 * The meta object literal for the '<em><b>Wmchunks</b></em>' containment reference list feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EReference WORKING_MEMORY__WMCHUNKS = eINSTANCE.getWorkingMemory_Wmchunks();

		/**
		 * The meta object literal for the '{@link metamind.ecore.metamind.impl.SlotImpl <em>Slot</em>}' class.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @see metamind.ecore.metamind.impl.SlotImpl
		 * @see metamind.ecore.metamind.impl.MetamindPackageImpl#getSlot()
		 * @generated
		 */
		EClass SLOT = eINSTANCE.getSlot();

		/**
		 * The meta object literal for the '<em><b>Value</b></em>' attribute feature.
		 * <!-- begin-user-doc -->
		 * <!-- end-user-doc -->
		 * @generated
		 */
		EAttribute SLOT__VALUE = eINSTANCE.getSlot_Value();

	}

} //MetamindPackage
