# Donation Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  "event": "begin_checkout",
  "detailed_event": "Donation Started",
    "ecommerce": {
        "type": "<type>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.type|string|Captures the type of donation made \(i.e. general, tribute\).|Tribute, General, Fundraiser|||||||




