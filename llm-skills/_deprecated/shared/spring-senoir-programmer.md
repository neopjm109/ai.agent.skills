---
name: spring-senior-programmer
description: Generate production-ready Spring Boot code following modern Java, Spring, and enterprise development best practices.
category: shared
tags:
  - spring-boot
  - java
  - clean-code
  - implementation
  - backend
model: gemma-4-e4b
tools:
  - file
---

# Goal

Implement production-ready Spring Boot code from the provided design specification.

Focus on implementation quality rather than business analysis.

# Inputs

The user or calling Skill should provide:

- Design specification
- Required classes
- Package structure
- Coding conventions (optional)
- Existing project context (optional)

# Output

Generate complete, compilable Java code.

Examples:

- Entity
- Repository
- RepositorySupport
- Service
- ServiceImpl
- Controller
- Request DTO
- Response DTO
- Mapper
- Configuration
- Exception classes
- Unit tests (when requested)

# Workflow

1. Read the design specification.
2. Understand project architecture.
3. Identify required dependencies.
4. Generate implementation.
5. Apply Spring Boot best practices.
6. Optimize readability and maintainability.
7. Verify consistency.
8. Return production-ready code.

# Rules

## General

- Generate complete compilable code.
- Never generate pseudo code.
- Prefer readability over cleverness.
- Follow SOLID principles.
- Follow Clean Architecture.
- Minimize duplicated code.

## Java

- Use Java 21.
- Prefer Records for immutable DTOs.
- Prefer sealed classes when appropriate.
- Use Optional appropriately.
- Avoid unnecessary null handling.
- Use final whenever possible.

## Spring

- Use constructor injection.
- Avoid field injection.
- Use Spring Boot 3.x conventions.
- Keep Controllers thin.
- Keep Services business-focused.
- Keep Repositories persistence-focused.

## JPA

- Follow Spring Data JPA best practices.
- Avoid N+1 problems.
- Use Fetch Join or EntityGraph when appropriate.
- Use Lazy Loading by default.
- Never expose Entity directly through APIs.

## Transactions

- Apply @Transactional appropriately.
- Keep transaction scope minimal.

## Validation

- Use Jakarta Bean Validation.
- Validate Request DTOs.
- Keep validation outside business logic.

## Exception Handling

- Use Global Exception Handler.
- Create domain-specific exceptions.
- Return consistent error responses.

## Logging

- Use SLF4J.
- Never log sensitive information.
- Log meaningful business events.

## Security

- Never expose passwords.
- Follow Spring Security best practices.
- Prevent common vulnerabilities.

## Performance

- Avoid unnecessary object creation.
- Optimize database access.
- Prefer pagination for collections.

## Naming

- Follow Java naming conventions.
- Use meaningful names.
- Keep methods small and focused.

## Output

Generate production-ready enterprise-quality code only.