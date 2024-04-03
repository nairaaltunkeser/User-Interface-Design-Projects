from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

current_id = 4
sales = [
    {
        "id": 1,
        "salesperson": "James D. Halpert",
        "client": "Shake Shack",
        "reams": 1000
    },
    {
        "id": 2,
        "salesperson": "Stanley Hudson",
        "client": "Toast",
        "reams": 4000
    },
    {
        "id": 3,
        "salesperson": "Michael G. Scott",
        "client": "Computer Science Department",
        "reams": 10000
    },
]
clients = [
 "Shake Shack",
 "Toast",
 "Computer Science Department",
 "Teacher's College",
 "Starbucks",
 "Subsconsious",
 "Flat Top",
 "Joe's Coffee",
 "Max Caffe",
 "Nussbaum & Wu",
 "Taco Bell",
];

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/infinity')
def log_sales():
    print("Clients:", clients)
    return render_template('log_sales.html', sales=sales, clients=clients)

@app.route('/log_sales_page')
def log_sales_page():
    fetched_sales = fetch_sales() 
    return render_template('log_sales.html', sales=fetched_sales, clients=clients)

def fetch_sales():
    return sales

@app.route('/get_clients')
def get_clients():
    return jsonify({'clients': clients})

@app.route('/save_sale', methods=['POST'])
def save_sale():
    global current_id
    global sales
    global clients

    new_sale = request.json
    new_sale['id'] = current_id
    current_id += 1

    sales.append(new_sale)
    if new_sale['client'] not in clients:
        clients.append(new_sale['client'])

    # Return only the updated sales list
    return jsonify({'sales': sales})

@app.route('/delete_sale', methods=['POST'])
def delete_sale():
    global sales

    id_to_delete = request.json['id']
    sales = [sale for sale in sales if sale['id'] != id_to_delete]

    # Return only the updated sales list
    return jsonify({'sales': sales})


if __name__ == '__main__':
    app.run(debug=True)