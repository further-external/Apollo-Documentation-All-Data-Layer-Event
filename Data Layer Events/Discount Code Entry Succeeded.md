# Discount Code Entry Succeeded

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "coupon_success",
  "detailed_event": "Discount Code Entry Succeeded",
    "ecommerce": {
        "items": [
            {
                "coupon": "<coupon>"
            }
        ]
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.items[n].coupon|string|Captures the coupon code associated with product level discounts for a transaction. |5OFFSHOES, AKRONCANDLES2019|||||||




