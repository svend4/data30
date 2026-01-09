CREATE TABLE reviews (
    id UUID PRIMARY KEY,
    entity_type TEXT NOT NULL,
    entity_id UUID NOT NULL,
    author_id UUID NOT NULL,
    quality_rating SMALLINT NOT NULL CHECK (quality_rating BETWEEN 1 AND 5),
    usefulness_rating SMALLINT NOT NULL CHECK (usefulness_rating BETWEEN 1 AND 5),
    quality_comment TEXT,
    usefulness_comment TEXT,
    legacy_rating SMALLINT CHECK (legacy_rating BETWEEN 1 AND 5),
    legacy_rating_source TEXT,
    status TEXT NOT NULL,
    verified BOOLEAN NOT NULL DEFAULT FALSE,
    verified_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX reviews_entity_idx
    ON reviews (entity_type, entity_id);

CREATE INDEX reviews_author_idx
    ON reviews (author_id);

CREATE INDEX reviews_status_idx
    ON reviews (status);

CREATE INDEX reviews_verified_idx
    ON reviews (verified);

CREATE TABLE review_aggregates (
    entity_type TEXT NOT NULL,
    entity_id UUID NOT NULL,
    quality_avg NUMERIC(3, 2) NOT NULL,
    usefulness_avg NUMERIC(3, 2) NOT NULL,
    quality_distribution JSONB NOT NULL,
    usefulness_distribution JSONB NOT NULL,
    review_count INTEGER NOT NULL,
    verified_review_count INTEGER NOT NULL,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (entity_type, entity_id)
);
