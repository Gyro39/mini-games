from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI(title="消消乐")

SCORES_FILE = Path(__file__).parent / "scores.json"

# Static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")


class ScoreRequest(BaseModel):
    score: int


def read_high_score() -> int:
    if SCORES_FILE.exists():
        try:
            data = json.loads(SCORES_FILE.read_text(encoding="utf-8"))
            return data.get("high_score", 0)
        except (json.JSONDecodeError, KeyError):
            pass
    return 0


def write_high_score(score: int) -> None:
    SCORES_FILE.write_text(
        json.dumps({"high_score": score}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


@app.get("/")
async def root():
    return FileResponse(Path(__file__).parent / "static" / "index.html")


@app.get("/api/highscore")
async def get_high_score():
    return {"high_score": read_high_score()}


@app.post("/api/highscore")
async def update_high_score(req: ScoreRequest):
    current = read_high_score()
    if req.score > current:
        write_high_score(req.score)
        return {"high_score": req.score, "updated": True}
    return {"high_score": current, "updated": False}
