import time
import requests

def read_inputs_from_file():
    with open('currency_inputs.txt', 'r') as file:
        lines = file.readlines()
        if len(lines) < 3:
            return None, None, None
        from_currency = lines[0].strip()
        to_currency = lines[1].strip()
        amount = lines[2].strip()
        return from_currency, to_currency, amount

def write_result_to_file(result):
    with open('currency_result.txt', 'w') as file:
        file.write(result)

def convert_currency():
    access_key = '838c76d2-31c7080a-21818f8f-13d38a88' 
    from_currency, to_currency, amount = read_inputs_from_file()

    if not all([from_currency, to_currency, amount]):
        write_result_to_file("Error: Invalid inputs.")
        return

    params = {
        'access_key': access_key,
        'from': from_currency,
        'to': to_currency,
        'amount': amount
    }

    try:
        response = requests.get('http://api.exconvert.com/convert', params=params)
        data = response.json()

        if 'result' in data:
            result = data['result'][to_currency]
            write_result_to_file(f"Converted Amount: {result:.2f} {to_currency}")
        else:
            write_result_to_file("Error: Conversion failed. Check your input parameters.")
    except requests.exceptions.RequestException as e:
        write_result_to_file(f"Error: {str(e)}")

if __name__ == '__main__':
    while True:
        convert_currency()
        time.sleep(10)  # Check for new inputs every 10 seconds
