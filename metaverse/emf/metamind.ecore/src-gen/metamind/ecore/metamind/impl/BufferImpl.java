/**
 */
package metamind.ecore.metamind.impl;

import metamind.ecore.metamind.Buffer;
import metamind.ecore.metamind.Chunk;
import metamind.ecore.metamind.MetamindPackage;

import org.eclipse.emf.common.notify.Notification;
import org.eclipse.emf.common.notify.NotificationChain;

import org.eclipse.emf.ecore.EClass;
import org.eclipse.emf.ecore.InternalEObject;

import org.eclipse.emf.ecore.impl.ENotificationImpl;
import org.eclipse.emf.ecore.impl.MinimalEObjectImpl;

/**
 * <!-- begin-user-doc -->
 * An implementation of the model object '<em><b>Buffer</b></em>'.
 * <!-- end-user-doc -->
 * <p>
 * The following features are implemented:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.impl.BufferImpl#getName <em>Name</em>}</li>
 *   <li>{@link metamind.ecore.metamind.impl.BufferImpl#getBufferchunk <em>Bufferchunk</em>}</li>
 * </ul>
 *
 * @generated
 */
public class BufferImpl extends MinimalEObjectImpl.Container implements Buffer {
	/**
	 * The default value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected static final String NAME_EDEFAULT = null;

	/**
	 * The cached value of the '{@link #getName() <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getName()
	 * @generated
	 * @ordered
	 */
	protected String name = NAME_EDEFAULT;

	/**
	 * The cached value of the '{@link #getBufferchunk() <em>Bufferchunk</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @see #getBufferchunk()
	 * @generated
	 * @ordered
	 */
	protected Chunk bufferchunk;

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	protected BufferImpl() {
		super();
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	protected EClass eStaticClass() {
		return MetamindPackage.Literals.BUFFER;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public String getName() {
		return name;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setName(String newName) {
		String oldName = name;
		name = newName;
		if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, MetamindPackage.BUFFER__NAME, oldName, name));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public Chunk getBufferchunk() {
		return bufferchunk;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public NotificationChain basicSetBufferchunk(Chunk newBufferchunk, NotificationChain msgs) {
		Chunk oldBufferchunk = bufferchunk;
		bufferchunk = newBufferchunk;
		if (eNotificationRequired()) {
			ENotificationImpl notification = new ENotificationImpl(this, Notification.SET,
					MetamindPackage.BUFFER__BUFFERCHUNK, oldBufferchunk, newBufferchunk);
			if (msgs == null)
				msgs = notification;
			else
				msgs.add(notification);
		}
		return msgs;
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	public void setBufferchunk(Chunk newBufferchunk) {
		if (newBufferchunk != bufferchunk) {
			NotificationChain msgs = null;
			if (bufferchunk != null)
				msgs = ((InternalEObject) bufferchunk).eInverseRemove(this,
						EOPPOSITE_FEATURE_BASE - MetamindPackage.BUFFER__BUFFERCHUNK, null, msgs);
			if (newBufferchunk != null)
				msgs = ((InternalEObject) newBufferchunk).eInverseAdd(this,
						EOPPOSITE_FEATURE_BASE - MetamindPackage.BUFFER__BUFFERCHUNK, null, msgs);
			msgs = basicSetBufferchunk(newBufferchunk, msgs);
			if (msgs != null)
				msgs.dispatch();
		} else if (eNotificationRequired())
			eNotify(new ENotificationImpl(this, Notification.SET, MetamindPackage.BUFFER__BUFFERCHUNK, newBufferchunk,
					newBufferchunk));
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public NotificationChain eInverseRemove(InternalEObject otherEnd, int featureID, NotificationChain msgs) {
		switch (featureID) {
		case MetamindPackage.BUFFER__BUFFERCHUNK:
			return basicSetBufferchunk(null, msgs);
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
		case MetamindPackage.BUFFER__NAME:
			return getName();
		case MetamindPackage.BUFFER__BUFFERCHUNK:
			return getBufferchunk();
		}
		return super.eGet(featureID, resolve, coreType);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public void eSet(int featureID, Object newValue) {
		switch (featureID) {
		case MetamindPackage.BUFFER__NAME:
			setName((String) newValue);
			return;
		case MetamindPackage.BUFFER__BUFFERCHUNK:
			setBufferchunk((Chunk) newValue);
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
		case MetamindPackage.BUFFER__NAME:
			setName(NAME_EDEFAULT);
			return;
		case MetamindPackage.BUFFER__BUFFERCHUNK:
			setBufferchunk((Chunk) null);
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
		case MetamindPackage.BUFFER__NAME:
			return NAME_EDEFAULT == null ? name != null : !NAME_EDEFAULT.equals(name);
		case MetamindPackage.BUFFER__BUFFERCHUNK:
			return bufferchunk != null;
		}
		return super.eIsSet(featureID);
	}

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @generated
	 */
	@Override
	public String toString() {
		if (eIsProxy())
			return super.toString();

		StringBuilder result = new StringBuilder(super.toString());
		result.append(" (name: ");
		result.append(name);
		result.append(')');
		return result.toString();
	}

} //BufferImpl
