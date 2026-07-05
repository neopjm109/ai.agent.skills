---
name: domain-model-generator
description: Produce a domain model (aggregates, entities, value objects, domain services, domain events, relationships, invariants) from unified requirements and the architecture design. Use at the blueprint stage after architecture and before database/API design.
version: 1.0.0
category: blueprint
tags:
  - domain
  - ddd
  - model
  - entity
  - aggregate
model: inherit
invokes: []
inputs:
  - unified_requirements
  - architecture_design
outputs:
  - domain_model
---

# Goal

Produce a complete domain model from business requirements and the architecture design:
aggregates, entities, value objects, domain services, domain events, relationships, and
invariants. This is a **design-time skill — it does not generate code**; it emits a
framework-agnostic `domain_model` artifact. No API, persistence, or infrastructure
concerns belong here (those are handled by database-generator, api-spec-generator, and
the backend generators).

# Inputs

```yaml
unified_requirements:
  functional_requirements:
    - id: FR-1
      description: Customers place orders containing multiple items
    - id: FR-2
      description: Payment is captured when an order is placed
  business_rules:
    - id: BR-1
      description: An order total must equal the sum of its item subtotals
    - id: BR-2
      description: An order cannot be modified after payment
architecture_design:
  modules:
    - name: order
      responsibility: order lifecycle
    - name: payment
      responsibility: payment capture
  service_boundaries:
    - module: order
      owns: [Order, OrderItem]
```

# Output

```yaml
domain_model:
  bounded_contexts: [ordering, payment]
  aggregates:
    - name: Order
      root: Order
      entities: [Order, OrderItem]
      value_objects: [Money, Quantity]
  entities:
    - name: Order
      identity: orderId
      attributes: [status, placedAt]
    - name: OrderItem
      identity: orderItemId
      attributes: [productId, quantity, unitPrice]
  value_objects:
    - name: Money
      fields: [amount, currency]
  domain_services:
    - name: PricingService
      responsibility: compute order total from items
  domain_events:
    - name: OrderPlaced
      payload: [orderId, total]
  relationships:
    - from: Order
      to: OrderItem
      type: composition (1..*)
  invariants:
    - id: INV-1
      rule: order.total == sum(item.subtotal)   # refs: BR-1
      refs: [BR-1]
```

# Workflow

## Step 1 — Identify domains and bounded contexts

From requirements and architecture modules, extract core domains, subdomains, and
bounded contexts. Align contexts with the module boundaries in `architecture_design`.

## Step 2 — Define aggregates

Identify aggregate roots and their transactional boundaries. Each aggregate owns its
internal entities and enforces its own invariants.

## Step 3 — Define entities and value objects

Assign identity-bearing entities to their aggregate. Extract immutable concepts
(Money, Email, Address, Status) as value objects.

## Step 4 — Define domain services and events

Capture domain logic that does not belong to a single entity as domain services. Capture
significant business occurrences as domain events (past tense: OrderPlaced,
PaymentCompleted).

## Step 5 — Define relationships and invariants

Define relationships between aggregates and entities (using IDs for cross-aggregate
references). Specify invariants — rules that must always hold — with traceability to
business rules.

# Rules

- Never generate implementation code — emit a design artifact only.
- The domain model must be framework-agnostic: no dependency on the API layer, database
  schema, or infrastructure.
- One aggregate root per transaction boundary; no direct cross-aggregate entity
  mutation — reference other aggregates by ID only.
- Invariants must be enforceable within the domain layer and must not rely on external
  systems.
- Every domain element must reference its requirement, architecture module, or business
  rule (traceability).
- The model is complete only when domains, aggregates, entities, value objects, domain
  events, and invariants are all defined.

# Examples

Input:

```yaml
unified_requirements:
  functional_requirements:
    - id: FR-1
      description: Users register with a unique email
  business_rules:
    - id: BR-1
      description: Email must be unique across all users
architecture_design:
  modules:
    - name: user
      responsibility: registration & profile
```

Output (abridged):

```yaml
domain_model:
  bounded_contexts: [identity]
  aggregates:
    - name: User
      root: User
      entities: [User]
      value_objects: [Email]
  value_objects:
    - name: Email
      fields: [address]
  domain_events:
    - name: UserRegistered
      payload: [userId, email]        # refs: FR-1
  invariants:
    - id: INV-1
      rule: email is unique across the User aggregate set
      refs: [BR-1]
```
