from flask import Flask, request,jsonify      
import json                            

app = Flask(__name__)
@app.route("/area", methods=["POST"])   

def data_receiver():
    data = request.get_json()           
    json_data = json.dumps(data)  
    obj = json.loads(json_data)
    
    def area(obj):
        shape=obj["geometricShape"].lower()
        if shape =='circle': 
             obj["area"]=setarea_of_circle(obj["radius"])
             return  obj["area"]
        elif(shape =='triangle'):
            obj["area"]=setareac_of_triangle(obj["length"],obj["breadth"])
            return  obj["area"]
        elif(shape =='rectangle'):
           obj["area"]= setareac_of_rectangle(obj["length"],obj["breadth"])
           return  obj["area"]
        else:
            return []
    def setarea_of_circle(r):
        area_circle=3.14*r*r
        return area_circle
    def setareac_of_triangle(b,h):
        area_triangle=0.5*b*h
        return area_triangle
    def setareac_of_rectangle(b,h):
        area_rectangle=b*h
        return area_rectangle 
    area=area(obj)
    
    return jsonify(area)
if __name__ == "__main__":              
    app.run()