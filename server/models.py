"""Module for defining the database models."""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, SmallInteger
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

Base: DeclarativeMeta = declarative_base()


class TimestampMixin:
    """Mixin for adding created_at and updated_at timestamps to a model."""

    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: datetime = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )


class League(Base, TimestampMixin):
    """
    Model for an league
    
    PSL
    2023
    """

    __tablename__ = "leagues"

    id = Column(SmallInteger, primary_key=True, index=True)
    name: str = Column(String, nullable=False, max_length=255)
    logo: str = Column(String, nullable=True, max_length=255)
    country: str = Column(String, nullable=False, max_length=255)
    code: str = Column(String, nullable=False, max_length=3)
    flag: str = Column(String, nullable=False, max_length=255)
    
    def __repr__(self):
        return f"<League: {self.name}>"
    

class Venue(Base, TimestampMixin):
    """Model for a venue."""

    id = Column(SmallInteger, primary_key=True, index=True)
    name: str = Column(String, nullable=False, max_length=255)
    city: str = Column(String, nullable=False, max_length=255)
    country: str = Column(String, nullable=False, max_length=255)
    capacity: int = Column(Integer, nullable=False)
    surface: str = Column(String, nullable=False, max_length=255)
    image: str = Column(String, nullable=True, max_length=255)
    
    def __repr__(self):
        return f"<Venue: {self.name}>"
    
    
class Team(Base, TimestampMixin):
    """Model for a team."""

    id = Column(SmallInteger, primary_key=True, index=True)
    name: str = Column(String, nullable=False, max_length=255)
    logo: str = Column(String, nullable=True, max_length=255)
    league_id: int = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    home_venue_id: int = Column(Integer, ForeignKey("venues.id"), nullable=False)

    league = relationship("Team", backref="leagues", lazy="joined")
    venue = relationship("Team", backref="venues", lazy="joined")
    
    def __repr__(self):
        return f"<Team: {self.name}>"
    
    
class Player(Base, TimestampMixin):
    """Model for a player."""

    id = Column(SmallInteger, primary_key=True, index=True)
    first_name: str = Column(String, nullable=False, max_length=255)
    last_name: str = Column(String, nullable=False, max_length=255)
    image: str = Column(String, nullable=True, max_length=255)
    team_id: int = Column(Integer, ForeignKey("teams.id"), nullable=False)
    position: str = Column(String, nullable=False, max_length=255)
    
    def __repr__(self):
        return f"<Player: {self.first_name} {self.last_name}>"
    
    
class Match(Base, TimestampMixin):
    """Model for a match."""
    
    # enum for status
    class Status:
        SCHEDULED = "scheduled"
        IN_PLAY = "in_play"
        PAUSED = "paused"
        FINISHED = "finished"
        POSTPONED = "postponed"
        SUSPENDED = "suspended"
        CANCELED = "canceled"
        AWARDED = "awarded"
        DELAYED = "delayed"
        UNKNOWN = "unknown"

    id = Column(SmallInteger, primary_key=True, index=True)
    home_team_id: int = Column(Integer, ForeignKey("teams.id"), nullable=False)
    away_team_id: int = Column(Integer, ForeignKey("teams.id"), nullable=False)
    
    venue_id: int = Column(Integer, ForeignKey("venues.id"), nullable=False)
    
    date: datetime = Column(DateTime(timezone=True), nullable=False)
    
    status: str = Column(String, nullable=False, max_length=255)
    
    home_team_score: int = Column(Integer, nullable=False)
    away_team_score: int = Column(Integer, nullable=False)
    home_team_ht_score: int = Column(Integer, nullable=False)
    away_team_ht_score: int = Column(Integer, nullable=False)
    home_team_ft_score: int = Column(Integer, nullable=False)
    away_team_ft_score: int = Column(Integer, nullable=False)

    home_team_et_score: int = Column(Integer, nullable=True)
    away_team_et_score: int = Column(Integer, nullable=True)
    home_team_pen_score: int = Column(Integer, nullable=True)
    away_team_pen_score: int = Column(Integer, nullable=True)

    referee: str = Column(String, nullable=False, max_length=255)
    attendance: int = Column(Integer, nullable=False)
    matchday: int = Column(Integer, nullable=False)
    season: str = Column(String, nullable=False, max_length=255)
    competition: str = Column(String, nullable=False, max_length=255)
    round: str = Column(String, nullable=False, max_length=255)
    group: str = Column(String, nullable=False, max_length=255)
    stage: str = Column(String, nullable=False, max_length=255)
    result: str = Column(String, nullable=False, max_length=255)
    winner: str = Column(String, nullable=False, max_length=255)
    duration: str = Column(String, nullable=False, max_length=255)
    weather: str = Column(String, nullable=False, max_length=255)
    temperature: int = Column(Integer, nullable=False)
    wind_speed: int = Column(Integer, nullable=False)
    wind_direction: str = Column(String, nullable=False, max_length=255)
    humidity: int = Column(Integer, nullable=False)
    pitch: str = Column(String, nullable=False, max_length=255)
    
    def __repr__(self):
        return f"<Match: {self.home_team_id} vs {self.away_team_id}>\
                date: {self.date} status: {self.status}"
    
    
class Coach(Base, TimestampMixin):
    """Model for a coach."""

    id = Column(SmallInteger, primary_key=True, index=True)
    first_name: str = Column(String, nullable=False, max_length=255)
    last_name: str = Column(String, nullable=False, max_length=255)
    image: str = Column(String, nullable=True, max_length=255)
    team_id: int = Column(Integer, ForeignKey("teams.id"), nullable=False)
    
    defv __repr__(self):
        return f"<Coach: {self.first_name} {self.last_name}>"
