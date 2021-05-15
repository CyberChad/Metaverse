/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Module</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Module#getName <em>Name</em>}</li>
 *   <li>{@link metamind.ecore.metamind.Module#getBuffer <em>Buffer</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getModule()
 * @model abstract="true"
 * @generated
 */
public interface Module extends EObject {
	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see metamind.ecore.metamind.MetamindPackage#getModule_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Module#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Buffer</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Buffer</em>' containment reference.
	 * @see #setBuffer(Buffer)
	 * @see metamind.ecore.metamind.MetamindPackage#getModule_Buffer()
	 * @model containment="true"
	 * @generated
	 */
	Buffer getBuffer();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Module#getBuffer <em>Buffer</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Buffer</em>' containment reference.
	 * @see #getBuffer()
	 * @generated
	 */
	void setBuffer(Buffer value);

} // Module
