import json

from fastapi import FastAPI
from utils.yaml_to_json import YamlToJsonConverter
import os
from pathlib import Path
from api.getvars import router as getvars_router
from uvicorn import run

app = FastAPI()

app.include_router(getvars_router, prefix="/api")


@app.get("/health", summary="Health Check Endpoint")
def health_check():
    return {"status": "healthy"}


def main():
    port = int(os.getenv("PORT", 8070))
    run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
