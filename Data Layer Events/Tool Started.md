# Tool Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "tool_start",
  "detailed_event": "Tool Started",
    "event_data": {
        "count_tools_started": "<count_tools_started>",
        "identifier": "<identifier>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.count_tools_started|number|Count of times that visitors started using digital tools \(i.e. mortgage calculator\).||||||||
|event_data.identifier|string|Captures the name or ID of the website or mobile app tools \(i.e. mortgage calculator\) used by visitors.|Mortgage Calculator|||||||




