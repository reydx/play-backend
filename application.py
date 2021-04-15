# -*- coding: UTF-8 -*-
"""
@Summary : 
@Author  : Rey
@Time    : 2020-11-05 11:45
@Log     :
           author datetime(DESC) summary
           Rey  2020-11-05 11:45
"""
from __future__ import absolute_import

import uvicorn
from fastapi import FastAPI

from settings import environment_settings

app = FastAPI()

url_prefix = "/api/v1"


@app.get(url_prefix+"")
async def api_index():
    return {"rey": "to the earth"}


@app.get("/home")
async def home():
    return {"rey": "home"}


@app.get("/")
async def host():
    return {f"{environment_settings.env_name}": "to the earth"}


if __name__ == '__main__':
    # uvicorn.run(app='application:app', port=4000, host="0.0.0.0", reload=True, reload_dirs=".")
    uvicorn.run(app='application:app', port=4000, host="0.0.0.0", reload=True)
