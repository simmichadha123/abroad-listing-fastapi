from sqlalchemy.orm import Session

from cnext_backend.apps.abroad_listing import models



def get_college_detail(db:Session, college_id:int):
    return db.query(models.College).filter(models.College.id == college_id).first()