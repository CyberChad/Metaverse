/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Condition</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Condition#getLHSbuffers <em>LH Sbuffers</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getCondition()
 * @model
 * @generated
 */
public interface Condition extends EObject {
	/**
	 * Returns the value of the '<em><b>LH Sbuffers</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Buffer}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>LH Sbuffers</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getCondition_LHSbuffers()
	 * @model containment="true" required="true"
	 * @generated
	 */
	EList<Buffer> getLHSbuffers();

} // Condition
