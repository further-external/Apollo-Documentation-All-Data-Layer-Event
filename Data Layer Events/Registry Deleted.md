# Registry Deleted

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  "event": "wishlist_delete",
  "detailed_event": "Registry Deleted",
    "ecommerce": {
        "identifier": "<identifier>",
        "type": "<type>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.identifier|string|Captures the ID associated with a gift registry.|12345, 435678, 34567, XCV456, XCV876|||||||
|ecommerce.type|string|Captures the type associated with a gift registry \(i.e. wedding, baby\).|Wedding, Baby, Birth Day, Anniversary|||||||




