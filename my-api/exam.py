from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class SkillCreate(BaseModel):
    name: str
    level: str

class Skill(SkillCreate):
    id: int

skills: list[Skill] = [
    Skill(id=1, name="Python — Assert, Pytest, Parametrize", level="intermediate"),
    Skill(id=2, name="Playwright — Form Testing, Screenshot อัตโนมัติ", level="advanced"),
    Skill(id=3, name="API Testing — GET, POST, PUT, DELETE", level="intermediate"),
    Skill(id=4, name="CI/CD — Git, GitHub, GitHub Actions", level="intermediate"),
]
next_id = 5

@app.get("/skills")
def get_skills():
    return skills

@app.get("/skills/{id}")
def get_skill(id: int):
    for skill in skills:
        if skill.id == id:
            return skill
    raise HTTPException(status_code=404, detail="Skill not found")

@app.post("/skills", status_code=201)
def create_skill(skill: SkillCreate):
    global next_id
    new_skill = Skill(id=next_id, **skill.dict())
    skills.append(new_skill)
    next_id += 1
    return new_skill

@app.delete("/skills/{id}", status_code=204)
def delete_skill(id: int):
    global skills
    for skill in skills:
        if skill.id == id:
            skills.remove(skill)
            return
    raise HTTPException(status_code=404, detail="Skill not found")