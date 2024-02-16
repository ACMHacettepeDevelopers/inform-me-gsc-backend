import json
from src.flask_app import app

def test_translate_category():
    with app.test_client() as client:
        # Define the parameters for the request
        category_to_translate = "sports"
        translation_country_code = "TR"

        # Make a GET request to the route
        response = client.get('/translate_category', query_string={
            'category_to_translate': category_to_translate,
            'translation_country_code': translation_country_code
        })

        # Check the response status code
        assert response.status_code == 200

        # Parse the response data as JSON
        data = json.loads(response.data.decode('utf-8'))

        # Check if the translation is correct
        assert 'translated_category' in data
        print(data["translated_category"])

