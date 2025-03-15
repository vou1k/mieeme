import requests
from flask import Flask, request
from jinja2 import Template
from pathlib import Path
import config

app = Flask(__name__, static_url_path="", static_folder="")

TEMPLATE_FILE_PATH = str(Path("template.html"))

def location_by_ip(ip):
    response = requests.get(
        url=f"{config.LOCATOR_API_URL}/v1/locate",
        params={ 'apikey': config.LOCATOR_API_TOKEN },
        json={"ip": [{'address': ip}]}
    )

    return response.json()["location"]
    

@app.route("/location")
def get_location_by_ip():
    ip = request.args.get('ip')

    location = location_by_ip(ip)

    with open(TEMPLATE_FILE_PATH) as f:
        return Template(f.read()).render(
            header=f'Location by ip: {ip}',
            lat=location['point']['lon'],
            lon=location['point']['lat']
        )

@app.route("/my_location", methods=["POST"])
def get_my_location():
    my_ip = requests.get(config.GET_IP_API_URL, params={'format': 'json'}).json()["ip"]

    location = location_by_ip(my_ip)

    with open(TEMPLATE_FILE_PATH) as f:
        return Template(f.read()).render(
            header='My location',
            lat=location['point']['lon'],
            lon=location['point']['lat']
        )


if __name__ == "__main__":
    app.run(config.HOST, config.PORT, debug=True)
