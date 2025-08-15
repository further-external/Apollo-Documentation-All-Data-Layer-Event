# Onsite Search Performed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ event_data: null });  // Clear the previous event_data object.
dataLayer.push({
  "event": "search",
  "detailed_event": "Onsite Search Performed",
    "event_data": {
        "accuracy": "<accuracy>",
        "corrected_term": "<corrected_term>",
        "days_to_start_date": <days_to_start_date>,
        "end_date": "<end_date>",
        "facets": "<facets>",
        "item_id": "<item_id>",
        "latitude": <latitude>,
        "location_id": "<location_id>",
        "longitude": <longitude>,
        "map_vendor": "<map_vendor>",
        "multi_search_entries": "<multi_search_entries>",
        "number_of_adults": <number_of_adults>,
        "number_of_children": <number_of_children>,
        "onsite_search_date_count": <onsite_search_date_count>,
        "people": "<people>",
        "postal_code": "<postal_code>",
        "radius": <radius>,
        "search_term": "<search_term>",
        "start_date": "<start_date>",
        "type": "<type>",
        "unit_of_measure": "<unit_of_measure>",
        "zoom_level": "<zoom_level>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|event_data.accuracy|string|Captures the accuracy of the method that determined the coordinates of the POI \(point of interest\).|high, medium, low|||||||
|event_data.corrected_term|string|Captures the search text used in on-site searches and what the search text was auto-corrected to.|bluth:blu, blue:blu, red lobster:rd lbstr|||||||
|event_data.days_to_start_date|integer|Captures the booking window used in search criteria \(e.g. number of days prior to requested check-in date\).|1, 2, 3, 4, 5||||0|||
|event_data.end_date|string|Captures the end date requested in search criteria.|2022-10-28, 2023-01-15|^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$||||||
|event_data.facets|string|Captures the city\|state\|zip combination that was used to search for a store||||||||
|event_data.item_id|string|Captures the Product Id requested in search criteria.|155, 65588, 987764448|||||||
|event_data.latitude|number|Captures the latitude of the point on map from which distance from POI \(point of interest\) is calculated.|-90, 90, 48.858093|||||||
|event_data.location_id|string|Captures the Location Id requested in search criteria.|155, 65588, 987764448|||||||
|event_data.longitude|number|Captures the longitude of the point on map from which distance from POI \(point of interest\) is calculated.|-180, 180, 2.294694|||||||
|event_data.map_vendor|string|Captures the technology vendor providing the map UI|Google, Bing, Mapquest, ESRI|||||||
|event_data.multi_search_entries|string|The user's fields and values entered for multi-search.|fieldName\~phrase, sku\~12345, product name\~oak\|sku\~12345\|color\~green|||||||
|event_data.number_of_adults|integer|Captures the number of adults entered in search criteria.|1, 2, 3, 4, 5||||1|||
|event_data.number_of_children|integer|Captures the number of children entered in search criteria.|1, 2, 3, 4, 5||||0|||
|event_data.onsite_search_date_count|integer|Captures the number of dates requested in search criteria.|8, 1, 5, 6, 7, 10||||1|||
|event_data.people|string|Captures the number of people entered in search criteria.|1, 2, 3, 4, 5||||1|||
|event_data.postal_code|string|Captures the postal code from which distance from POI \(point of interest\) is calculated.|53533, 30381, M1R 0E9, M3C 0C1|||||||
|event_data.radius|number|Captures the Radius from the POI \(point of interest\) defining the location search area.|2.294694||||0|||
|event_data.search_term|string|Captures the search text used in on-site searches.|bluth, blue, red lobster|||||||
|event_data.start_date|string|Captures the start date requested in search criteria. \(e.g. check-in date\)|2022-10-22, 2023-01-15|^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|0[1-9]|[12][0-9])$||||||
|event_data.type|string|Captures the type of on-site search performed \(i.e., content, product, location, product location, scheduled event, room, report\)|products, properties, articles, authors, coupons, publications|||||||
|event_data.unit_of_measure|string|Captures the ID associated with internal campaigns clicks and see the impact on downstream success or conversion.|miles, kilometers, meters|||||||
|event_data.zoom_level|string|Captures the numeric value representing the zoom level of the map \(i.e. 1, 2, 3, 4\).|1, 2, 3, 4, 5, 6|||||||




