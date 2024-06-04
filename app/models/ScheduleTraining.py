from sqlalchemy import Column, String, Integer, ForeignKey
from app.config.database import Base
from sqlalchemy.orm import relationship

class ScheduleTraining(Base):
    __tablename__ = 'ScheduleTraining'
    
    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey('Schedule.id'), nullable=False)
    training_id = Column(Integer, ForeignKey('Training.id'), nullable=False)
    name = Column(String)
    
    schedule = relationship("Schedule", back_populates="scheduleTraining")
    training = relationship("Training", back_populates="scheduleTraining")