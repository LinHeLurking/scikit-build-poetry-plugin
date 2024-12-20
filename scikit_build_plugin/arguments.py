from ast import iter_fields
from typing import Literal

from cleo.io.inputs.option import Option
from pydantic import BaseModel, model_validator, ConfigDict
from pydantic.fields import FieldInfo, Field


class ScikitBuildArguments(BaseModel):
    model_config = ConfigDict(use_attribute_docstrings=True)

    keep_tmp: bool = Field(default=False, alias="k")
    """Whether to keep temporary directory.
    """

    @classmethod
    def convert_to_cleo_options(cls) -> list[Option]:
        options = []
        for name, field_info in cls.model_fields.items():
            name: str
            field_info: FieldInfo
            opt = Option(name=name, description=field_info.description, flag=field_info.annotation == bool,
                         shortcut=field_info.alias, )
            options.append(opt)
        return options
