Feature: Product management
  As a user
  I want to search and manage products
  So that I can maintain the product catalogue

  Background:
    Given the following products
      | name   | description    | price | available | category    |
      | Hat    | A red fedora   | 29.99 | true      | Clothing    |
      | Shoes  | Running shoes  | 59.99 | false     | Clothing    |
      | Big Mac| Burger         | 5.99  | true      | Food        |
      | Sheets | Bed sheets     | 25.00 | true      | Furniture   |

  Scenario: Read a Product
    Given I visit the Home Page
    When I enter "Hat" in the Name field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    When I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the ID field
    And I press the "Search" button
    Then I should see the message "Success"
    And the product Name should be "Hat"
    And the product Description should be "A red fedora"
    And the product Available should be "True"
    And the product Category should be "Clothing"
    And the product Price should be "29.99"

  Scenario: Update a Product
    Given I visit the Home Page
    When I enter "Hat" in the Name field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    When I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the ID field
    And I press the "Search" button
    Then I should see the message "Success"
    When I update the product name to "Fedora"
    And I press the "Update" button
    Then I should see the message "Success"
    And I should see "Fedora" in the results
    And I should not see "Hat" in the results
    When I clear the form
    And I enter the copied ID in the ID field
    And I press the "Search" button
    Then the product Name should be "Fedora"

  Scenario: Delete a Product
    Given I visit the Home Page
    When I enter "Hat" in the Name field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    When I copy the ID of product "Hat"
    And I clear the form
    And I enter the copied ID in the ID field
    And I press the "Search" button
    When I press the "Delete" button
    Then I should see the message "Hat has been deleted"
    When I clear all filters
    And I press the "Search" button
    Then I should not see "Hat" in the results

  Scenario: List all products
    When I visit the "Home Page"
    And I press the "Clear" button
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Shoes" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results

  Scenario: Search for products by name
    When I visit the "Home Page"
    And I press the "Clear" button
    And I enter "Hat" in the "Name" field
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see the description "A red fedora"

  Scenario: Search for products by category
    When I visit the "Home Page"
    And I press the "Clear" button
    And I select "Food" from the "Category" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Big Mac" in the results
    And I should not see "Hat" in the results
    And I should not see "Shoes" in the results
    And I should not see "Sheets" in the results

  Scenario: Search for products by availability
    When I visit the "Home Page"
    And I press the "Clear" button
    And I select "True" from the "Available" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Hat" in the results
    And I should see "Big Mac" in the results
    And I should see "Sheets" in the results
    And I should not see "Shoes" in the results
