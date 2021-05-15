/**
 */
package metamind.ecore.metamind.impl;

import java.lang.reflect.InvocationTargetException;
import java.util.Collection;

import metamind.ecore.metamind.Chunk;
import metamind.ecore.metamind.DeclarativeMemory;
import metamind.ecore.metamind.MetamindPackage;

import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Declarative Memory</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.impl.DeclarativeMemoryImpl#getDmchunks <em>Dmchunks</em>}</li>
 * </ul>
 *
 * @generated
 */
public class DeclarativeMemoryImpl extends ModuleImpl implements DeclarativeMemory {
	/**
	 * The cached value of the '{@link #getDmchunks() <em>Dmchunks</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getDmchunks()
	 * @generated
	 * @ordered
	 */
	protected EList<Chunk> dmchunks;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected DeclarativeMemoryImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return MetamindPackage.Literals.DECLARATIVE_MEMORY;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EList<Chunk> getDmchunks() {
		if (dmchunks == null) {
			dmchunks = new EObjectContainmentEList<Chunk>(Chunk.class, this,
					MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS);
		}
		return dmchunks;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void request() {
		// TODO: implement this method
		// Ensure that you remove @generated or mark it @generated NOT
		throw new UnsupportedOperationException();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS:
			return ((InternalEList<?>) getDmchunks()).basicRemove(otherEnd, msgs);
		}
		return super.eInverseRemove(otherEnd, featureID, msgs);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eGet(int featureID, boolean resolve, boolean coreType) {
		switch (featureID) {
		case MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS:
			return getDmchunks();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@SuppressWarnings("unchecked")
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
		case MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS:
			getDmchunks().clear();
			getDmchunks().addAll((Collection<? extends Chunk>) newValue);
			return;
		}
		super.eSet(featureID, newValue);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eUnset(int featureID) {
		switch (featureID) {
		case MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS:
			getDmchunks().clear();
			return;
		}
		super.eUnset(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public boolean eIsSet(int featureID) {
		switch (featureID) {
		case MetamindPackage.DECLARATIVE_MEMORY__DMCHUNKS:
			return dmchunks != null && !dmchunks.isEmpty();
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public Object eInvoke(int operationID, EList<?> arguments) throws InvocationTargetException {
		switch (operationID) {
		case MetamindPackage.DECLARATIVE_MEMORY___REQUEST:
			request();
			return null;
		}
		return super.eInvoke(operationID, arguments);
	}

} //DeclarativeMemoryImpl
