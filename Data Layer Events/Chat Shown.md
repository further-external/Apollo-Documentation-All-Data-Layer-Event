# Chat Shown

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "chat_view",
  "detailed_event": "Chat Shown",
    "event_data": {
        "proactive": <proactive>,
        "reactive": <reactive>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.proactive|boolean|Count of times that a user was proactively shown online chat. This represents cases in which a user did not request chat, but was shown chat based upon business rules.|TRUE, FALSE|||||||
|event_data.reactive|boolean|Count of times that a user manually requested to view online chat.|TRUE, FALSE|||||||




