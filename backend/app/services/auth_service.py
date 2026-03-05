"""Authentication service - IMPLEMENTED."""

from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # Truncate to 72 bytes for bcrypt compatibility
    return pwd_context.hash(password[:72])


def verify_password(plain: str, hashed: str) -> bool:
    # Truncate to 72 bytes for bcrypt compatibility
    return pwd_context.verify(plain[:72], hashed)


def create_user(db: Session, user_data: UserCreate):
    """Create a new user. Returns None if email exists."""
    existing = db.query(User).filter(User.email == user_data.email).first()
    if existing:
        return None
    user = User(
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
        full_name=user_data.full_name,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str):
    """Authenticate user by email and password."""
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
