# Order Status Checked

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  "event": "check_order_status",
  "detailed_event": "Order Status Checked",
    "ecommerce": {
        "transaction_id": "<transaction_id>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.transaction_id|string|Captures the unique ID associated with the purchase|ABC-132456789, DEF-132456789, 987654567|^[a-zA-Z0-9]{6,20}$|6|20||||




