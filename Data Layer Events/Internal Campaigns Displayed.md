# Internal Campaigns Displayed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "view_promotion",
  "detailed_event": "Internal Campaigns Displayed",
    "ecommerce": {
        "creative_name": "<creative_name>",
        "creative_slot": "<creative_slot>",
        "items": [
            {
                "affiliation": "<affiliation>",
                "coupon": "<coupon>",
                "creative_name": "<creative_name>",
                "currency": "<currency>",
                "discount": <discount>,
                "index": <index>,
                "item_brand": "<item_brand>",
                "item_category": "<item_category>",
                "item_category2": "<item_category2>",
                "item_category3": "<item_category3>",
                "item_category4": "<item_category4>",
                "item_category5": "<item_category5>",
                "item_id": "<item_id>",
                "item_list_id": "<item_list_id>",
                "item_list_name": "<item_list_name>",
                "item_name": "<item_name>",
                "item_variant": "<item_variant>",
                "location_id": "<location_id>",
                "price": <price>,
                "promotion_id": "<promotion_id>",
                "promotion_name": "<promotion_name>",
                "quantity": <quantity>
            }
        ],
        "promotion_id": "<promotion_id>",
        "promotion_name": "<promotion_name>",
        "promotion_objective": "<promotion_objective>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.creative_name|string|Captures the internal campaign creative associated with internal campaigns. Used for internal campaign impressions and clicks only.|Girl with bike, Mountain Top, River Cruise Danube|||||||
|ecommerce.creative_slot|string|Captures the position of an internal campaign on a website page or mobile app screen. Used for internal campaign impressions and clicks only.|1, 5, 78, 3||||1|||
|ecommerce.items[n].affiliation|string|A product affiliation to designate a supplying company or brick and mortar store location.|Google Store|||||||
|ecommerce.items[n].coupon|string|Item-level coupon code used for a purchase.|SUMMER\_FUN|||||||
|ecommerce.items[n].creative_name|string|The name of a creative used in a promotional spot.|summer\_banner2|||||||
|ecommerce.items[n].currency|string|The currency, in 3-letter ISO 4217 format.|USD|||||||
|ecommerce.items[n].discount|number|Monetary value of discount associated with a purchase.|2.22|||||||
|ecommerce.items[n].index|number|The index\/position of the item in a list.|1, 2, 3, 4|||||||
|ecommerce.items[n].item_brand|string|Item brand|Gucci|||||||
|ecommerce.items[n].item_category|string|Item Category \(context-specific\). item\_category2 through item\_category5 can also be used if the item has many categories.|pants|||||||
|ecommerce.items[n].item_category2|string|The second category of an item.||||||||
|ecommerce.items[n].item_category3|string|The third category of an item.||||||||
|ecommerce.items[n].item_category4|string|The fourth category of an item.||||||||
|ecommerce.items[n].item_category5|string|The fifth category of an item.||||||||
|ecommerce.items[n].item_id|string|Item ID \(context-specific\).The product primary ID \(SKU or UPC\)|SKU\_12345|||||||
|ecommerce.items[n].item_list_id|string|The computer-readable machine name of the list the item showed up in \(if sent with a view\_item\_list event\). Use UUID provided by the component if no more specific ID is available.|12345abcde12345|||||||
|ecommerce.items[n].item_list_name|string|The human-readable name of the item list the item showed up in \(if sent with a view\_item\_list event\). If one is not available, populate with numerical index of which list this is on the page \(1-indexed\). For filter\_by\_group component, use that value.|filter\_by\_group, recommended\_products, recently\_viewed\_products|||||||
|ecommerce.items[n].item_name|string|Item Name \(context-specific\).|jeggings|||||||
|ecommerce.items[n].item_variant|string|The variant of the item.|Black|||||||
|ecommerce.items[n].location_id|string|Captures a unique ID of a physical location such as a store, banking branch, atm, hotel, office, or other.|155, 65588, 987764448|||||||
|ecommerce.items[n].price|number|The monetary price of the item, in units of the specified currency parameter.|9.99|||||||
|ecommerce.items[n].promotion_id|string|The ID of a product promotion.|P\_12345|||||||
|ecommerce.items[n].promotion_name|string|The name of a product promotion. One of promotion\_id or promotion name is required.|Summer Sale|||||||
|ecommerce.items[n].quantity|integer|Item quantity.|1|||||||
|ecommerce.promotion_id|string|Captures the ID associated with internal campaigns. Used for internal campaign impressions and clicks only.|2345, 56789, 9876|||||||
|ecommerce.promotion_name|string|Captures the name associated with internal campaigns. Used for internal campaign impressions and clicks only.|Trek bikes for kids, REI Spring Sale 2019, Viking Cruise Fall Specials|||||||
|ecommerce.promotion_objective|string|Captures the objective \(A\/B Test, sale promo\) associated with each internal campaign click and the impact on downstream success or conversion.|Order Starter, Order Value, Newsletter Subscriptions, 12, 33, 44|||||||




