Send a request and returns converted currency

How to use: 
1. Make sure currency_inputs.txt and currency_result.txt exist (feel free to rename but make sure to adjust the code)
2. Run currency_microservice.py
3. Make a request by writing to currency_inputs file
4. Microservice will read the inputs, and make the api call
4. api will return the converted currency, and microservice will write it to currency_result.txt in the format EX: "Converted Amount: 165.59 MXN"

EX: When writing to currency_inputs use something similar to file.write(f"{from_currency}\n{to_currency}\n{amount}\n") in python
[ original currency ]
[ currency we need to convert to ]
[ amount ]
(one input per line, in the above order)


inputs must use ISO 4217 currency codes
Ex:
USD
MXN
10


