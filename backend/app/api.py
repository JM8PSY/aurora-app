from fastapi import APIRouter
from app.models import ObservationConditions
import os
import requests
import json

router = APIRouter()

@router.get("/conditions/{latitude}/{longitude}", response_model=ObservationConditions)
def get_conditions(latitude: float, longitude: float):
    # OpenWeatherMap APIのキーにアクセスできるかまずCHECKする
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    if not OPENWEATHER_API_KEY:
        raise RuntimeError("OPENWEATHER_API_KEY is not set in environment variables")
    
    # OpenWeatherMap APIを呼び出して天候情報を取得
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ja"
    print(f"Fetching weather data from: {url}")

    response = requests.get(url) # API呼び出し
    if response.status_code != 200: # ステータスコードが200でない場合はエラー
        raise RuntimeError(f"Failed to fetch data from OpenWeatherMap: {response.status_code} {response.text}")
    
    data = response.json()
    print(f"Received data: {json.dumps(data, ensure_ascii=False, indent=2)}")

    # NOAAのKp指数
    response_kp = requests.get("https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json")
    if response_kp.status_code != 200:
        raise RuntimeError(f"Failed to fetch Kp index from NOAA: {response_kp.status_code} {response_kp.text}")
    kp_data = response_kp.json()
    print(f"Received Kp index data: {json.dumps(kp_data, ensure_ascii=False, indent=2)}")
    # 最新のKp値を取得
    if len(kp_data) > 1:
        latest_kp = float(kp_data[-1][1])
    else:
        latest_kp = None

    return ObservationConditions(
        cloud_cover= data.get("clouds", {}).get("all", 0), # 雲量（%）
        kp_index_fromNOAA=latest_kp, # 仮の値
        relative_humidity=  data.get("main", {}).get("humidity", 0),# 相対湿度
        visibility_north=True,
        recommendation="北の空が晴れていれば観測チャンス！"
    )
