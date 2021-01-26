# Bank-API

### REST service that can fetch bank details, using the data given in the API’s query parameters.
### Essential Features

- Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
- Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.


### Valid Urls

- GET- /api/branches/autocomplete?q=<>
    - Example : api/branches/autocomplete?q=RTGS&limit=2&offset=0
- GET- /api/branches?q=<>
    - Example : api/branches?q=RTGS&limit=2&offset=0# bank_api
