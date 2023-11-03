// customerList.spec.js

describe('CustomerList Page', () => {

    beforeEach(() => {
        cy.login('datalake_user', '123');
        cy.wait(2000)
        cy.visit('http://localhost:8080/customer-list'); // Replace with the actual URL for your CustomerList page
      });

    it('should open and close the "Add New Customer" modal', () => {

      cy.get('button:contains("Add New Customer")').click();
      cy.get('.modal-overlay').should('be.visible');
      cy.get('button:contains("Cancel")').click();
    });

    it('should add a new customer', () => {
        cy.get('button:contains("Add New Customer")').click();
        cy.get('.modal-overlay').should('be.visible');
    
        // Fill in the customer information
        cy.get('input[name="customerName"]').type('John Doe');
        cy.get('input[name="customerCompany"]').type('ABC Inc');
        cy.get('input[name="customerEmail"]').type('123@456.com')       // Add more input field interactions as needed
    
        cy.get('button:contains("Save")').click();
    
        // Wait for the save to complete (adjust the timeout as needed)
        cy.wait(2000);
    
        // Verify that the new customer is added to the list
        cy.contains('John Doe');
        cy.contains('ABC Inc');
        // Add more assertions for other fields as needed
      });
  
    it('should edit a customer', () => {
      // Assume you have at least one customer in the list
      cy.get('button:contains("Edit"):first').click(); // Edit the first customer in the list
      cy.get('.modal-overlay').should('be.visible');
  
      // Modify the customer information
      cy.get('input[name="customerName"]').clear().type('Updated Name');
      cy.get('input[name="customerCompany"]').clear().type('Updated Company');
      // Add more input field interactions as needed
  
      cy.get('button:contains("Update")').click();
  
      // Wait for the update to complete (adjust the timeout as needed)
      cy.wait(2000);
  
      // Verify that the customer is updated in the list
      cy.contains('Updated Name');
      cy.contains('Updated Company');
      // Add more assertions for other fields as needed
    });
  
    it('should delete a customer', () => {
      // Assume you have at least one customer in the list
      cy.get('button:contains("Delete"):first').click(); // Delete the first customer in the list
      cy.wait(2000);
  
      // Verify that the customer is removed from the list
      cy.contains('Updated Name').should('not.exist'); // Replace with the actual customer name
    });
  });
  