/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Action</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Action#getRHSbuffers <em>RH Sbuffers</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getAction()
 * @model
 * @generated
 */
public interface Action extends EObject {
	/**
	 * Returns the value of the '<em><b>RH Sbuffers</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Buffer}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>RH Sbuffers</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getAction_RHSbuffers()
	 * @model containment="true" required="true"
	 * @generated
	 */
	EList<Buffer> getRHSbuffers();

} // Action
