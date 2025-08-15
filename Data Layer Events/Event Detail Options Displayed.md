# Event Detail Options Displayed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "view_item_list",
  "detailed_event": "Event Detail Options Displayed",
    "ecommerce": {
        "items": [
            {
                "item_variant": "<item_variant>",
                "price": "<price>",
                "quantity": <quantity>
            }
        ],
        "number_of_options": <number_of_options>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.items[n].item_variant|string|Captures the type \(i.e. Adult, Student, Infant, Senior, Family\) associated with a ticket.|Adult, Family, Student, Senior, All Access, General Admission|||||||
|ecommerce.items[n].price|string|Captures the per person price. May vary by ticket type.|200, 29.99, 50, 0|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.items[n].quantity|integer|Captures the number of tickets associated with an event|1, 2, 3, 4, 5||||1|||
|ecommerce.number_of_options|integer|Count of times that each event detail option is displayed|1, 3, 5|||||||




