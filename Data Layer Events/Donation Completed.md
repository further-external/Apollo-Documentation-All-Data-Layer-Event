# Donation Completed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "purchase",
  "detailed_event": "Donation Completed",
    "ecommerce": {
        "affiliation": "<affiliation>",
        "city": "<city>",
        "coupon": "<coupon>",
        "currency": "<currency>",
        "items": [
            {
                "affiliation": "<affiliation>",
                "coupon": "<coupon>",
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
                "quantity": <quantity>
            }
        ],
        "payment_frequency": "<payment_frequency>",
        "payment_id": "<payment_id>",
        "payment_type": "<payment_type>",
        "postal_code": "<postal_code>",
        "sequence": <sequence>,
        "shipping": <shipping>,
        "state_province": "<state_province>",
        "tax": <tax>,
        "thank_you_card_type": "<thank_you_card_type>",
        "transaction_id": "<transaction_id>",
        "type": "<type>",
        "value": <value>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.affiliation|string|A order affiliation to designate a supplying company or brick and mortar store location.|Google Store|||||||
|ecommerce.city|string|Captures the city associated with a payment.|Atlanta, New York, Los Angeles, Chicago|||||||
|ecommerce.coupon|string|Order-level coupon code used for a purchase.|summer\_fun|||||||
|ecommerce.currency|string|The currency, in 3-letter ISO 4217 format.|USD|||||||
|ecommerce.items[n].affiliation|string|A product affiliation to designate a supplying company or brick and mortar store location.|Google Store|||||||
|ecommerce.items[n].coupon|string|Item-level coupon code used for a purchase.|SUMMER\_FUN|||||||
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
|ecommerce.items[n].location_id|string|The location associated with the event. If possible, set to the Google Place ID that corresponds to the associated item. Can also be overridden to a custom location ID string.|L\_12345|||||||
|ecommerce.items[n].price|number|The monetary price of the item, in units of the specified currency parameter.|9.99|||||||
|ecommerce.items[n].quantity|integer|Item quantity.|1|||||||
|ecommerce.payment_frequency|string|Captures the recurring frequency of donation \(i.e. one-time, monthly\).|One Time, Monthly|||||||
|ecommerce.payment_id|string|Captures a unique payment ID for a transaction.||ZPH-87698-098||||||
|ecommerce.payment_type|string|Captures the payment methods used for a transaction \(i.e. credit card, Visa, MasterCard, Amex, Paypal, purchase order, etc\).|Credit Card, PayPal, Mastercard, Visa, Amex, Discover|||||||
|ecommerce.postal_code|string|Captures the postal code associated with a transaction \(i.e. order, booking, dontation, etc.\).|53533, 30381, M1R 0E9, M3C 0C1|||||||
|ecommerce.sequence|integer|Indicates the sequence of payment application within a transaction|1, 2, 3, 4, 5||||1|||
|ecommerce.shipping|number|Shipping cost associated with a transaction.|3.33|||||||
|ecommerce.state_province|string|Captures the state or province associated with payments used for a transaction \(i.e. order, booking, dontation, etc.\).|WI, GA, NB, ON|||||||
|ecommerce.tax|number|Tax cost associated with a transaction.|1.11|||||||
|ecommerce.thank_you_card_type|string|Captures the type of card requested with a donation \(i.e. email, physical, e-card1, e-card2\).|Electronic, Physical|||||||
|ecommerce.transaction_id|string|The unique identifier of a transaction.|T\_12345, 19283j2nm9jdjs|^[a-zA-Z0-9]{6,20}$|6|20||||
|ecommerce.type|string|Captures the type of donation made \(i.e. general, tribute\).|Tribute, General, Fundraiser|||||||
|ecommerce.value|number|The monetary value of the event.|7.77, 239.55, 659|||||||




