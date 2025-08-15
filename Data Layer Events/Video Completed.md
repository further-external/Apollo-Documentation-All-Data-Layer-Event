# Video Completed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "video_complete",
  "detailed_event": "Video Completed",
    "event_data": {
        "identifier": "<identifier>",
        "type": "<type>",
        "video_duration": <video_duration>,
        "video_provider": "<video_provider>",
        "video_title": "<video_title>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.identifier|string|Captures the ID of video content viewed by visitor.|YT456789, BC4567890, 876546789|||||||
|event_data.type|string|Captures the type of video viewed.||||||||
|event_data.video_duration|integer|Captures the length of the video viewed by the visitor.|36, 67, 178, 600||||0|||
|event_data.video_provider|string|Captures the video player used by the visitor for each video.|youTube, bright cove, JW Player, vimeo|||||||
|event_data.video_title|string|Captures the Name of video content viewed by visitor.|Twitch\_FPS, Age of Empires, Halo|||||||




