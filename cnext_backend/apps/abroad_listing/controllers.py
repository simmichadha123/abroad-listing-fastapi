from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from cnext_backend.apps.abroad_listing import models
from cnext_backend.apps.abroad_listing.helpers import common_helper
from cnext_backend.settings import base

router = APIRouter(
    prefix='/api/{version}/study-abroad'
)


@router.get('/detail/{college_id}')
async def collegeDetailAPI(college_id:int, db:Session=Depends(base.get_db)):
    db_college = common_helper.get_college_detail(db, college_id=college_id)
    if db_college is None:
        raise HTTPException(status_code=404, detail='College not found')
    return db_college


