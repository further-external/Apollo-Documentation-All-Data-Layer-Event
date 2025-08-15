# Page Load Started

### 

## Javascript Code
```js
window.dataLayer = window.dataLayer || [];
dataLayer.push({ page_data: null });  // Clear the previous page_data object.
dataLayer.push({
  "event": "page_load_started",
  "detailed_event": "Page Load Started",
    "page_data": {
        "affiliate_id": "<affiliate_id>",
        "breadcrumb": "<breadcrumb>",
        "country": "<country>",
        "day_of_week": "<day_of_week>",
        "email_message_id": "<email_message_id>",
        "email_message_link_id": "<email_message_link_id>",
        "email_recipient_id": "<email_recipient_id>",
        "hour": "<hour>",
        "language": "<language>",
        "name": "<name>",
        "owner": "<owner>",
        "page_hash": "<page_hash>",
        "page_location": "<page_location>",
        "page_name_detailed": "<page_name_detailed>",
        "page_path": "<page_path>",
        "page_query_string": "<page_query_string>",
        "page_title": "<page_title>",
        "page_variant": "<page_variant>",
        "pages_viewed_num_visit": "<pages_viewed_num_visit>",
        "platform_version": "<platform_version>",
        "release_version": "<release_version>",
        "site_country": "<site_country>",
        "site_language": "<site_language>",
        "site_name": "<site_name>",
        "site_section": "<site_section>",
        "site_section2": "<site_section2>",
        "site_section3": "<site_section3>",
        "site_section4": "<site_section4>",
        "site_type": "<site_type>",
        "site_variant": "<site_variant>",
        "type": "<type>",
        "weekday_or_weekend": "<weekday_or_weekend>"
    },
    "user_data": {
        "user_id": "<user_id>"
    }
});
```

## Variable Definitions

|Path|Type|Description|Example|Pattern|Min Length|Max Length|Minimum|Maximum|Multiple Of|
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|page_data.affiliate_id|string|Captures the ID of the affiliate related to a given event||||||||
|page_data.breadcrumb|string|A delimited list of hierarchical sections that describe the current page's location within the navigation of the site.|Home&gt;Women&gt;Tops&gt;Sweaters, Mens - Tops - Sweaters - Supmina, Wool, Rayon, Checkout &gt; Order Thank You|||||||
|page_data.country|string|The country associated with the current page.|US, CA, FR, UK|||||||
|page_data.day_of_week|string|The day of the week the activity occured.||||||||
|page_data.email_message_id|string|Captures the ID associated with a given email message||||||||
|page_data.email_message_link_id|string|Captures the ID associated with the specific link within an email||||||||
|page_data.email_recipient_id|string|Captures the ID of the recipient to whom an email was sent||||||||
|page_data.hour|string|The time of activity at the top of the hour.||||||||
|page_data.language|string|The language of the current page, usually pulled from the &lt;html&gt; tag lang attribute.|en-us, en-gb, ch-cn, fr-ca, fr-fr|||||||
|page_data.name|string|Captures the name of the page the user is on|product - XYZ123, Mens - Tops - Sweaters, Order Confirmation|||||||
|page_data.owner|string|Captures the licensee or owner of content \(i.e. HBO\).|XX product management, marketing, vendor name|||||||
|page_data.page_hash|string|Does the link point to a different domain?||||||||
|page_data.page_location|string|Use this only if you need to report Page URLs different from those that appear in the address bar of the browser, for example redacting PII, providing page paths when none exist for SPAs, etc. Captures the URL of the page currently being viewed. This value will include the full, unaltered URL of the page\/screen the user is currently viewing, including query parameters, fragments, etc., for example https:\/\/www.example.com\/home?user=true&audience=test\#aboutus.|https:\/\/www.example.com\/home?user=true&audience=test\#aboutus|||||||
|page_data.page_name_detailed|string|Captures the full detail of the page the user is on \(usage is flexible\)|product - XYZ123 - super cotton neck scarf, Mens - Tops - Sweaters - Supmina, Wool, Rayon, Order Confirmation - 098fghjkl|||||||
|page_data.page_path|string|Captures the path portion of the page URL.||||||||
|page_data.page_query_string|string|The query string portion of the URL.||||||||
|page_data.page_title|string|The title of the page currently being viewed, generally available in &lt;title&gt;.||||||||
|page_data.page_variant|string|When a feature ramp up is taking place, capture a code to identify users receiving that feature's experience.||||||||
|page_data.pages_viewed_num_visit|string|Running total of how many pages or screens a visitor had viewed at the time they took a website or mobile app action. Count re-starts with each visit.||||||||
|page_data.platform_version|string|The platform used to share content||||||||
|page_data.release_version|string|Captures the version number of the release active on the site||||||||
|page_data.site_country|string|Captures the country associated with website or mobile app activity.|US, CA, FR, UK|^[A-Z]{2}$||||||
|page_data.site_language|string|Captures the language associated with website or mobile app activity.|en-us, en-gb, ch-cn, fr-ca, fr-fr, da|^[a-z]{2}([-]{1}[a-z]{2}){0,1}$||||||
|page_data.site_name|string|Common language used within the business to refer to the website. May be specific County Sites.|Prospecting-EU, Prospecting-US, Member Portal, Shop-CA, Shop-US, Shop-EU|||||||
|page_data.site_section|string|The section of the site that the current page resides in. site\_section2 through site\_section5can also be used if the site has many sections.||||||||
|page_data.site_section2|string|Captures the sub-section of the site where the page being viewed is located|Shop &gt; Kids, Shop &gt; Mens, Shop &gt; Womens|||||||
|page_data.site_section3|string|Captures the website or mobile app sub-sub-section \(two levels below main section\) associated with the page or screen viewed.|Shop &gt; Kids &gt; Tops, Shop &gt; Mens &gt; Shoes|||||||
|page_data.site_section4|string|Captures the website or mobile app sub-sub-sub-section \(three levels below main section\) associated with the page or screen viewed.|Shop &gt; Kids &gt; Tops &gt; Tees, Shop &gt; Mens &gt; Shoes &gt; Oxfords|||||||
|page_data.site_type|string|Common language description of the site type of purpose. May be used to group siteName.|Prospecting, Shop, Members, Brand|||||||
|page_data.site_variant|string|Describes the version of the site that is being shown|Responsive, Mobile, Desktop|||||||
|page_data.type|string|The type of page currently viewed.|home, pdp, article|||||||
|page_data.weekday_or_weekend|string|Whether it was a weekday or weekend when the activity occurred.||||||||
|user_data.user_id|string|The id of the user currently logged in to the site, if the site offers authentication and the user is authenticated.|123456, abc123|||||||




