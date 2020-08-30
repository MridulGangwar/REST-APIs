from flask import Flask, jsonify, request, render_template	

app  = Flask(__name__)

stores = [
    {   'name':'Vons',
        'items':[
        {
            'name':'Sprouts 2 ply Paper Towels',
            'price':'$7.49'
        }
        ]
    },
    {   'name':'Costco',
        'items':[
        {
            'name':'Kirkland Coconut Water',
            'price':'$11.49'
        }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(stores) 
    
@app.route('/store/<string:name>')
def get_store(name):    
    for store in stores:
        if store['name']==name:
            return jsonify(store)
    return jsonify({'message':'store not found'})
    
@app.route('/store')    
def get_stores():
    return jsonify({'stores':stores})

@app.route('/store/<string:name>/item',methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']==name:
            new_item =  {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return ({'message':'store not found'})
    
@app.route('/store/<string:name>/item')
def get_items_in_store(name):    
    for store in stores:
        if store['name']==name:
            return jsonify({'items':store['items']})
    return ({'message':'store not found'})
    
app.run(port = 5000)
