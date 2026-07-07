---
name: domain-generator
description: Generate the complete Domain layer including Entity, Repository, RepositorySupport and Service from business requirements.
category: backend
tags:
  - spring-boot
  - domain
  - entity
  - repository
  - service
model: gemma-4-e4b
tools:
  - file
---

# Goal

Generate the Domain layer for a Spring Boot application based on business requirements and database structure.

The Domain layer should include all persistence and business logic components required for the requested feature.

# Inputs

The user should provide:

- Domain name
- Business requirements
- Database schema (optional)
- Existing Entity (optional)
- Existing project structure (optional)

Example:

Domain: User

Table:

id
name
email
created_at

Requirements:

- Register user
- Update user
- Delete user
- Search user

# Output

Generate:

Entity

Repository

RepositorySupport (if required)

Service

ServiceImpl (if applicable)

The generated domain should be production-ready.

# Workflow

1. Analyze business requirements.
2. Analyze database schema.
3. Design the domain model.
4. Identify required repositories.
5. Design business services.
6. Build a Domain specification.
7. Delegate implementation to `spring-senior-programmer`.
8. Validate generated code consistency.

# Rules

- Generate only required classes.
- Follow DDD-inspired layered architecture.
- Keep Entities persistence-focused.
- Keep Services business-focused.
- Use constructor injection.
- Use Java 21 features when appropriate.
- Follow Spring Data JPA best practices.
- Avoid duplicated logic.
- Generate production-ready code only.