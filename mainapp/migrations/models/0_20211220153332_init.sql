-- upgrade --
CREATE TABLE IF NOT EXISTS "broadcastuser" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(400) NOT NULL UNIQUE,
    "password" VARCHAR(100) NOT NULL,
    "created" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "active" BOOL NOT NULL  DEFAULT False
);
CREATE INDEX IF NOT EXISTS "idx_broadcastus_usernam_be399d" ON "broadcastuser" ("username");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSONB NOT NULL
);
