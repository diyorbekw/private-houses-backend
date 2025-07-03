from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.db.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .admin.study_form import StudyForm
    from .admin.study_lenguage import StudyLanguage
    from .admin.study_direction import StudyDirection
    from .user import User
    from .application import Application

class StudyInfo(Base):
    __tablename__ = "study_info"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    study_direction_id: Mapped[int] = mapped_column(ForeignKey("study_directions.id"))
    study_form_id: Mapped[int] = mapped_column(ForeignKey("study_forms.id"))
    study_language_id: Mapped[int] = mapped_column(ForeignKey("study_languages.id"))

    user: Mapped["User"] = relationship("User", back_populates="study_info")
    study_direction: Mapped["StudyDirection"] = relationship("StudyDirection", back_populates="study_infos")
    study_form: Mapped["StudyForm"] = relationship("StudyForm", back_populates="study_infos")
    study_language: Mapped["StudyLanguage"] = relationship("StudyLanguage", back_populates="study_infos")
    application: Mapped["Application"] = relationship("Application", back_populates="study_info", uselist=False)

    def __repr__(self):
        return (
            f"<StudyInfo(id={self.id}, user_id={self.user_id}, "
            f"study_direction_id={self.study_direction_id}, "
            f"study_form_id={self.study_form_id}, study_language_id={self.study_language_id})>"
        )

    def __str__(self):
        return (
            f"StudyInfo for User {self.user_id} — "
            f"Direction: {self.study_direction.name if self.study_direction else 'N/A'}, "
            f"Form: {self.study_form.name if self.study_form else 'N/A'}, "
            f"Language: {self.study_language.name if self.study_language else 'N/A'}"
        )
