from base64 import decodebytes
import datetime
import io
import json
import time
from django.shortcuts import render, redirect
import requests
from generation.forms import *
from PIL import Image
from pathlib import Path


def set_params(request):
    context = {}
    if request.method == 'POST':
        form = StyleForm(request.POST)

        style = form.data['style']
        frm = form.data['frm']
        quality = form.data['quality'] + ' качество'

        with open('generation/params.txt', 'w') as fl:
            fl.write(f"{style}, {frm}, {quality}")

    context['form'] = StyleForm()
    return render(request, 'set_params.html', context)
    

def characters(request):
    context = {}
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        character = form.data['character']
        action = form.data['action']
        place = form.data['place']
        avoidance = form.data['avoidance']

        with open('generation/params.txt', 'r') as fl:
            params = fl.read()

        with open('generation/prompt.txt', 'w') as fl:
            prompt = f"{character} {action} {place}, постарайся избежать {avoidance}, " + params
            fl.write(prompt)

        return redirect('generation.html')

    context['form'] = CharacterForm()
    return render(request, 'characters.html', context)
    
    

def generation(request):
    yandex_cloud_catalog = "b1glihj9h7pkj7mnd6at"
    yandex_api_key = "AQVNyJRotHlHIhGec5YfWrslmo8tsbsc8eatOf_V"
        
    temperature = 0.3
    seed = int(round(datetime.datetime.now().timestamp()))

    with open('generation/prompt.txt', 'r') as fl:
        prompt = fl.read()

    body = {
        "modelUri": f"art://{yandex_cloud_catalog}/yandex-art/latest",
        "generationOptions": {"seed": seed, "temperature": temperature},
        "messages": [
            {"weight": 1, "text": prompt},
        ],
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {"Authorization": f"Api-Key {yandex_api_key}"}

    response = requests.post(url, headers=headers, json=body)
    response_json = json.loads(response.text)
    operation_id = response_json["id"]

    url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"
    headers = {"Authorization": f"Api-Key {yandex_api_key}"}

    while True:
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        done = response_json["done"]
        if done:
            break
        else:
            time.sleep(2)

    image_data = response_json["response"]["image"]
    image_data = Image.open(io.BytesIO(decodebytes(bytes(response_json["response"]["image"], "utf-8"))))
    url = f"media/image{len(list(Path('/media').iterdir()))}.jpeg"
    image_data.save(url)

    context = {}
    context['url'] = url

    return render(request, "generation.html", context)
