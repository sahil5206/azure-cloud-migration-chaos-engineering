## Database Decision

SQLite is used for local development to ensure deterministic and
platform-independent execution.

During cloud migration, the application is re-platformed to Azure
and uses Azure Database for PostgreSQL without changing business logic.

This mirrors real-world enterprise development practices.
