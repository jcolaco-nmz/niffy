# niffy

How to insert a new Invoice:

```
curl --include \
     --request POST \
     --header "Content-Type: application/json" \
     --data-binary "{
    \"date\": \"2016-10-10\",
    \"doc_type\": \"FR\",
    \"company\": {
        \"name\": \"Wild Fortress, Lda.\",
        \"business_name\": \"Wild Fortress\",
        \"address_detail\": \"Rua Ali ao Lado, 34\",
        \"tax_id\": \"999999990\",
        \"postal_code\": \"1000-111\",
        \"country\": \"PT\",
        \"phone\": \"+315123321432\"
    },
    \"lines\": [
        {
            \"code\": \"REF\",
            \"description\": \"Produto ABC\",
            \"unit_of_measure\": \"Uni\",
            \"quantity\": 10.0,
            \"net_total\": 100.0,
            \"tax_payable\": 0.0,
            \"settlement_total\": 0.0
        }
    ],
    \"net_total\": 100.0,
    \"gross_total\": 100.0,
    \"description\": \"Fatura 3421\",
    \"tags\": []
}" \
'http://localhost:8000/invoices'
```