from typing import List, Protocol, runtime_checkable, Dict, Any


@runtime_checkable
class Model(Protocol):
    def load(self, path: str):
        ...

    def predict(self, data: List[Dict[str, Any]]):
        ...


class FakeModel(Model):
    def load(self, path: str):
        ...

    def predict(self, datas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        predictions = [{"num": data["data"]} for data in datas]
        return predictions
