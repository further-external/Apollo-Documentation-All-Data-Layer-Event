# Chat Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "chat_start",
  "detailed_event": "Chat Started",
    "event_data": {
        "identifier": "<identifier>",
        "method": "<method>",
        "service_line": "<service_line>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.identifier|string|Captures a unique ID associated with each chat session.||||||||
|event_data.method|string|Captures the specific chat portal used.||||||||
|event_data.service_line|string|Captures the specific chat service line used. \(i.e., the agent\)||||||||




