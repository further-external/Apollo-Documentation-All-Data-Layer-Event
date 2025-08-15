# Checkout Interaction Occurred

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "checkout_interaction",
  "detailed_event": "Checkout Interaction Occurred",
    "event_data": {
        "type": "<type>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.type|string|Type of click event engaged with by the user on the checkout page.||||||||




