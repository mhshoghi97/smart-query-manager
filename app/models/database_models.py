from sqlalchemy import Column, Integer, String, Text, DateTime, JSON, Boolean, Float
from sqlalchemy.sql import func
from app.core.database import Base


# User Query History
class UserQuery(Base):
    __tablename__ = "user_queries"

    id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, index = True)
    query_text = Column(Text, nullable = False)
    query_type = Column(String(50)) # analysis, report, search, etc.


    # AI Analysis
    intent = Column(String(100))
    confidence_score = Column(Float)
    entities = Column(JSON) # Extracted entities
    parameters = Column(JSON) # Query parameters


    # Status
    status = Column(String(50), default = "pending") # pending, processing, completed, failed
    result = Column(JSON) # Final Result


    # Timestamps
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    processed_at = Column(DateTime(timezone = True))
    completed_at = Column(DateTime(timezone = True))



# Data Source Configuration
class DataSource(Base):
    __tablename__ = "data_sources"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100), unique = True)
    type = Column(String(50)) # database, api, file, etc.
    connection_config = Column(JSON) # Connection configuration
    is_active = Column(Boolean, default = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())



# Query Template
class QueryTemplate(Base):
    __tablename__ = "query_templates"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100))
    description = Column(Text)
    template_sql = Column(Text)
    parameters = Column(JSON)
    category = Column(String(50))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())

