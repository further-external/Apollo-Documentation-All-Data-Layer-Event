# Order Placed

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  "event": "purchase",
  "detailed_event": "Order Placed",
    "ecommerce": {
        "affiliation": "<affiliation>",
        "alternate_pickup_person": "<alternate_pickup_person>",
        "cart_id": "<cart_id>",
        "country": "<country>",
        "coupon": "<coupon>",
        "currency": "<currency>",
        "fulfillment_method": "<fulfillment_method>",
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
        "items_purchased_together": "<items_purchased_together>",
        "number_of_payment_methods": <number_of_payment_methods>,
        "order_level_discount": "<order_level_discount>",
        "payment_id": "<payment_id>",
        "payment_type": "<payment_type>",
        "postal_code": "<postal_code>",
        "product_skus_purchased_together": "<product_skus_purchased_together>",
        "revenue_band": "<revenue_band>",
        "sequence": <sequence>,
        "ship_to_country": "<ship_to_country>",
        "ship_to_postal_code": "<ship_to_postal_code>",
        "ship_to_state_or_province": "<ship_to_state_or_province>",
        "shipping": <shipping>,
        "shipping_amount_collected": "<shipping_amount_collected>",
        "shipping_coupon": "<shipping_coupon>",
        "shipping_discount": "<shipping_discount>",
        "shipping_tier": "<shipping_tier>",
        "state_province": "<state_province>",
        "tax": <tax>,
        "tax_amount_collected": "<tax_amount_collected>",
        "transaction_id": "<transaction_id>",
        "value": <value>
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|ecommerce.affiliation|string|A order affiliation to designate a supplying company or brick and mortar store location.|Google Store|||||||
|ecommerce.alternate_pickup_person|string|When a user has put in the information of an alternate pick up person during the checkout process.||||||||
|ecommerce.cart_id|string|Captures the name or ID of the region within which CTA links are used.|12345, 435678, 34567, XCV456, XCV876|||||||
|ecommerce.country|string|Captures the country associated with payments used for a transaction \(i.e. order, booking, dontation, etc.\).|US, CA, FR, UK|^[A-Z]{2}$||||||
|ecommerce.coupon|string|Order-level coupon code used for a purchase.|summer\_fun|||||||
|ecommerce.currency|string|The currency, in 3-letter ISO 4217 format.|USD|||||||
|ecommerce.fulfillment_method|string|Captures the shipping fullfilment method associated with a product.|Shipped, Emailed, Pick Up In Store, Will Call|||||||
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
|ecommerce.items_purchased_together|string||1234\|7878\|9039, abc12\|deh213, abc12|||||||
|ecommerce.number_of_payment_methods|integer|Collects the number of payment methods used for an order at order confirmaton||||||||
|ecommerce.order_level_discount|string|Amount of money discounted for the entire order.|5, 20, 10.22, 19.2|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.payment_id|string|Captures a unique payment ID for a transaction.||ZPH-87698-098||||||
|ecommerce.payment_type|string|Captures the payment methods used for a transaction \(i.e. credit card, Visa, MasterCard, Amex, Paypal, purchase order, etc\).|Credit Card, PayPal, Mastercard, Visa, Amex, Discover|||||||
|ecommerce.postal_code|string|Captures the postal code associated with a transaction \(i.e. order, booking, dontation, etc.\).|53533, 30381, M1R 0E9, M3C 0C1|||||||
|ecommerce.product_skus_purchased_together|string|Captures a concatenated list of product SKU's that are present in the same purchase.|sku123\|sku465, 67890\|87576\|74674, 87, 654|||||||
|ecommerce.revenue_band|string|Captures the revenue dollar amount of the order for use in bucketing orders into specific revenue bands \(i.e. $0-$50, $51-$100\).|125.05, 432.21, 90.22, 12.05|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.sequence|integer|Indicates the sequence of payment application within a transaction|1, 2, 3, 4, 5||||1|||
|ecommerce.ship_to_country|string|Captures the country associated with the shipping address|US, CA, FR, UK|^[A-Z]{2}$||||||
|ecommerce.ship_to_postal_code|string|Captures the postal code for shipping.|53533, 30381, M1R 0E9, M3C 0C1|||||||
|ecommerce.ship_to_state_or_province|string|Captures the state or province associated with the shipping address|WI, GA, NB, ON|||||||
|ecommerce.shipping|number|Shipping cost associated with a transaction.|3.33|||||||
|ecommerce.shipping_amount_collected|string|Captures the amount paid for shipping|15.05, 2, 0.22, 2.2|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.shipping_coupon|string|Captures the code used for the shipping discount|FREESHIPAPRIL, FREESHIP100|||||||
|ecommerce.shipping_discount|string|Captures the amount of discount associated with the shipping cost|5, 20, 10.22, 19.2|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.shipping_tier|string|Captures the shipping method for each product \(i.e. UPS Ground, FedEx Next Day, FedEx Ground, etc.\)|Regular, Overnight, Overnight AM, Overnight AM Sat, UPS Ground, UPS Air|||||||
|ecommerce.state_province|string|Captures the state or province associated with payments used for a transaction \(i.e. order, booking, dontation, etc.\).|WI, GA, NB, ON|||||||
|ecommerce.tax|number|Tax cost associated with a transaction.|1.11|||||||
|ecommerce.tax_amount_collected|string|Captures the amount of tax paid on the order|5.05, 20, 10.22, 9.2|^[0-9]*(\.[0-9]{1,2})?$||||||
|ecommerce.transaction_id|string|The unique identifier of a transaction.|T\_12345, 19283j2nm9jdjs|^[a-zA-Z0-9]{6,20}$|6|20||||
|ecommerce.value|number|The monetary value of the event.|7.77, 239.55, 659|||||||




