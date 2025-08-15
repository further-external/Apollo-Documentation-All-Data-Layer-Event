# Report Completed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "report_complete",
  "detailed_event": "Report Completed",
    "event_data": {
        "time_to_complete": <time_to_complete>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.time_to_complete|integer|Captures how long it took visitors to complete the process of interest.|33, 45, 60, 120||||0|||




