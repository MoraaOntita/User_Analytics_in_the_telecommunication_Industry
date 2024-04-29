import requests

# List of values for PC1 to PC45
pc_values = [-1.341770114256601, -2.338481166732056, 1.9920891593561552, -1.127284208321293, -0.1415896269774047, 0.1538783530310079, 1.432256434521688, -0.448920140322828, 0.0262495416984306, -1.1988917915893496, -1.2096000699984424, -0.3814139698964005, 0.9309581141297704, -0.2242497511379735, -0.0143263099436148, -1.014998522691488, -0.2793470025725173, -0.6583568842655741, 0.1040254300558363, -0.707044994224307, 0.3569036646583723, 0.995164733291133, 0.7452736954294749, 0.5988835988115936, -0.0627418951002569, -0.1478207602505733, -0.0345284807555302, -0.2226607289312226, 0.3950301370632304, -0.2312018531484498, 0.1423310641118556, 0.0503236867222849, -0.0120714616245445, -0.1606714781082032, 0.0729245087182212, 0.0057116329625139, -0.0232954553638986, -0.1603567926720024, -0.0100139993005052, 0.0244054539610034, -0.0267366751031128, -0.0093203704092927, -3.697016617339736e-06, -4.022835777242889e-17, -6.090623541139716e-17]

# Create a dictionary with PC labels as keys and values as the corresponding values
pc_dict = {f'PC{i+1}': value for i, value in enumerate(pc_values)}

# API endpoint URL
url = 'http://localhost:8000/predict/'

# Make a POST request with PC values as data
response = requests.post(url, json=pc_dict)

# Check if the request was successful
if response.status_code == 200:
    # Write the response JSON data to a file
    with open('response.json', 'w') as f:
        f.write(response.text)
    print("Response saved to 'response.json'")
else:
    print("Request failed with status code:", response.status_code)
