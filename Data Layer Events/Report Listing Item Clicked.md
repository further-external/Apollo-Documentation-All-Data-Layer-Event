# Report Listing Item Clicked

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "select_item",
  "detailed_event": "Report Listing Item Clicked",
    "ecommerce": {
        "facets": "<facets>",
        "identifier": "<identifier>",
        "items": [
            {
                "index": <index>
            }
        ],
        "listing_context": "<listing_context>",
        "listing_driver": "<listing_driver>",
        "sort_order": <sort_order>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.facets|string|Details filters used to refine a listing|sort\~price ascending\|color\~green\|size\~medium|||||||
|ecommerce.identifier|string|Captures the name or ID of each report.||||||||
|ecommerce.items[n].index|integer|Captures the position of each report in a report listing.|1, 2, 3, 4, 5||||0|||
|ecommerce.listing_context|string|The context in which the listing is displayed \(Onsite Search, Curated Assortment, Navigation\)|Filter Added, Filter Removed, Sort Change, Pagination|||||||
|ecommerce.listing_driver|string||Onsite Search, Curated Assortment, Navigation|||||||
|ecommerce.sort_order|number|The sort value selected by the user on listings.|high-low, low-high, nearest-farthest, a-z, newest-oldest|||||||




