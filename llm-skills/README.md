# oliver-skills

문서(요구사항)로부터 애플리케이션을 생성하는 **스킬 기반 코드 생성 파이프라인**입니다.
문서 분석 → 블루프린트 설계 → 계획 → 백엔드/프론트엔드 생성 → 검증 → 리뷰로 이어집니다.

- **런타임**: Claude Code / Hermes 등 범용 AI 에이전트 (특정 엔진 비의존)
- **대상 스택**: backend(Spring Boot·NestJS·Django 택1, `target_stack.backend` 기본 `spring`) + 클라이언트(웹=Next.js, 데스크톱=Tauri, 모바일=Flutter, `target_stack.clients` 기본 `[web]`)
- **언어 규칙**: 이 README와 문서는 **한국어**, 각 스킬 파일 본문은 **영어**로 통일

---

## 카테고리 요약 (32개 카테고리 · 299 스킬 · 36 폴더)

> `backend`·`frontend`는 계층 하나가 여러 스택/타깃 폴더로 나뉜다(폴더=변형, category=계층).

### 앱 생성·변경 파이프라인 (13 · 172)
| category | 수 | 역할 |
|----------|---:|------|
| orchestrator | 13 | 파이프라인 제어 (직접 코드 생성 안 함; app + data + doc 파이프라인) |
| docs-analyze | 6 | 입력 문서/데이터 파싱 (docx/pptx/xlsx/markdown/pdf/csv) |
| blueprint | 6 | 설계 산출물 (architecture/domain-model/database/api-spec/event-topology) + 스펙 검증기 |
| design | 6 | 디자인 시스템/토큰/플로우 + 스펙 검증기 |
| backend | 60 | 백엔드 — `spring`(20)·`nestjs`(20)·`django`(20), `target_stack.backend`로 택1 |
| frontend | 42 | 클라이언트 — `web`(21)·`desktop`(8)·`mobile`(13), `target_stack.clients`로 선택 |
| validator | 10 | 산출물 검증 (pass/fail + validation_result); 클라이언트별 mobile/desktop 검증기 포함 |
| code-change | 4 | 기존 코드 수정/리팩토링/삭제 (생성 아님; senior-programmer 위임) |
| data-change | 4 | 기존 데이터 증분 수정·참조무결성 삭제 + 자가치유 루프 (seed-data·localization·knowledge-base·data-analysis·audit; 도메인 생성기·검증기 위임) |
| doc-change | 4 | 기존 산문 문서 섹션 개정·교차참조 지킨 삭제 + 자가치유 루프 (docwriting·proposal 대상; 생성기·게이트 위임) |
| spec-change | 3 | 기존 설계 스펙 개정·삭제 + 코드 파급 (blueprint·design; L2↔L3 브리지, code-change·validation 위임) |
| deployment | 3 | CI/CD + 환경설정 (컨테이너 없음) |
| vcs | 13 | git/VCS 운영 — repo init·브랜치·커밋·통합(cherry-pick/merge)·changelog/PR + 커밋린트 (브랜치 안전; **실행형** 계층) |

### 독립 업무 도메인 (9 · 66)
| category | 수 | 역할 |
|----------|---:|------|
| research | 10 | 웹/문서/코드 리서치 (근거·출처) |
| docwriting | 8 | 코드/요구사항 → 문서 |
| audit | 8 | 문서 규정 준수 감사 (검증기 포함) |
| proposal | 7 | RFP → 제안서 (검증기 포함) |
| asset | 7 | 2D 비주얼 에셋 (SVG/스프라이트/플레이스홀더) |
| seed-data | 6 | 시드/목 데이터 |
| data-analysis | 8 | 데이터 분석·리포팅 (검증기 포함) |
| knowledge-base | 7 | 문서 코퍼스 → FAQ/온보딩/용어집 (검증기 포함) |
| localization | 5 | 제품 문자열 현지화 |

### 독립 여가 도메인 (9 · 57)
| category | 수 | 역할 |
|----------|---:|------|
| game-master | 7 | TRPG 세션 준비 |
| story-studio | 7 | 창작 소설 |
| trip-planner | 7 | 여행 계획 (research 재활용) |
| recipe-kitchen | 6 | 집밥/요리 |
| quiz-forge | 6 | 퀴즈/트리비아 |
| fitness-coach | 6 | 운동 계획 (교육용) |
| event-planner | 6 | 파티/모임 호스팅 |
| media-curator | 6 | 영화/도서 큐레이션 (research 재활용) |
| music-curator | 6 | 플레이리스트 큐레이션 (research 재활용) |

