import requests

def get_prod():
    s_terms = {
                'action':'process',
                'tagtype_0':'countries',
                'tag_contains_0':'contains',
                'tag_0':'France',
                'tagtype_1':'ingredients',
                'tag_contains_1':'contains',
                'tag_1':'taurine',
                'page_size':500,
                "json": 1
              }

    url = "https://fr.openfoodfacts.org/cgi/search.pl?"
    res = requests.get(url, params=s_terms)

    results = res.json()
    products = results["products"]

    data = []
    data.append( [  "Code", "Nom", "Qté",  "Marque", 
                    "Nutrition", "Nom Générique" 
                 ] )
    for product in products:
        row = [     product["code"], 
                    product["product_name"], 
                    product.get("quantity", ""), 
                    product.get("brands", ""), 
                    product.get("nutrition_grade_fr", ""), 
                    product.get("generic_name", "") 
                ]
        data.append(row)
    return data

def main():
    data = []
    data = get_prod()
    print(data)

if __name__ == '__main__':
    main()
