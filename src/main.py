from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

import moex.moex as moex
import moex.schemas as moex_schemas
import chart.charts as charts


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, form_data: moex_schemas.SMOEX = Depends(moex_schemas.SMOEX.as_form)):

    df = moex.get_moex_data(engine=form_data.engine.name, 
                            market=form_data.market.name, 
                            board=form_data.board.name, 
                            seccode=form_data.seccode, 
                            start=form_data.start,
                            end=form_data.end,
                            interval=form_data.interval.name)

    chart_html = charts.candle_chart(df, form_data.seccode, True)

    return templates.TemplateResponse("index.html", {"request": request, 
                                                     "chart": chart_html})