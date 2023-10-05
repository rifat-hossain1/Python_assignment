mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
}

i = 0
while i < len(mobile_data["data"]):
    price_USD = float(mobile_data['data'][i]['price'].split()[0])
    price_BDT = price_USD*mobile_data['exchnage_rate']
    print(f"{mobile_data['data'][i]['name']} is made in {mobile_data['data'][i]['made']}. The price is {mobile_data['data'][i]['price']} which is almost equal to {price_BDT:.2f} BDT ")
    i = i+1

