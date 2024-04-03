from flask import Flask
from flask import render_template
import random
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)


current_id = 10
restaurants = {

	"1": {
 	"id": "1",
 	"name": "Leyla Restaurant",
 	"image": "https://www.leylanyc.com/wp-content/uploads/2019/11/img-gallery-1-1024x661.jpg",
 	"location": "123 Main St, New York, NY",
 	"summary": "Leyla Turkish Restaurant offers a rich selection of authentic Turkish dishes, ranging from kebabs to mezes, prepared with traditional recipes and fresh ingredients. Our cozy ambiance and warm hospitality ensure a delightful dining experience for all guests.",
 	"chef": "Chef Mehmet",
 	"menu": ["Mixed Grill Kebab", "Turkish Meze Platter", "Iskender Kebab", "Baklava"],
 	"price_range": "$$ - $$$",
 	"rating": "4.5",
 	"similar_restaurants": ["2", "3", "8"],
 	"cuisine": ["Turkish", "Middle Eastern", "Mediterranean"], 
    "phone":"+1 284 783 2984"
    },

	"2": {
 	"id": "2",
    	"name": "Saray Turkish Restaurant",
    	"image": "https://static01.nyt.com/images/2023/08/16/multimedia/15OFF-cqvt/15OFF-cqvt-superJumbo.jpg",
    	"location": "456 Elm St,  New York, NY",
   	 "summary": "Saray Turkish Restaurant offers a wide range of traditional Turkish dishes with a focus on authenticity and flavor. Our welcoming atmosphere and attentive service make dining with us an enjoyable experience.",
    	"chef": "Chef Ayşe",
    	"menu": ["Adana Kebab", "Lamb Shank", "Meze Platter", "Kunefe"],
    	"price_range": "$$ - $$$",
    	"rating": "4.3",
    	"similar_restaurants": ["1", "3", "7"],
    	"cuisine": ["Turkish", "Middle Eastern"],
        "phone":"+1 285 358 3984"
 	},
	

	"3": {
 	"id": "3",
    	"name": "Babylon Mediterranean Bar",
    	"image": "https://www.miamiculinarytours.com/wp-content/uploads/2023/06/unnamed1.webp",
    	"location": "789 Maple St,  New York, NY",
    	"summary": "Babylon Mediterranean Bar offers a fusion of Turkish and Mediterranean cuisine in a vibrant setting. Our menu features a variety of kebabs, mezes, and seafood dishes, all made with the freshest ingredients.",
    	"chef": "Chef Fatih",
    	"menu": ["Lamb Adana Kebab", "Seafood Platter", "Moussaka", "Baklava"],
    	"price_range": "$$ - $$$",
    	"rating": "4.4",
    	"similar_restaurants": ["1", "2", "5"],
   	 "cuisine": ["Turkish", "Mediterranean"],
        "phone":"+1 285 678 3984"
 	},
	"4": {
 	"id": "4",
    	"name": "Sultana Turkish Restaurant",
    	"image": "https://media-cdn.tripadvisor.com/media/photo-s/13/35/b5/10/very-cozy-dining-area.jpg",
    	"location": "1010 Oak St,  New York, NY",
    	"summary": "Sultana Turkish Restaurant offers a diverse selection of traditional Turkish dishes served in an elegant and cozy atmosphere. From appetizers to desserts, our menu showcases the rich flavors of Turkish cuisine.",
    	"chef": "Chef Selim",
    	"menu": ["Chicken Shish Kebab", "Turkish Pide", "Manti", "Kazandibi"],
    	"price_range": "$$ - $$$",
    	"rating": "4.6",
    	"similar_restaurants": ["2", "5", "6"],
    	"cuisine": ["Turkish", "Middle Eastern"],
        "phone":"+1 285 358 3464"
 	},
	"5": {
 	"id": "5",
    	"name": "Mazi Turkish Restaurant",
    	"image": "https://static01.nyt.com/images/2016/01/17/nyregion/17DINELI1/17DINELI1-articleLarge.jpg?quality=75&auto=webp&disable=upscale",
    	"location": "111 Pine St,  New York, NY",
    	"summary": "Mazi Turkish Restaurant offers a delightful array of traditional Turkish dishes with a modern twist. Our cozy ambiance and friendly service create the perfect setting for enjoying authentic Turkish cuisine.",
    	"chef": "Chef Cem",
    	"menu": ["Turkish Breakfast", "Lahmacun", "Doner Kebab", "Kunefe"],
    	"price_range": "$$ - $$$",
    	"rating": "4.3",
    	"similar_restaurants": ["1", "4", "7"],
    	"cuisine": ["Turkish", "Middle Eastern"],
        "phone":"+1 285 358 3274"
 	},
	"6": {
 	"id": "6",
    	"name": "Istanbul Meze",
    	"image": "https://media-cdn.tripadvisor.com/media/photo-s/16/c6/99/af/sicak-ortam.jpg",
    	"location": "212 Oakwood Ave,  New York, NY",
    	"summary": "Istanbul Meze offers a diverse menu of Turkish delights, from classic kebabs to fresh seafood dishes. Our warm atmosphere and authentic flavors transport diners to the heart of Istanbul.",
    	"chef": "Chef Hasan",
    	"menu": ["Mixed Grill Platter", "Seafood Casserole", "Lamb Moussaka", "Baklava"],
    	"price_range": "$$ - $$$",
    	"rating": "4.7",
    	"similar_restaurants": ["4", "5", "7"],
    	"cuisine": ["Turkish", "Mediterranean"],
        "phone":"+1 555 358 3984"
 	},
	"7": {
 	"id": "7",
    	"name": "Turquoise Turkish Grill",
    	"image": "https://media-cdn.tripadvisor.com/media/photo-s/0b/bc/be/2f/turquoise-new-york.jpg",
    	"location": "321 Cedar St,  New York, NY",
    	"summary": "Turquoise Turkish Grill offers an authentic Turkish dining experience with a focus on traditional flavors and hospitality. Our menu features a variety of kebabs, mezes, and desserts.",
    	"chef": "Chef Emre",
    	"menu": ["Lamb Shish Kebab", "Vegetarian Moussaka", "Turkish Dumplings", "Baklava"],
    	"price_range": "$$ - $$$",
    	"rating": "4.5",
    	"similar_restaurants": ["3", "5", "6"],
    	"cuisine": ["Turkish", "Middle Eastern"],
        "phone":"+1 285 898 3984"
 	},
	"8": {
 	"id": "8",
    	"name": "Anatolia Turkish Restaurant",
    	"image": "https://images.squarespace-cdn.com/content/v1/53cc1616e4b0f4361f8ace24/1424013976127-YMEU47N3QLBGE246QV69/image-asset.jpeg",
    	"location": "432 Walnut St,  New York, NY",
    	"summary": "Anatolia Turkish Restaurant offers a taste of authentic Turkish cuisine in a cozy and welcoming atmosphere. From savory kebabs to flavorful mezes, our menu has something for everyone.",
    	"chef": "Chef Ali",
    	"menu": ["Chicken Adana Kebab", "Turkish Lentil Soup", "Lahmacun", "Baklava"],
    	"price_range": "$$ - $$$",
    	"rating": "4.3",
    	"similar_restaurants": ["2", "4", "7"],
    	"cuisine": ["Turkish", "Middle Eastern"],
        "phone":"+1 344 458 3984"
 	},

	"9": {
 	"id": "9",
   	"name": "Sultan Garden Turkish Restaurant",
   	"image": "https://20410430.fs1.hubspotusercontent-na1.net/hub/20410430/hubfs/Imported%20sitepage%20images/slide-image.jpg?width=1440&height=900&name=slide-image.jpg",
    	"location": "543 Cedar Lane,  New York, NY",
    	"summary": "Sultan's Garden Turkish Restaurant offers a delightful mix of traditional Turkish flavors and contemporary twists. With a focus on fresh ingredients and expertly crafted dishes, we ensure a memorable dining experience.",
    	"chef": "Chef Murat",
    	"menu": ["Turkish Mixed Grill", "Stuffed Eggplant", "Turkish Delight", "Kadayif"],
    	"price_range": "$$ - $$$",
    	"rating": "4.6",
    	"similar_restaurants": ["1", "5", "8"],
    	"cuisine": ["Turkish", "Mediterranean"],
        "phone":"+1 343 583 1984"
  	},
	"10": {
    	"id": "10",
    	"name": "Bosphorus Turkish Cuisine",
    	"image": "https://whatnowny.com/wp-content/uploads/sites/11/2023/08/ff0dd5_0d103dec38e54aa0ba3167c1b210e3d7mv2.jpg",
    	"location": "654 Grove St,  New York, NY",
    	"summary": "Bosphorus Turkish Cuisine offers a refined dining experience with a menu that celebrates the rich culinary heritage of Turkey. Our dishes are prepared with care and attention to detail, ensuring an unforgettable meal.",
    	"chef": "Chef Aydin",
    	"menu": ["Lamb Kofta", "Octopus Salad", "Chicken Pilav", "Kunefe"],
    	"price_range": "$$ - $$$",
    	"rating": "4.4",
    	"similar_restaurants": ["2", "6", "9"],
    	"cuisine": ["Turkish", "Mediterranean"],
        "phone":"+1 255 683 2984"
  	}
}

