# Content Loaded

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "view_content",
  "detailed_event": "Content Loaded",
    "event_data": {
        "date_modified": "<date_modified>",
        "date_published": "<date_published>",
        "identifier": "<identifier>",
        "licensor": "<licensor>",
        "title": "<title>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.date_modified|string|Captures the last date that content was modified\/updated.|43831, 43498|||||||
|event_data.date_published|string|Captures the publish date of content items \(i.e. article or blog post\).|37247, 40544|^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$||||||
|event_data.identifier|string|Captures the unique ID of content items \(i.e. article or blog post\).||||||||
|event_data.licensor|string|Captures the licensee or owner of content \(i.e. HBO\).|HBO, Disney|||||||
|event_data.title|string|Captures the title associated with website or mobile app content \(i.e. article, blog post\).|50 ways to use jello, Another look at pandas, Year end giving|||||||




