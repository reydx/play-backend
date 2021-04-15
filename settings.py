# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2021-04-15 13:49
@Log     :
           author datetime(DESC) summary
           Rey  2021-04-15 13:49  init
"""
from pydantic import BaseSettings


class EnvironmentSettings(BaseSettings):

    env_name: str

    class config:
        case_sensitive = False


environment_settings = EnvironmentSettings()


if __name__ == '__main__':
    environment_settings = EnvironmentSettings()
    print(environment_settings)
