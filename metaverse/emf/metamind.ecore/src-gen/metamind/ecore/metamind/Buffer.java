/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Buffer</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Buffer#getName <em>Name</em>}</li>
 *   <li>{@link metamind.ecore.metamind.Buffer#getBufferchunk <em>Bufferchunk</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getBuffer()
 * @model
 * @generated
 */
public interface Buffer extends EObject {
	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see metamind.ecore.metamind.MetamindPackage#getBuffer_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Buffer#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Bufferchunk</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Bufferchunk</em>' containment reference.
	 * @see #setBufferchunk(Chunk)
	 * @see metamind.ecore.metamind.MetamindPackage#getBuffer_Bufferchunk()
	 * @model containment="true"
	 * @generated
	 */
	Chunk getBufferchunk();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Buffer#getBufferchunk <em>Bufferchunk</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Bufferchunk</em>' containment reference.
	 * @see #getBufferchunk()
	 * @generated
	 */
	void setBufferchunk(Chunk value);

} // Buffer
