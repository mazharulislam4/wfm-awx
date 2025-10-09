from typing import Optional, Union
from pydantic import BaseModel
import yaml


class YamlToJsonConverter:
    @staticmethod
    def convert(yaml_content: Union[str, None], file_path: Union[str, None]) -> dict:
        if not yaml_content and not file_path:
            raise ValueError("Either yaml_content or file_path must be provided.")

        if file_path:
            with open(file_path, "r") as file:
                yaml_content = file.read()
        try:
            data = yaml.safe_load(yaml_content or "")
            return data
        except yaml.YAMLError as e:
            raise ValueError(f"Error parsing YAML content: {e}")
