from flask import Flask, jsonify, request
import yaml

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"Hello World": True})


@app.route("/json-to-yaml", methods=["POST"])
def json_to_yaml():
    data = request.get_json()

    yaml_data = yaml.dump(data)

    return yaml_data, 200, {"Content-Type": "text/yaml"}


@app.route("/yaml-to-json", methods=["POST"])
def yaml_to_json():
    yaml_text = request.data.decode("utf-8")

    data = yaml.safe_load(yaml_text)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5001)