# ROUTES

@app.route('/')
def homepage():
    restaurant_3_name = restaurants["3"]["name"]
    restaurant_5_name = restaurants["5"]["name"]
    restaurant_9_name = restaurants["9"]["name"]
    restaurant_3_url = restaurants["3"]["image"]
    restaurant_5_url = restaurants["5"]["image"]
    restaurant_9_url= restaurants["9"]["image"]
    return render_template('homepage.html', restaurants=restaurants, restaurant_3_name=restaurant_3_name, restaurant_5_name=restaurant_5_name, restaurant_9_name=restaurant_9_name)

 
@app.route('/search_results')
def search_results():
    return render_template('search_results.html')  

@app.route('/view/<id>')
def view_item(id):
    # Retrieve item details based on ID
    item = restaurants.get(id)
    if item:
        # Render the view template with item details
        return render_template('view.html', item=item, restaurants=restaurants)
    else:
        # Handle case where item ID is not found
        return "Item not found", 404
    

# AJAX FUNCTIONS

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        location = request.form.get('location')
        summary = request.form.get('summary')
        chef = request.form.get('chef')
        rating = request.form.get('rating')
        price_range = request.form.get('price_range')
        image = request.form.get('image')
        cuisine = request.form.get('cuisine')
        menu = request.form.get('menu')
        phone =request.form.get('phone')

        # Validate form data
        if not name.strip() or not location.strip() or not summary.strip() or not chef.strip() or not phone.strip() or not menu.strip()  or not rating.strip() or not price_range.strip():
            return jsonify(error="All fields are required"), 400

        # Validate rating field (should be a number)
        try:
            float(rating)
        except ValueError:
            return jsonify(error="Rating must be a number"), 400

        # Validate price range field (should only contain dollar signs)
        if not all(char == '$' for char in price_range):
            return jsonify(error="Price range must contain only dollar signs"), 400

        # Convert cuisine and menu strings to lists
        cuisine_list = [c.strip() for c in cuisine.split(',')]
        menu_list = [m.strip() for m in menu.split(',')]
        
        if len(phone) != 12:
            return jsonify(error="Phone number must start with '+' followed by 11 digits with no spaces"), 400
        
        phone_edited = ' '.join([phone[:2], phone[2:5], phone[5:8], phone[8:]])

        # Check if summary contains at least 180 characters
        if len(summary) < 180:
            return jsonify(error="Summary must contain at least 180 characters"), 400

        # Assuming the item is added successfully
        global current_id
        current_id += 1
        new_id = str(current_id)

        # Randomly select similar restaurants
        num_similar = min(3, len(restaurants) - 1)  # Ensure not to select more than the available restaurants
        similar_restaurants = random.sample(list(restaurants.keys()), num_similar)

        new_item = {
            "id": new_id,
            "name": name,
            "location": location,
            "summary": summary,
            "chef": chef,
            "rating": rating,
            "price_range": price_range,
            "image": image,
            "cuisine": cuisine_list,
            "menu": menu_list,
            "similar_restaurants": similar_restaurants,
            "phone": phone_edited
        }
        restaurants[new_id] = new_item

        # Construct the response data
        response_data = {
            "success": True,
            "message": "New item successfully created.",
            "new_id": new_id
        }
        
        return jsonify(response_data)
    else:
        # Handle GET method
        # Here you can return the form template or any other appropriate response
        return render_template('add_item.html')
	
