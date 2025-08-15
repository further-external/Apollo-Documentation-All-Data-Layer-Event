# User Unsubscribed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "unsubscribe",
  "detailed_event": "User Unsubscribed",
    "event_data": {
        "method": "<method>",
        "type": "<type>"
    },
    "user_data": {
        "user_attributes": "<user_attributes>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.method|string|Captures the website method \(i.e. search, top nav\) used to find each product.|email, facebook, twitter|||||||
|event_data.type|string|Captures the type of subscription \(i.e. email newsletter, SMS text\).|news, updates, sales, events|||||||
|user_data.user_attributes|string|Attributes of the application user|homeStore\~234\|loyaltyTier\~gold\|memberSince\~2002|||||||




