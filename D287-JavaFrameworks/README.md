# WESTERN GOVERNORS UNIVERSITY 

Robert Kearns | ID: 011818662 | D287 – Java Frameworks

---

## Project Description
You are working for a company that licenses and customizes a software application to keep track of inventory in stores. Your job as a software developer is to customize this application to meet a specific customer’s needs.

## Project Requirements
Detailed below are the requirements and proof of changes as required with submission With Prompt, File Name, Line Number(s), and Change Descriptions.

### C. Customize User Interface
***Prompt:*** Customize the HTML user interface for your customer’s application. The user interface should include the shop name, the product names, and the names of the parts.

***Commit Message:*** Requirement C - Customized HTML and CSS on mainscreen.html for customer. Added notes to README for changes.

***File:*** \src\main\resources\templates\mainscreen.html
- Lines 14 - 18
    - Added internal CSS for background color to cadetblue.
- Line 19
    - Update title to "Bob's Bakery".
- Line 24
    - Update h1 element to Bob's Bakery Inventory.

### D. About Page with Navigation
***Prompt:*** Add an “About” page to the application to describe your chosen customer’s company to web viewers and include navigation to and from the “About” page and the main screen.

***Commit Message:*** Requirement D - Created an about page for company, created AboutController to handle requests to navigate to the page, added button to allow user to navigate to main page. Updated mainscreen to have a button element to allow user to navigate to about page.

***File:*** \src\main\resources\templates\about.html
- New file - All lines
  - Created about.html file to describe the Bob's Bakery company with internal CSS for styling. 
  - Added button to return the user to the main page.

***File:*** \src\main\java\com\example\demo\controllers\AboutController.java
- New File - All lines
  - Created class AboutController to use the @GetMapping method to route requests to the about.html page.

***File:*** \src\main\resources\templates\mainscreen.html
- Lines: 25 - 27
  - Added button to navigate user to about page.

### E.  Sample Inventory
***Prompt:*** Add a sample inventory appropriate for your chosen store to the application. You should have five parts and five products in your sample inventory and should not overwrite existing data in the database.

***Commit Message:*** Requirement E - Added sample inventory of 5 parts and 5 products objects. Added conditional logic for inventory to be added if part and product lists are empty.

***File:*** \src\main\java\com\example\demo\bootstrap\BootStrapData.java
- Lines: 59 - 93
  - Sample parts added to bootstrap data.
- Lines: 99 - 117
  - Sample products added to bootstrap data. Implemented conditional functionality implemented to only add the parts and products to the application if the part and product lists are empty. 


### F. Buy Now Button for Products
***Prompt:*** Add a “Buy Now” button to your product list. Your “Buy Now” button must meet each of the following parameters:
  - The “Buy Now” button must be next to the buttons that update and delete products.
  - The button should decrement the inventory of that product by one. It should not affect the inventory of any of the associated parts.
  - Display a message that indicates the success or failure of a purchase.

***Commit Message:*** Requirement F - Updated README formatting and content. Updated about page for formatting and style. Added Buy Now button for products section to complete purchases if there is inventory.

***File:*** src\main\java\com\example\demo\controllers\BuyProductController.java
- New File - All lines
   - Created new controller for Buy Now button in Product section of mainscreen.html. The productID is passed to/buyProduct using @RequestMapping. 
   - Logic is implemented to confirm the product inventory is greater than zero. Depending on outcome, user will be navigated to a purchase success or purchase failure page.
   - If successful, logic implemented to decrease product inventory by one.

***File:*** src\main\resources\templates\buyProductFail.html
- New File - All lines
  - Created buyProductfail.html page for the user to be navigated to if the Buy Now functionality fails based on logic in the BuyProductController

***File:*** src\main\resources\templates\buyProductSuccess.html
- New File - All lines
  - Created buyProductSuccess.html page for the user to be navigated to if the Buy Now functionality succeeds based on logic in the BuyProductController

***File:*** src\main\resources\templates\mainscreen.html
- Line 93: 
  - Added button for Buy Now functionality to Product List. Referenced the button to invoke the BuyProductController


### G. Part Maximum and Minimum Inventory Tracking

***Prompt:*** Modify the parts to track maximum and minimum inventory by doing the following:
- Add additional fields to the part entity for maximum and minimum inventory.
- Modify the sample inventory to include the maximum and minimum fields.
- Add to the InhousePartForm and OutsourcedPartForm forms additional text inputs for the inventory so the user can set the maximum and minimum values.
- Rename the file the persistent storage is saved to.
- Modify the code to enforce that the inventory is between or at the minimum and maximum value.

***Commit Message:*** Requirement G - Various style updates to pages for consistency. New functionality for part inventory min/max bound checking. Update sample data to include new fields. Update persistent database name.

***File:*** src\main\java\com\example\demo\domain\Part.java
- Line: 6
  - Imported additional java validation package for Max contraint.
- Lines: 32 - 35
  - Created additional fields for maximum and minimum inventory, includes respective contraints. 
- Lines: 57 - 65
  - Create new overloaded Part constructor to contain the new maximum and minimum fields.
- Lines: 107 - 118
  - Add getter and setter methods for maximum and minimum inventory fields.
  - Created isInvInRange method that returns a boolean to check if the inventory of a part is within the maximum and minimum range.

