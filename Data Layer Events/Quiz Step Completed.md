# Quiz Step Completed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "survey_step_complete",
  "detailed_event": "Quiz Step Completed",
    "event_data": {
        "name": "<name>",
        "step_name": "<step_name>",
        "step_number": <step_number>,
        "step_value": "<step_value>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.name|string|Captures the human-friendly quiz name.|Floor Chooser, Swim Finder, Movie Decider, My Next Book|||||||
|event_data.step_name|string|Captures the name of the quiz step.|Indoor \/ Outdoor, Durability, Mood|||||||
|event_data.step_number|integer|Captures the number or sequence of quiz steps.|1, 2, 3, 4||||1|||
|event_data.step_value|string|Captures the visitor entry at the time of quiz step completion.|Hardwood, High Traffic, Happy, Fiction|||||||




