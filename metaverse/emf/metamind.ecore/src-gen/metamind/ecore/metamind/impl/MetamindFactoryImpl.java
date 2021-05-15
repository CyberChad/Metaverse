/**
 */
package metamind.ecore.metamind.impl;

import metamind.ecore.metamind.Action;
import metamind.ecore.metamind.Buffer;
import metamind.ecore.metamind.Chunk;
import metamind.ecore.metamind.Condition;
import metamind.ecore.metamind.DeclarativeMemory;
import metamind.ecore.metamind.Environment;
import metamind.ecore.metamind.MetamindFactory;
import metamind.ecore.metamind.MetamindPackage;
import metamind.ecore.metamind.Model;
import metamind.ecore.metamind.Motor;
import metamind.ecore.metamind.ProceduralMemory;
import metamind.ecore.metamind.Rule;
import metamind.ecore.metamind.Slot;
import metamind.ecore.metamind.Visual;
import metamind.ecore.metamind.WorkingMemory;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.emf.ecore.EPackage;

import org.eclipse.emf.ecore.impl.EFactoryImpl;

import org.eclipse.emf.ecore.plugin.EcorePlugin;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model <b>Factory</b>.
 * <!-- end-user-doc -->
 * @generated
 */
public class MetamindFactoryImpl extends EFactoryImpl implements MetamindFactory {
	/**
	 * Creates the default factory implementation.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public static MetamindFactory init() {
		try {
			MetamindFactory theMetamindFactory = (MetamindFactory) EPackage.Registry.INSTANCE
					.getEFactory(MetamindPackage.eNS_URI);
			if (theMetamindFactory != null) {
				return theMetamindFactory;
			}
		} catch (Exception exception) {
			EcorePlugin.INSTANCE.log(exception);
		}
		return new MetamindFactoryImpl();
	}

	/**
	 * Creates an instance of the factory.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MetamindFactoryImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public EObject create(EClass eClass) {
		switch (eClass.getClassifierID()) {
		case MetamindPackage.MODEL:
			return createModel();
		case MetamindPackage.BUFFER:
			return createBuffer();
		case MetamindPackage.DECLARATIVE_MEMORY:
			return createDeclarativeMemory();
		case MetamindPackage.PROCEDURAL_MEMORY:
			return createProceduralMemory();
		case MetamindPackage.MOTOR:
			return createMotor();
		case MetamindPackage.VISUAL:
			return createVisual();
		case MetamindPackage.RULE:
			return createRule();
		case MetamindPackage.CHUNK:
			return createChunk();
		case MetamindPackage.CONDITION:
			return createCondition();
		case MetamindPackage.ENVIRONMENT:
			return createEnvironment();
		case MetamindPackage.ACTION:
			return createAction();
		case MetamindPackage.WORKING_MEMORY:
			return createWorkingMemory();
		case MetamindPackage.SLOT:
			return createSlot();
		default:
			throw new IllegalArgumentException("The class '" + eClass.getName() + "' is not a valid classifier");
		}
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Model createModel() {
		ModelImpl model = new ModelImpl();
		return model;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Buffer createBuffer() {
		BufferImpl buffer = new BufferImpl();
		return buffer;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public DeclarativeMemory createDeclarativeMemory() {
		DeclarativeMemoryImpl declarativeMemory = new DeclarativeMemoryImpl();
		return declarativeMemory;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public ProceduralMemory createProceduralMemory() {
		ProceduralMemoryImpl proceduralMemory = new ProceduralMemoryImpl();
		return proceduralMemory;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Motor createMotor() {
		MotorImpl motor = new MotorImpl();
		return motor;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Visual createVisual() {
		VisualImpl visual = new VisualImpl();
		return visual;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Rule createRule() {
		RuleImpl rule = new RuleImpl();
		return rule;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Chunk createChunk() {
		ChunkImpl chunk = new ChunkImpl();
		return chunk;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Condition createCondition() {
		ConditionImpl condition = new ConditionImpl();
		return condition;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Environment createEnvironment() {
		EnvironmentImpl environment = new EnvironmentImpl();
		return environment;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Action createAction() {
		ActionImpl action = new ActionImpl();
		return action;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public WorkingMemory createWorkingMemory() {
		WorkingMemoryImpl workingMemory = new WorkingMemoryImpl();
		return workingMemory;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Slot createSlot() {
		SlotImpl slot = new SlotImpl();
		return slot;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public MetamindPackage getMetamindPackage() {
		return (MetamindPackage) getEPackage();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @deprecated
	 * @generated
	 */
	@Deprecated
	public static MetamindPackage getPackage() {
		return MetamindPackage.eINSTANCE;
	}

} //MetamindFactoryImpl
