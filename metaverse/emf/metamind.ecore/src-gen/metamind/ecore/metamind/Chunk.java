/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Chunk</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Chunk#getName <em>Name</em>}</li>
 *   <li>{@link metamind.ecore.metamind.Chunk#getSlot <em>Slot</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getChunk()
 * @model
 * @generated
 */
public interface Chunk extends EObject {
	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see metamind.ecore.metamind.MetamindPackage#getChunk_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Chunk#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Slot</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Slot}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Slot</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getChunk_Slot()
	 * @model containment="true" required="true"
	 * @generated
	 */
	EList<Slot> getSlot();

} // Chunk