### 독립 유틸리티 (1 · 2)
| category | 수 | 역할 |
|----------|---:|------|
| codegen | 2 | 직렬화 페이로드(JSON/XML) → 언어별 타입 모델(DTO/class/interface) + 매핑 (payload-model-generator + kotlin-senior-programmer; 오케스트레이터 없는 단독 유틸리티) |

**합계: 174 + 66 + 57 + 2 = 299 스킬** · 독립 도메인 18개(업무 9 + 여가 9) + 독립 유틸리티 1개 카테고리 → 도메인 상세는 [DOMAINS.md](DOMAINS.md)

---

## 디렉토리 구조

```
oliver-skills/
├── orchestrator/   파이프라인 제어 (app / data-pipeline / doc-pipeline / blueprint / design / feature / execution / validation / remediation / review / project-planner + backend/frontend)
├── docs-analyze/   입력 문서/데이터 파싱 (docx / pptx / xlsx / markdown / pdf / csv)
├── blueprint/      설계 산출물 생성 (architecture / domain-model / database / api-spec / event-topology / validator)  ※ 코드 생성 아님
├── spring/         [backend=spring] Spring Boot 코드 생성 (spring-backend-orchestrator + 도메인/API/보안/이벤트/메시징/캐시/스케줄/배치/마이그레이션/config/observability/notification/file-storage/websocket/api-docs/test) + spring-senior-programmer(구현 위임)
├── nestjs/         [backend=nestjs] NestJS+TypeORM (domain/api/auth/event/messaging/cache/scheduler/queue/migration/config/observability/notification/storage/websocket/api-docs/test) + nestjs-senior-programmer
├── django/         [backend=django] Django+DRF (model/api/auth/signals/celery/cache/scheduler/task/migration/settings/observability/notification/storage/channels/api-docs/test) + django-senior-programmer
├── web/       Next.js 웹 클라이언트 (page/layout/component/form/table/dialog/chart/hook/state/data/api-client/auth/i18n/middleware/theme/toast/realtime/feature) + typescript-senior-programmer(구현 위임)
├── desktop/        Tauri 데스크톱 클라이언트 (shell/native-bridge/storage/updater/packaging/test) — web/* React 재사용, UI 미생성
├── mobile/         Flutter 모바일 클라이언트 (initializer/screen/widget/navigation/state/api-client/storage/theme/form/notification/test) + flutter-senior-programmer(구현 위임) — 자체 UI, design·api-spec 재사용
├── design/         UI/디자인 시스템 (design-tokens / design-system / figma-to-component / validator 등) ※ design-orchestrator가 조율
├── validator/      산출물 검증 (architecture / backend / frontend / integration / security / performance / dependency-license / test)
├── code-change/    기존 코드 수정/리팩토링/삭제 (code-change-orchestrator / code-modifier / code-refactorer / code-remover) — 생성 아님, senior-programmer 위임
├── data-change/    기존 데이터 증분 수정·참조무결성 삭제 + 자가치유 (data-change-orchestrator / data-remediation-orchestrator / data-modifier / data-remover) — seed-data·localization·knowledge-base·data-analysis·audit 대상, 도메인 생성기·검증기 위임
├── doc-change/     기존 산문 문서 섹션 개정·삭제 + 자가치유 (doc-change-orchestrator / doc-remediation-orchestrator / doc-modifier / doc-remover) — docwriting·proposal 대상, 생성기·게이트 위임
├── spec-change/    기존 설계 스펙 개정·삭제 + 코드 파급 (spec-change-orchestrator / spec-modifier / spec-remover) — blueprint·design 대상, L2↔L3 브리지(code-change·validation 위임)
├── deployment/     배포 (컨테이너 없음: deployment-orchestrator / cicd / env-config) — CI/CD + 스크립트 + 환경설정
├── vcs/            git/VCS 운영 (vcs-orchestrator + repo-init/branch/commit/integrate(cherry-pick·merge)/changelog/PR/hooks + repo-state/commit-lint 게이트) — 브랜치 안전, **실행형**(실제 git 실행)
├── codegen/        직렬화 페이로드 → 언어별 타입 모델 (payload-model-generator: JSON/XML → Java·Kotlin·TypeScript·Python DTO/class/interface + 매핑) + kotlin-senior-programmer(구현 위임) — 앱 생성과 독립 유틸리티
├── research/       웹/문서/코드 리서치 파이프라인 (앱 생성과 독립)
├── docwriting/     문서 작성 파이프라인 (outline/draft/api-guide/release-notes/adr/style-check/translate) — 코드→문서, 앱 생성과 독립
├── audit/          문서 규정 준수 감사 파이프라인 (ruleset-loader/clause-extractor/conformance-checker/gap-analyzer/risk-scorer/report/validator) — 문서 평가, 앱 생성과 독립
├── proposal/       RFP→제안서 파이프라인 (rfp-analyzer/scope-definer/effort-estimator/pricing-generator/proposal-drafter/validator) — 사전영업 스코핑, 앱 생성과 독립
├── asset/          2D 에셋 파이프라인 (brief/icon(SVG)/sprite-sheet/placeholder/image-prompt/manifest) — 벡터·절차적 직접 저작, 래스터는 프롬프트 스펙, 앱 생성과 독립
├── seed-data/      시드/목 데이터 파이프라인 (schema-analyzer/mock-record/relationship-linker/export/validator) — 스키마를 데이터로 채움, 앱 생성과 독립
├── data-analysis/  데이터 분석 파이프라인 (profiler/cleaner/analyzer/chart-spec/insight/report/validator) — chart-spec은 web/chart로, 앱 생성과 독립
├── knowledge-base/ 지식베이스 파이프라인 (chunker/indexer/faq/onboarding/glossary/validator) — 코퍼스→지식 아티팩트, 앱 생성과 독립
├── localization/   현지화 파이프라인 (string-extractor/catalog-translator/plural-format/validator) — 번역 카탈로그, 앱 생성과 독립
├── game-master/    [여가] TRPG 세션 준비 (world/npc/quest/encounter/session/consistency) — 앱 생성과 독립
├── story-studio/   [여가] 창작 소설 (premise/character/plot/chapter/style/continuity) — 앱 생성과 독립
├── trip-planner/   [여가] 여행 계획 (destination/itinerary/logistics/budget/packing/feasibility) — research 재활용, 앱 생성과 독립
├── recipe-kitchen/ [여가] 집밥/요리 (pantry/recipe/meal-plan/shopping/nutrition) — 앱 생성과 독립
├── quiz-forge/     [여가] 퀴즈/트리비아 (blueprint/question/distractor/key/fairness) — 앱 생성과 독립
├── fitness-coach/  [여가] 운동 계획 (profiler/program/workout/progression/safety) — 교육용, 앱 생성과 독립
├── event-planner/  [여가] 파티/모임 (brief/theme/menu/run-of-show/feasibility) — 앱 생성과 독립
├── media-curator/  [여가] 영화/도서 큐레이션 (taste/title/recommend/order/fit) — research 재활용, 앱 생성과 독립
├── music-curator/  [여가] 플레이리스트 (taste/track/sequence/annotate/flow) — research 재활용, 앱 생성과 독립
├── _deprecated/    이전 버전 아카이브 (참고용, 신규 규격 아님)
├── _template.md    스킬 작성 템플릿
├── INVENTORY.md    전체 스킬 목록 + 의존성 그래프(DAG) — 참조의 단일 소스
└── DOMAINS.md      앱 생성과 독립된 18개 도메인(업무 9 + 여가 9) 한눈에 보기
```

