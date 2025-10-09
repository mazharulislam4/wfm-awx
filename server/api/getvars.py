from pathlib import Path
from utils.yaml_to_json import YamlToJsonConverter
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
import json
import os

router = APIRouter()

file_path = Path(Path(__file__).parent.parent.parent, "ansible", "vars", "vars.yml")


@router.get("/get-vars", summary="Get input variables from YAML file")
def get_input_vars():
    try:
        if file_path is None or not file_path.exists():
            return JSONResponse(
                content={"message": "server error", "results": {}},
                status_code=500,
            )
        vars = YamlToJsonConverter.convert(file_path=str(file_path), yaml_content=None)
        if vars is None:
            return JSONResponse(
                content={"message": "No variables found", "results": {}},
                status_code=404,
            )
        varlist = []
        for key, value in vars.items():
            action_name = value.get("name", key)
            itemvars = []
            for varitem in value["vars"]:
                for k, v in varitem.items():
                    itemvars.append({"key": k, "value": v})
            varlist.append({"action_name": action_name, "vars": itemvars})

        return JSONResponse(
            content={"message": "Success", "results": varlist}, status_code=200
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# get var by name
@router.get("/get-var/{action_name}", summary="Get a specific variable by name")
def get_var(action_name: str):
    try:
        if file_path is None or not file_path.exists():
            return JSONResponse(
                content={"message": "server error", "results": {}},
                status_code=500,
            )
        vars = YamlToJsonConverter.convert(file_path=str(file_path), yaml_content=None)
        if vars is None:
            return JSONResponse(
                content={"message": "No variables found", "results": {}},
                status_code=404,
            )
        for key, value in vars.items():
            if "name" in value and value["name"] == action_name:
                var = value
                break
        else:
            var = None
        if var is not None:
            varlist = []
            for varitem in var["vars"]:
                for k, v in varitem.items():
                    varlist.append({"key": k, "value": v})
            return JSONResponse(
                content={
                    "message": "Success",
                    "results": {"action_name": var["name"], "vars": varlist},
                },
                status_code=200,
            )
        return JSONResponse(
            content={"message": "Variable not found", "results": {}},
            status_code=404,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
