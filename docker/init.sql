-- Create extra schemas
CREATE SCHEMA IF NOT EXISTS analytics;

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Comment for History
COMMENT ON DATABASE query_manager IS "Smart Query Manager Database";