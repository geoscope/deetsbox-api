from app.models.base import Base
from sqlalchemy import Column, String, Integer, BigInteger, Boolean, UUID, text


class Repository(Base):
    __tablename__ = "repositories"

    id: UUID = Column(
        "id",
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()"),
    )
    source_id: int = Column("source_id", BigInteger, index=True, nullable=False)
    node_id: str = Column("node_id", String(50), nullable=True)
    name: str = Column("name", String(256), nullable=False)
    full_name: str = Column("full_name", String(512), nullable=True)
    owner_id: UUID = Column("owner_id", UUID(as_uuid=True), nullable=True)
    private: bool = Column(Boolean, nullable=False, default=False)
    html_url: str = Column(String(256), nullable=True)
    description: str = Column(String(512), nullable=True)
    fork: bool = Column(Boolean, nullable=False, default=False)
    url: str = Column(String(256), nullable=True)
    archive_url: str = Column(String(256), nullable=True)
    branches_url: str = Column(String(256), nullable=True)
    collaborators_url: str = Column(String(256), nullable=True)
    commits_url: str = Column(String(256), nullable=True)
    contributors_url: str = Column(String(256), nullable=True)
    issues_url: str = Column(String(256), nullable=True)
    labels_url: str = Column(String(256), nullable=True)
    languages_url: str = Column(String(256), nullable=True)
    merges_url: str = Column(String(256), nullable=True)
    pulls_url: str = Column(String(256), nullable=True)
    releases_url: str = Column(String(256), nullable=True)
    homepage: str = Column(String(256), nullable=True)
    forks_count: int = Column(Integer, nullable=False, default=0)
    forks: int = Column(Integer, nullable=False, default=0)
    watchers_count: int = Column(Integer, nullable=False, default=0)
    watchers: int = Column(Integer, nullable=False, default=0)
    size: int = Column(Integer, nullable=False, default=0)
    default_branch: str = Column(String(128), nullable=True)
    open_issues_count: int = Column(Integer, nullable=False, default=0)
    open_issues: int = Column(Integer, nullable=False, default=0)
    is_template: bool = Column(Boolean, nullable=False, default=False)
    has_issues: bool = Column(Boolean, nullable=False, default=False)
    has_projects: bool = Column(Boolean, nullable=False, default=False)
    has_wiki: bool = Column(Boolean, nullable=False, default=False)
    has_pages: bool = Column(Boolean, nullable=False, default=False)
    has_downloads: bool = Column(Boolean, nullable=False, default=False)
    has_discussions: bool = Column(Boolean, nullable=False, default=False)
    archived: bool = Column(Boolean, nullable=False, default=False)
    disabled: bool = Column(Boolean, nullable=False, default=False)
    visibility: str = Column(String(32), nullable=True)
    pushed_at: str = Column(String(32), nullable=True)
    created_at: str = Column(String(32), nullable=True)
    updated_at: str = Column(String(32), nullable=True)
    allow_rebase_merge: bool = Column(Boolean, nullable=False, default=False)



    is_enabled: bool = Column(Integer, nullable=False, default=False)
    is_deleted: bool = Column(Integer, index=True, nullable=False, default=False)
