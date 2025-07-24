from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    date_time: datetime
    description: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    date_time: datetime
    description: Optional[str] = None
    created_at: datetime
    updated_at: datetime

# Add other schemas as needed (e.g., MedicalRecord, Prescription, etc.)
