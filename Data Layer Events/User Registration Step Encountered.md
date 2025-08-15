# User Registration Step Encountered

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "registration_step_view",
  "detailed_event": "User Registration Step Encountered",
    "event_data": {
        "step_name": "<step_name>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.step_name|string|Captures the name \/ id of each user registration step encountered.||||||||