---

## Frontmatter 규격 (단일 표준)

모든 스킬은 아래 필드만 사용합니다. 엔진 전용 필드(`priority/entrypoint/parallel/timeout/retry`)는 **사용하지 않습니다** (범용 에이전트 이식성 우선).

```yaml
---
name: <kebab-case, 파일명과 반드시 일치>
description: <한 줄. "무엇을 언제 쓰는지"가 드러나게>
version: 1.0.0
category: orchestrator | docs-analyze | blueprint | backend | frontend | design | validator | code-change | data-change | doc-change | spec-change | deployment | vcs | codegen | research | docwriting | audit | proposal | asset | seed-data | data-analysis | knowledge-base | localization | game-master | story-studio | trip-planner | recipe-kitchen | quiz-forge | fitness-coach | event-planner | media-curator | music-curator
tags: [<검색용 키워드…>]
model: inherit
invokes: [<하위 스킬 name…>]   # 오케스트레이터만. DAG의 단일 소스. 없으면 [] 또는 생략
inputs: [<입력 이름…>]
outputs: [<출력 이름…>]
---
```

규칙:
- `name` 값은 **파일명(확장자 제외)과 정확히 일치**해야 한다. (파일명 오타 금지)
- `invokes`에 적는 값은 **실제 존재하는 스킬의 `name`** 이어야 한다. (dangling reference 금지)
- `model`은 오케스트레이터/설계 계층은 `inherit`, 실행 계층도 기본 `inherit` (특정 모델 하드코딩 금지).
- `tags`로 통일한다. `keyword`는 사용하지 않는다.

