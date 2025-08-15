# Listing Sort Order Changed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  "event": "sort_list",
  "detailed_event": "Listing Sort Order Changed",
    "ecommerce": {
        "facets": "<facets>",
        "sort_order": <sort_order>,
        "type": "<type>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.facets|string|Details filters used to refine a listing|sort\~price ascending\|color\~green\|size\~medium|||||||
|ecommerce.sort_order|number|The sort value selected by the user on listings.|high-low, low-high, nearest-farthest, a-z, newest-oldest|||||||
|ecommerce.type|string|Captures the methods that bring users to listings \(i.e. Onsite Search, Top Nav, External Link, Category Landing Page\). Does not update if listings are sorted, filtered, or paginated.|Product, Location, Event, Room, Content|||||||




