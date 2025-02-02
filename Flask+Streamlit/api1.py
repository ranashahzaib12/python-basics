
from flask import Flask , jsonify ,request,render_template

app = Flask(__name__)
# Initial data in the to sdo list
items =[
    {'id':1,'name':'item1' ,'description':'This is item 1'},
    {'id':2,'name':'item2' ,'description':'This is item 2'}
]

@app.route('/')
def home():
    # return "Welcom to the Jome Page"
    return render_template("home1.html") 

@app.route('/items', methods = ['GET'])
def get_items():
     return jsonify(items)
     return render_template("getitems.html")
 
@app.route('/items/<int:item_id>',methods = ["GET"])
def get_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

@app.route('/items' ,methods = ['POST'])
def create_item():
    if not request.jsonify or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item ={
        'id':items[-1]['id'] + 1 if items else 1 ,
        'name':request.json['name'],
        'description':request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>',methods= ['PUT'])
def update_item(item_id):
    item=next((item for item in items if item['id'] == item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    item['name']=request.json.get('name' , item['name'])
    item['description']=request.json.get('description' , item['description'])
    return jsonify(item)



if __name__ == '__main__':
    app.run(debug=True)
