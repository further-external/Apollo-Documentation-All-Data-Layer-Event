# User Visit Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "custom_session_start",
  "detailed_event": "User Visit Started",
    "ecommerce": {
        "price": "<price>"
    },
    "event_data": {
        "persisted_cart_value": "<persisted_cart_value>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.price|string|Amount of money associated with the product being interacted with|200, 29.99, 50, 0|^[0-9]*(\.[0-9]{1,2})?$||||||
|event_data.persisted_cart_value|string|Amount of money associated with persistent shopping carts at the time visitors signed-in.|125.05, 432.21, 90.22, 12.05|^[0-9]*(\.[0-9]{1,2})?$||||||




