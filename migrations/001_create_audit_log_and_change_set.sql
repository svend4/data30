CREATE TABLE change_set (
    id BIGSERIAL PRIMARY KEY,
    created_by TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    label TEXT,
    metadata JSONB
);

CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id TEXT NOT NULL,
    action TEXT NOT NULL,
    changed_by TEXT NOT NULL,
    changed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    before JSONB,
    after JSONB,
    change_set_id BIGINT REFERENCES change_set(id)
);

CREATE INDEX audit_log_entity_type_entity_id_idx
    ON audit_log (entity_type, entity_id);

CREATE INDEX audit_log_changed_at_idx
    ON audit_log (changed_at);

CREATE INDEX audit_log_change_set_id_idx
    ON audit_log (change_set_id);
