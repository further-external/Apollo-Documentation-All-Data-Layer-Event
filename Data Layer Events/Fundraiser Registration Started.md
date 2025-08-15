# Fundraiser Registration Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "fundraiser_registration_start",
  "detailed_event": "Fundraiser Registration Started",
    "event_data": {
        "identifier": "<identifier>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.identifier|string|Captures the name or ID associated with each fundraiser.|FT-2019-Chicago, 19-45678, 2019-01-20\_0123|||||||




