/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Working Memory</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.WorkingMemory#getWmchunks <em>Wmchunks</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getWorkingMemory()
 * @model
 * @generated
 */
public interface WorkingMemory extends metamind.ecore.metamind.Module {
	/**
	 * Returns the value of the '<em><b>Wmchunks</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Chunk}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Wmchunks</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getWorkingMemory_Wmchunks()
	 * @model containment="true"
	 * @generated
	 */
	EList<Chunk> getWmchunks();

} // WorkingMemory
