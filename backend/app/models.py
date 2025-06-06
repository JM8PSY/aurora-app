from pydantic import BaseModel

class ObservationConditions(BaseModel):
    cloud_cover: int            # 雲量（%）
    kp_index_fromNOAA: int      # NOAAからのKp指数
    relative_humidity: int      # 相対湿度
    visibility_north: bool      # 北側の空が開けているか
    recommendation: str         # 一言アドバイス
