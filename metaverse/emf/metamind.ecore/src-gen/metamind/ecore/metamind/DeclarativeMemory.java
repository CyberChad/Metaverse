/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.common.util.EList;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Declarative Memory</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.DeclarativeMemory#getDmchunks <em>Dmchunks</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getDeclarativeMemory()
 * @model
 * @generated
 */
public interface DeclarativeMemory extends metamind.ecore.metamind.Module {
	/**
	 * Returns the value of the '<em><b>Dmchunks</b></em>' containment reference list.
	 * The list contents are of type {@link metamind.ecore.metamind.Chunk}.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Dmchunks</em>' containment reference list.
	 * @see metamind.ecore.metamind.MetamindPackage#getDeclarativeMemory_Dmchunks()
	 * @model containment="true"
	 * @generated
	 */
	EList<Chunk> getDmchunks();

	/**
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @model
	 * @generated
	 */
	void request();

} // DeclarativeMemory
