---
name: spring-initializer
description: Initialize a production-ready Spring Boot project with the required technology stack and project conventions.
category: backend
tags:
  - spring-boot
  - java
  - initializer
  - backend
model: gemma-4-e4b
tools:
  - terminal
  - file
---

# Goal

Initialize a production-ready Spring Boot project using the selected technology stack and predefined project conventions.

# Inputs

The user may provide:

- Spring Boot version
- Java version
- Build tool (Gradle/Maven)
- Group ID
- Artifact ID
- Package name
- Dependencies
- Database
- Project architecture
- Additional libraries

Example:

Spring Boot 3.5
Java 21
Gradle
MariaDB
JPA
Redis
MongoDB
Validation
Spring Security
JWT
QueryDSL

# Output

Generate:

- Spring Boot project
- Build configuration
- Package structure
- Base configuration
- Profiles
- Exception handling
- Logging configuration
- Common modules
- Development environment

The generated project should compile successfully.

# Workflow

1. Analyze requested technology stack.
2. Select compatible dependency versions.
3. Initialize the project.
4. Configure project structure.
5. Configure common infrastructure.
6. Configure development environment.
7. Validate project integrity.

# Rules

- Follow modern Spring Boot conventions.
- Use Java 21.
- Prefer Gradle.
- Enable configuration separation.
- Follow layered architecture.
- Keep the project production-ready.