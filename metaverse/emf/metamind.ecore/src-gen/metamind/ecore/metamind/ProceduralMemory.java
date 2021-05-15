/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Procedural Memory</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.ProceduralMemory#getRules <em>Rules</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getProceduralMemory()
 * @model
 * @generated
 */
public interface ProceduralMemory extends metamind.ecore.metamind.Module {
	/**
	 * Returns the value of the '<em><b>Rules</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Rule}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Rules</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getProceduralMemory_Rules()
	 * @model containment="true"
	 * @generated
	 */
	EList<Rule> getRules();

} // ProceduralMemory