---

## 본문 섹션 규격

**생성기/오케스트레이터** (영어 본문):

```markdown
# Goal
# Inputs
# Output
# Workflow
# Rules
# Examples   ← 필수. 최소 1개 end-to-end 예시
```

**검증기(validator)** 는 워크플로 대신 검증 규격을 명시:

```markdown
# Goal
# Scope
# Checks
# Pass/Fail Criteria
# Output Schema   ← validation_result 스키마를 반드시 정의
# Examples
```

- 헤딩 레벨은 `#`(H1)로 통일. 파일 최상단 `# <skill-name>` 타이틀은 두지 않음(frontmatter로 대체).
- 모든 섹션에 `# Examples` 필수.

---

## 파이프라인 (Invocation Flow)

```
app-orchestrator
├── docs-analyze/*                     (docx/pptx/xlsx/markdown/pdf)
├── blueprint-orchestrator
│   ├── architecture-generator
│   ├── domain-model-generator
│   ├── database-generator
│   ├── api-spec-generator
│   └── event-topology-generator
├── design-orchestrator                (앱 레벨 1회: tokens+system, +선택 flows/wireframes)
│   ├── design-tokens-generator
│   ├── design-system-generator
│   ├── ux-flow-generator
│   ├── wireframe-generator
│   └── figma-to-component
├── <backend>-initializer / nextjs-initializer   (1회: 스캐폴드; backend=spring/nestjs/django 택1)
├── project-planner
├── feature-orchestrator               (feature 단위 반복)
│   ├── backend-orchestrator
│   ├── frontend-orchestrator          (웹)
│   └── integration-generator          (외부 HTTP 전송; 직접 호출)
├── [클라이언트 확장]                    (target_stack.clients에 따라 선택)
│   ├── desktop-orchestrator           (Tauri: 웹 산출물 래핑; UI 미생성)
│   └── mobile-orchestrator            (Flutter: design+api-spec → 모바일 클라이언트)
├── execution-orchestrator
├── validation-orchestrator
│   └── validator/*                    (architecture/backend/frontend/integration/security/performance/dependency-license/test)
├── remediation-orchestrator           (검증 실패 시 code-change 외과수정 또는 execution 재생성 + validation 루프)
├── review-orchestrator
├── vcs-orchestrator                    (선택: options.init_vcs — 브랜치 안전 커밋/통합/PR, 보호브랜치 직접 안 건드림)
└── deployment-orchestrator            (선택: CI/CD + 스크립트 + 환경설정, 컨테이너 없음)
    ├── cicd-generator
    └── env-config-generator
```

우선순위/순서는 별도 숫자 필드 대신 위 그래프와 `INVENTORY.md`가 정의합니다.

---

## 이전 버전(_deprecated/)에서 고친 것들

- 깨진 참조 제거: `service-generator / validation-generator / openapi-generator / integration-test-generator / test-generator`(→ `spring-test-generator`/`frontend-test-generator`), research의 미존재 검색 스킬 7종 정리.
- 파일명 오타 수정: `nextjs-intializer → nextjs-initializer`, `spring-senoir-programmer → spring-senior-programmer`.
- 파일명↔`name` 불일치 수정: `search-validation → source-validation`.
- frontmatter 4종 분열 → 단일 규격 통일. `author: OpenAI`, `model: gemma-4-e4b`(존재하지 않는 모델) 제거.
- `# Examples` 전 파일 필수화, 검증기 pass/fail·result 스키마 정의.
