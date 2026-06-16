from re import search

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
import models
from database import engine, get_db

# สร้าง table ใน database อัตโนมัติ
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class SkillCreate(BaseModel):
    name: str
    level: str

class SkillResponse(SkillCreate):
    id: int

    class Config:
        from_attributes = True

@app.get("/skills", response_model=list[SkillResponse])
def get_skills(db: Session = Depends(get_db)):
    return db.query(models.Skill).all()

    # GET /skills/search?keyword=Python
    # ค้นหา skill ที่มีคำนั้นอยู่ใน name
@app.get("/skills/search", response_model=list[SkillResponse])
def search_skills(keyword: str, db: Session = Depends(get_db)):
    return db.query(models.Skill).filter(models.Skill.name.contains(keyword)).all()

@app.get("/skills/{id}", response_model=SkillResponse)
def get_skill(id: int, db: Session = Depends(get_db)):
    skill = db.query(models.Skill).filter(models.Skill.id == id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill

@app.post("/skills", response_model=SkillResponse, status_code=201)
def create_skill(skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = models.Skill(**skill.dict())
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

@app.put("/skills/{id}", response_model=SkillResponse)
def update_skill(id: int, skill: SkillCreate, db: Session = Depends(get_db)):
    db_skill = db.query(models.Skill).filter(models.Skill.id == id).first()
    if not db_skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    for key, value in skill.dict().items():
        setattr(db_skill, key, value)
    db.commit()
    db.refresh(db_skill)
    return db_skill


@app.delete("/skills/{id}")
def delete_skill(id: int, db: Session = Depends(get_db)):
    skill = db.query(models.Skill).filter(models.Skill.id == id).first()
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    db.delete(skill)
    db.commit()
    return {"detail": "Skill deleted"}
    
