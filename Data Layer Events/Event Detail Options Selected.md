# Event Detail Options Selected

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "select_item_variant",
  "detailed_event": "Event Detail Options Selected",
    "ecommerce": {
        "items": [
            {
                "item_variant": "<item_variant>",
                "quantity": <quantity>
            }
        ]
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.items[n].item_variant|string|Captures the type \(i.e. Adult, Student, Infant, Senior, Family\) associated with a ticket.|Adult, Family, Student, Senior, All Access, General Admission|||||||
|ecommerce.items[n].quantity|integer|Captures the number of tickets associated with an event|1, 2, 3, 4, 5||||1|||