***File:*** src\main\java\com\example\demo\bootstrap\BootStrapData.java
- Lines: 66,67,75,76,84,85,93,94,101,102
  - Updated sample parts inventory to include the maximum and inventory fields. 

***File:*** src\main\resources\templates\InhousePartForm.html
- Numerous lines:
  - Cleaned up HTML indentation and spacing for readability, added/updated CSS.
- Lines: 65 - 69
  - Added additional text input fields for maximum and minimum inventory so user can set these values on the form.

***File:*** src\main\resources\templates\OutsourcedPartForm.html
- Numerous lines:
  - Cleaned up HTML indentation and spacing for readability, added/updated CSS.
- Lines: 64 - 68
  - Added additional text input fields for maximum and minimum inventory so user can set these values on the form.

***File:*** src\main\resources\application.properties
- Line: 6
  - Renamed the file for persistent storage that corresponds to company name.

***File:*** src\main\java\com\example\demo\controllers\AddInhousePartController.java
- Lines: 42 - 46
  - Created conditional to check if inventory is in range of maximum and minimum values using the isInvInRange method. Produced error message to user of value out of bounds and does not submit form.

***File:*** src\main\java\com\example\demo\controllers\AddOutsourcedPartController.java
- Lines:43 - 47
  - Created conditional to check if inventory is in range of maximum and minimum values using the isInvInRange method. Produced error message to user of value out of bounds and does not submit form.

### H.  Validation for Maximum and Minimum Fields, Including Error Messaging

***Prompt:*** Add validation for between or at the maximum and minimum fields. The validation must include the following:
- Display error messages for low inventory when adding and updating parts if the inventory is less than the minimum number of parts.
- Display error messages for low inventory when adding and updating products lowers the part inventory below the minimum.
- Display error messages when adding and updating parts if the inventory is greater than the maximum.

***Commit Message:*** Requirement H - Added validation functionality for part maximum and minimum value, included error messaging if values are outside of the bounds.

***File:*** src\main\java\com\example\demo\domain\Part.java
- Lines: 118 - 125
  - Created two methods isInvInMinBound and isInvInMaxBound to return boolean value to use in validation created in controllers.

***File:*** src\main\java\com\example\demo\controllers\AddOutsourcedPartController.java
- Lines: 48 - 55
  - Added conditionals to reject values if they are above the maximum or minimum inventory values. Also shows error message to user depending on which bound is violated.

***File:*** src\main\java\com\example\demo\controllers\AddOutsourcedPartController.java
- Lines: 47 - 54
  - Added conditionals to reject values if they are above the maximum or minimum inventory values. Also shows error message to user depending on which bound is violated.

***File:*** src\main\java\com\example\demo\validators\EnufPartsValidator.java
- Line: 36
  - Updated conditional statement to include an OR logic for if the (current inventory - 1) is less than the minimum inventory of the part to make the method return false.

***File:*** src\main\java\com\example\demo\validators\ValidEnufParts.java
- Line: 20
  - Updated message to include clarity that the parts inventory would be below minimum amounts if the action completed.

### I.  Part Unit Tests
***Prompt:*** Add at least two unit tests for the maximum and minimum fields to the PartTest class in the test package.

***Commit Message:*** Requirement I - Created two unit tests for testing the minimum and maximum inventory validations.

***File:*** src\test\java\com\example\demo\domain
- Lines: 130 - 147
  - Created two unit tests named testIsInvInMaxBound() and testIsInvInMinBound(). 


### J.  Remove Unused Class Files
***Prompt:*** Remove the class files for any unused validators in order to clean your code.

***Commit Message:*** Requirement J - Removed class DeletePartValidator.java as it is not used in application.

***Files:*** src\main\java\com\example\demo\validators\DeletePartValidator.java
- File/class deleted since it was not used throughout application.

---

## Revisions for Second Submission:
### G. Part Maximum and Minimum Inventory Tracking
***Evaluator Comment:*** "The parts minimum and maximum inventory fields are not sufficiently available in the parts table."

***Commit Message:*** Requirement G (Revision2): Updated Parts table to include Min and Max Inventory values for each part. Updated part related fields and methods for min and max inventory functionality.

***File:*** \src\main\resources\templates\mainscreen.html
- Lines: 46-47
  - Add table headers for Max & Min Inventory
- Lines: 56-57
  - Add table data to display Max and Min Inventory values in the parts table
  
***File:*** src\main\java\com\example\demo\domain\Part.java
- Lines: 33-34
  - Removed Max annotation for maximumInv field, not required constraint on the maximum inventory field.
  - Removed static from minimumInv and maximumInv fields.
- Lines: 114, 118, 122
  - Removed static from isInvInRange, isInvInMinBound, and isInvInMaxBound methods

***File:*** src\main\java\com\example\demo\controllers\AddInhousePartController.java
- Lines: 43, 47, 51
  - Updated method calls so that Non-static methods are not referenced from a static context

***File:*** src\main\java\com\example\demo\controllers\AddOutsourcedPartController.java
- Lines: 44, 48, 52
  - Updated method calls so that Non-static methods are not referenced from a static context