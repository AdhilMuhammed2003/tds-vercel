from flask import Flask, request, jsonify
import json

app = Flask(__name__)


data = [{"name":"y","marks":56},{"name":"z8570CE","marks":25},{"name":"SOammUBr","marks":69},{"name":"1KHEhni6n4","marks":65},{"name":"A","marks":13},{"name":"MoNQCE","marks":80},{"name":"ZWf8","marks":13},{"name":"e","marks":90},{"name":"UrmZRcv","marks":82},{"name":"dp61x1af9f","marks":78},{"name":"Lt","marks":48},{"name":"RH","marks":6},{"name":"ajTYKemPnp","marks":73},{"name":"zoXP2y5ppF","marks":67},{"name":"XDyk","marks":64},{"name":"Y1frQsh","marks":97},{"name":"KlPqj","marks":63},{"name":"DN","marks":70},{"name":"zk5","marks":40},{"name":"qK","marks":10},{"name":"2PRXH8DJGb","marks":53},{"name":"6FOyI","marks":41},{"name":"5fPNpgvX0","marks":2},{"name":"7KnJ0p","marks":34},{"name":"ny4H","marks":3},{"name":"wALXi7PU","marks":18},{"name":"Z","marks":58},{"name":"MTgGqeaA","marks":17},{"name":"4RYOtj0NgZ","marks":84},{"name":"m","marks":27},{"name":"fGZPY","marks":88},{"name":"I857J","marks":64},{"name":"UAchRT7g","marks":93},{"name":"Dswk7vJi","marks":17},{"name":"MMnCug","marks":72},{"name":"0HeZm","marks":14},{"name":"beowm","marks":28},{"name":"sOyk","marks":20},{"name":"c","marks":30},{"name":"ou5","marks":83},{"name":"4ndlRlIa6","marks":6},{"name":"hPoxdGP","marks":11},{"name":"CkYXcSrtY","marks":50},{"name":"0vyWQ","marks":66},{"name":"NSJ9","marks":39},{"name":"6","marks":28},{"name":"gw0hefF1","marks":62},{"name":"CMB","marks":43},{"name":"SqyiL","marks":25},{"name":"EU","marks":55},{"name":"UWMkhs","marks":29},{"name":"ihxcaPelcM","marks":77},{"name":"LVLC","marks":32},{"name":"4V","marks":72},{"name":"ztlAih6r","marks":77},{"name":"I6T0MgHhuE","marks":11},{"name":"x","marks":78},{"name":"Glqg8DmL","marks":22},{"name":"GObpv","marks":43},{"name":"3KcXh","marks":41},{"name":"Xo","marks":50},{"name":"LWG2cO","marks":35},{"name":"bwf","marks":91},{"name":"Zz0hN3ds","marks":33},{"name":"0zYlmpZmx","marks":93},{"name":"LmCUj2","marks":99},{"name":"VPSDUuI","marks":51},{"name":"vGDiFLUO","marks":59},{"name":"cU","marks":37},{"name":"G2NlooHnc","marks":8},{"name":"7m","marks":86},{"name":"oR3mD5ww","marks":42},{"name":"C87","marks":34},{"name":"THpkk","marks":27},{"name":"y","marks":64},{"name":"5","marks":7},{"name":"et","marks":12},{"name":"sY5fNTf4g","marks":98},{"name":"J1SGoKqUTA","marks":96},{"name":"io9TbC","marks":64},{"name":"1","marks":13},{"name":"W","marks":37},{"name":"JDI7ZcS6","marks":45},{"name":"ZC","marks":88},{"name":"Ow","marks":8},{"name":"9Rft","marks":75},{"name":"Ndd1C","marks":77},{"name":"Xe8RWIj0Ls","marks":16},{"name":"7MQ","marks":25},{"name":"wC0","marks":14},{"name":"SZQwkY","marks":57},{"name":"A","marks":46},{"name":"umq","marks":1},{"name":"h2h","marks":0},{"name":"7Jxl3a","marks":76},{"name":"s4pd","marks":41},{"name":"6rZ","marks":27},{"name":"ehZ","marks":22},{"name":"KhyVNFHE","marks":47},{"name":"Gpm","marks":58}]

@app.route('/api', methods=['GET'])
def get_marks():
    # Load data from the JSON file

    # Extract 'name' parameters from the request
    names = request.args.getlist('name')

    # Find marks for the requested names
    marks = [item['marks'] for item in data if item['name'] in names]

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)
