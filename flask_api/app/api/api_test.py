from flask import Blueprint,request,jsonify
# BluePrint參數設定
api_test = Blueprint('api_test', __name__)
# ***********************************************
# Create GET http://IP:5000/
# ***********************************************
@api_test.route('/index',methods=['GET'])
def index():  
  return """
  <h1>Python Flask in Docker!</h1>
  <p>A sample web-app for running Flask inside Docker.</p>
  """

# *****************************************************************************************
# Create POST http://IP:5000/post_name
# json
# Key: name
# Value: Your Name
# *****************************************************************************************
@api_test.route("/post_name", methods=['POST'])
def postMethod():
    value = request.json['name']
    try:
        print("json value : %s " %value)
        return jsonify({"status": 200, "comment": "Hello " + value})
    except:
        return jsonify({"status": 200, "comment": "Hello " + value})