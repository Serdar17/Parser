
# Parser

## Api documentation for `https://parserapp.serdar17.repl.co/docs#/`

##### Содержание  

[/Product](#/product) 


<a name="/product"><h2>/Product</h2></a>


----
  Created and returns json data about a product.

* **URL**

  /product

* **Method:**

  `POST`
  
*  **URL Params**

   None

* **Data Params**

  `
  {
  "name": "string",
  "description": "string",
  "price": 0
  }
  `

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ name : "Product name", description: "Product description", price: 100.0 }`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "Product with current name exist" }`

* **Sample Call: CURL**

  ```curl -X 'POST' \
  'https://parserapp.serdar17.repl.co/product/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "description": "string",
  "price": 0
  }'
  ```

**/Products**
----
  Returns array of json data about a products.

* **URL**

  /products/?skip=0&limit=10

* **Method:**

  `GET`
  
*  **QUERY Params**

   **Nont Required:**
 
   `skip=[integer], by default 0`
   `limit=[integer], by default 100`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12, name : "Michael Bloom" }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
    });
  ```
