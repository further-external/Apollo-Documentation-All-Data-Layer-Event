# Wishlist Shared

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "share_wishlist",
  "detailed_event": "Wishlist Shared",
    "ecommerce": {
        "currency": "<currency>",
        "identifier": "<identifier>",
        "items": [
            {
                "price": "<price>"
            }
        ],
        "value": "<value>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.currency|string|Specifies the currency to be used. Enables exchange rate calucations at the time of data caputure.|USD, CAD, GBP, CHF|^[A-Z]{3}$|3|3||||
|ecommerce.identifier|string|Captures a unique identifier for each wishlist|12345, 435678, 34567, XCV456, XCV876|||||||
|ecommerce.items[n].price|string|Amount of money associated with products shared from a wishlist.|200, 29.99, 50, 0|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.value|string|Captures the total monetary value of each wishlist.|5, 20, 10.22|^[0-9]*(\.[0-9]{1,2})?$||||||




