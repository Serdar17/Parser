
# Parser

## Api documentation for `https://parserapp.serdar17.repl.co/docs#/`

##### Content

[POST /Product](#/product)  
[GET /Products?skip=0&limit=100](#/Products?skip=0&limit=100)  
[GET /Product/{product_id}](#/Product/{product_id})  
[PUT /Product/{product_id}](#PUT_/Product/{product_id})  
[DELETE /Product/{product_id}](#DELETE_/Product/{product_id})  
[GET /Product/get-product-by-name/{product_name}](#/Product/get-product-by-name/{product_name})  
[GET /Product/get-statistics/{product_name}](#/Product/get-statistics/{product_name})  


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
    **Content:** `{ name : "Product name", description: "Product description", price: 100.0}`
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ error : "Product with current name exist" }`

* **Sample Call CURL:**

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


<a name="/Products?skip=0&limit=100"><h2>/Products?skip=0&limit=100</h2></a>

----
  Returns array of json data about a products.

* **URL**

  /products/?skip=0&limit=10

* **Method:**

  `GET`
  
*  **QUERY Params**

   **None Required:**
 
   `skip=[integer], by default 0`
   `limit=[integer], by default 100`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[ { id : 1, name : "Product Name", description: "Product description", price: 100.0, datetime: "2023-01-01" } ]`
 
* **Sample Call CURL:**

  ```curl -X 'GET' \
  'https://parserapp.serdar17.repl.co/products/?skip=0&limit=100' \
  -H 'accept: application/json'
  ```


<a name="/Product/{product_id}"><h2>/Products/{product_id}</h2></a>

----
  Returns json data about a product by id.

* **URL**

  /products/{product_id}

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `product_id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, name : "Product Name", description: "Product description", price: 100.0, datetime: "2023-01-01" }`

  * **Code:** 404 NOT FOUND <br />
  **Content:** `{ error : "Product with current id not found" }`
 
* **Sample Call CURL:**

  ```curl -X 'GET' \
  'https://parserapp.serdar17.repl.co/product/2' \
  -H 'accept: application/json'
  ```


<a name="PUT_/Product/{product_id}"><h2>PUT /Product/{product_id}</h2></a>

----
  Returns updated json data about a product by id.

* **URL**

  /products/{product_id}

* **Method:**

  `PUT`
  
*  **URL Params**

   **Required:**
 
   `product_id=[integer]`

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
    **Content:** `{ id : 1, name : "Product Name", description: "Product description", price: 100.0, datetime: "2023-01-01" }`

  * **Code:** 404 NOT FOUND <br />
  **Content:** `{ error : "Product with current id not found" }`
 
* **Sample Call CURL:**

  ```curl -X 'PUT' \
  'https://parserapp.serdar17.repl.co/product/69' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "test name",
  "description": "string",
  "price": 111
  }'
  ```

<a name="DELETE_/Product/{product_id}"><h2>DELETE /Product/{product_id}</h2></a>

----
  Delete json data about a product by id.

* **URL**

  /products/{product_id}

* **Method:**

  `DELETE`
  
*  **URL Params**

   **Required:**
 
   `product_id=[integer]`

* **Data Params**

None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "status": "ok", "message": "Deletion was successful" }`

  * **Code:** 404 NOT FOUND <br />
  **Content:** `{ error : "Product with current id not found" }`
 
* **Sample Call CURL:**

  ```curl -X 'DELETE' \
  'https://parserapp.serdar17.repl.co/product/69' \
  -H 'accept: application/json'
  ```

<a name="/Product/get-product-by-name/{product_name}"><h2>/Product/get-product-by-name/{product_name}</h2></a>

----
  Returns json data about a product by name.

* **URL**

  /products/get-products-by-name/{product_name}

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `product_name=[string]`

* **Data Params**

None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 1, name : "Product Name", description: "Product description", price: 100.0, datetime: "2023-01-01" }`

  * **Code:** 404 NOT FOUND <br />
  **Content:** `{ error : "Product with current name not found" }`
 
* **Sample Call CURL:**

  ```curl -X 'GET' \
  'https://parserapp.serdar17.repl.co/product/get-product-by-name/Asus%20VivoBook%20Pro%2015%20OLED%20%20%28i7-12700H%7CRTX3050%29' \
  -H 'accept: application/json'
  ```

<a name="/Product/get-statistics/{product_name}"><h2>/Product/get-statistics/{product_name}</h2></a>

----
  Returns image.png file about price statistics.


* **URL**

  /products/get-products-by-name/{product_name}

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `product_name=[string]`

* **Data Params**

None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `Media type image/png`

  * **Code:** 404 NOT FOUND <br />
  **Content:** `{ error : "Product with current name not found" }`
 
* **Sample Call CURL:**

  ```curl -X 'GET' \
  'https://parserapp.serdar17.repl.co/product/get-statistics/ASUS%20Laptop%20X515%20%28%20i7-1065G7%7CSilver%20%29' \
  -H 'accept: image/png'
  ```
* **RETURNS**

![statistics](https://github.com/Serdar17/Parser/assets/96997312/a46d75d6-f33e-41e4-bde3-d0195c129004)
