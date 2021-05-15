/**
 */
package metamind.ecore.metamind;

import org.eclipse.emf.ecore.EObject;

/**
 * <!-- begin-user-doc -->
 * A representation of the model object '<em><b>Rule</b></em>'.
 * <!-- end-user-doc -->
 *
 * <p>
 * The following features are supported:
 * </p>
 * <ul>
 *   <li>{@link metamind.ecore.metamind.Rule#getConditions <em>Conditions</em>}</li>
 *   <li>{@link metamind.ecore.metamind.Rule#getName <em>Name</em>}</li>
 *   <li>{@link metamind.ecore.metamind.Rule#getActions <em>Actions</em>}</li>
 * </ul>
 *
 * @see metamind.ecore.metamind.MetamindPackage#getRule()
 * @model
 * @generated
 */
public interface Rule extends EObject {
	/**
	 * Returns the value of the '<em><b>Conditions</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Conditions</em>' containment reference.
	 * @see #setConditions(Condition)
	 * @see metamind.ecore.metamind.MetamindPackage#getRule_Conditions()
	 * @model containment="true" required="true"
	 * @generated
	 */
	Condition getConditions();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Rule#getConditions <em>Conditions</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Conditions</em>' containment reference.
	 * @see #getConditions()
	 * @generated
	 */
	void setConditions(Condition value);

	/**
	 * Returns the value of the '<em><b>Name</b></em>' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Name</em>' attribute.
	 * @see #setName(String)
	 * @see metamind.ecore.metamind.MetamindPackage#getRule_Name()
	 * @model
	 * @generated
	 */
	String getName();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Rule#getName <em>Name</em>}' attribute.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Name</em>' attribute.
	 * @see #getName()
	 * @generated
	 */
	void setName(String value);

	/**
	 * Returns the value of the '<em><b>Actions</b></em>' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @return the value of the '<em>Actions</em>' containment reference.
	 * @see #setActions(Action)
	 * @see metamind.ecore.metamind.MetamindPackage#getRule_Actions()
	 * @model containment="true" required="true"
	 * @generated
	 */
	Action getActions();

	/**
	 * Sets the value of the '{@link metamind.ecore.metamind.Rule#getActions <em>Actions</em>}' containment reference.
	 * <!-- begin-user-doc -->
	 * <!-- end-user-doc -->
	 * @param value the new value of the '<em>Actions</em>' containment reference.
	 * @see #getActions()
	 * @generated
	 */
	void setActions(Action value);

} // Rule
