/**
 */
package metamind.ecore.metamind.impl;

import java.util.Collection;

import metamind.ecore.metamind.Chunk;
import metamind.ecore.metamind.MetamindPackage;
import metamind.ecore.metamind.WorkingMemory;

import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.util.EObjectContainmentEList;
import org.eclipse.emf.ecore.util.InternalEList;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Working Memory</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.impl.WorkingMemoryImpl#getWmchunks <em>Wmchunks</em>}</li>
 * </ul>
 *
 * @generated
 */
public class WorkingMemoryImpl extends ModuleImpl implements WorkingMemory {
	/**
	 * The cached value of the '{@link #getWmchunks() <em>Wmchunks</em>}' containment reference list.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getWmchunks()
	 * @generated
	 * @ordered
	 */
	protected EList<Chunk> wmchunks;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected WorkingMemoryImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return MetamindPackage.Literals.WORKING_MEMORY;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public EList<Chunk> getWmchunks() {
		if (wmchunks == null) {
			wmchunks = new EObjectContainmentEList<Chunk>(Chunk.class, this, MetamindPackage.WORKING_MEMORY__WMCHUNKS);
		}
		return wmchunks;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case MetamindPackage.WORKING_MEMORY__WMCHUNKS:
			return ((InternalEList<?>) getWmchunks()).basicRemove(otherEnd, msgs);
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
		case MetamindPackage.WORKING_MEMORY__WMCHUNKS:
			return getWmchunks();
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
		case MetamindPackage.WORKING_MEMORY__WMCHUNKS:
			getWmchunks().clear();
			getWmchunks().addAll((Collection<? extends Chunk>) newValue);
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
		case MetamindPackage.WORKING_MEMORY__WMCHUNKS:
			getWmchunks().clear();
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
		case MetamindPackage.WORKING_MEMORY__WMCHUNKS:
			return wmchunks != null && !wmchunks.isEmpty();
		}
		return super.eIsSet(featureID);
	}

} //WorkingMemoryImpl
