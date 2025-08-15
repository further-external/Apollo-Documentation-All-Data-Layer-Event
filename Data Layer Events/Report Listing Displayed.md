# Report Listing Displayed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "view_item_list",
  "detailed_event": "Report Listing Displayed",
    "ecommerce": {
        "default_sort_order": "<default_sort_order>",
        "facets": "<facets>",
        "identifier": "<identifier>",
        "items": [
            {
                "index": <index>
            }
        ],
        "listing_context": "<listing_context>",
        "listing_driver": "<listing_driver>",
        "listing_filter_count": <listing_filter_count>,
        "number_of_items": <number_of_items>,
        "number_of_items_displayed": <number_of_items_displayed>,
        "sort_order": <sort_order>,
        "type": "<type>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.default_sort_order|string|The sort value selected by default on listings.|A to Z, Low to High, Newest to Oldest||||0|||
|ecommerce.facets|string|Details filters used to refine a listing|sort\~price ascending\|color\~green\|size\~medium|||||||
|ecommerce.identifier|string|Captures the name or ID of each report.||||||||
|ecommerce.items[n].index|integer|Captures the position of each report in a report listing.|1, 2, 3, 4, 5||||0|||
|ecommerce.listing_context|string|The context in which the listing is displayed \(Onsite Search, Curated Assortment, Navigation\)|Filter Added, Filter Removed, Sort Change, Pagination|||||||
|ecommerce.listing_driver|string||Onsite Search, Curated Assortment, Navigation|||||||
|ecommerce.listing_filter_count|integer|Captures the number of filters applied to a listing.|0, 20, 12||||0|||
|ecommerce.number_of_items|integer|Count of the number of results in a list of reports|1, 21, 111, 166||||0|||
|ecommerce.number_of_items_displayed|integer|Captures the number of reports displayed in a report listing.|10, 20, 30, 40||||0|||
|ecommerce.sort_order|number|The sort value selected by the user on listings.|high-low, low-high, nearest-farthest, a-z, newest-oldest|||||||
|ecommerce.type|string|Captures the methods that bring users to listings \(i.e. Onsite Search, Top Nav, External Link, Category Landing Page\). Does not update if listings are sorted, filtered, or paginated.|Product, Location, Event, Room, Content|||||||