@app.route('/search')
def search():
    query = request.args.get('query', '').strip()

    # Check if the search query contains only whitespace characters
    if not query.strip():
        # Redirect back to the home page or any appropriate page
        return Response(status=204)

    # Continue with regular search logic
    results = []
    for restaurant in restaurants.values():
        # Check if the query is in the restaurant name, chef name, or menu
        if (query.lower() in restaurant['name'].lower() or 
            query.lower() in restaurant['chef'].lower() or
            any(query.lower() in item.lower() for item in restaurant['menu'])):
            results.append(restaurant)

    if results:
        message = f"Showing Results for \"{query}\""
    else:
        message = "No results found"

    return render_template('search_results.html', results=results, message=message, search_text=query)
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_item(id):
    # Retrieve item details based on ID
    item = restaurants.get(id)
    if item:
        if request.method == 'POST':
            # Update item details based on user input
            item['name'] = request.form.get('name')
            item['location'] = request.form.get('location')
            item['summary'] = request.form.get('summary')
            item['chef'] = request.form.get('chef')
            item['rating'] = request.form.get('rating')
            item['price_range'] = request.form.get('price_range')
            item['image'] = request.form.get('image')
            item['phone'] = request.form.get('phone')
            item['cuisine'] = request.form.get('cuisine')
            item['menu'] = request.form.get('menu')
            item['cuisine'] = request.form.get('cuisine').split(',') if request.form.get('cuisine') else []
            item['menu'] = request.form.get('menu').split(',') if request.form.get('menu') else []
            
            # Redirect to the view page after saving changes
            return redirect(url_for('view_item', id=id))
        else:
            # Convert cuisine and menu lists to strings for pre-population
            return render_template('edit.html', item=item)
    else:
        # Handle case where item ID is not found
        return "Item not found", 404

if __name__ == '__main__':
   app.run(debug = True)




