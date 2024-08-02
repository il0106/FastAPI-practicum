from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, HTMLResponse

import scr.moex.moex as moex
import scr.chart.charts as charts


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(request: Request, 
                    engine: str = Form(...), 
                    market: str = Form(...), 
                    board: str = Form(...),
                    seccode: str = Form(...),
                    start: str = Form(...),
                    end: str = Form(...),
                    interval: int = Form(...)):

    df = moex.get_moex_data(engine, 
                            market, 
                            board, 
                            seccode, 
                            start=start,
                            end=end, 
                            interval=interval)

    chart_html = charts.candle_chart(df, seccode, True)

    return templates.TemplateResponse("index.html", {"request": request, "chart": chart_html})