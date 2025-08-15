# Product Interaction Occurred

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  "event": "product_interaction",
  "detailed_event": "Product Interaction Occurred",
    "ecommerce": {
        "interaction_detail": "<interaction_detail>",
        "visualization": "<visualization>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.interaction_detail|string|Captures the interaction detail for an interaction that was performed with a product.|Added to Favorites, Removed from Favorites, Front View, Side View|||||||
|ecommerce.visualization|string|Captures the scene for which a product is being displayed.|Kitchen, Great Room, Bathroom, Bedroom, Custom|||||||




