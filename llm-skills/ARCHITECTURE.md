# oliver-skills 아키텍처 & 사용법

문서(요구사항)를 입력받아 검증된 애플리케이션(Spring Boot + Next.js)까지 생성하는
**스킬 기반 코드 생성 파이프라인**의 구조와 사용법을 정리한 문서입니다.

> 참조의 단일 소스는 [INVENTORY.md](INVENTORY.md)(스킬 목록 + 의존성 DAG)와
> [README.md](README.md)(규격)입니다. 이 문서는 그 둘을 아키텍처 관점에서 종합합니다.

---

## 1. 한눈에 보는 개요

- **입력**: 요구사항 문서(docx / pptx / xlsx / markdown / pdf) + 테이블 데이터(csv / tsv)
- **출력**: 검증·리뷰까지 완료된 백엔드/클라이언트(웹·데스크톱·모바일) 소스 + (선택) 배포 산출물
- **런타임**: Claude Code / Hermes 등 범용 AI 에이전트 (특정 엔진 비의존)
- **고정 스택**: backend(Spring Boot·NestJS·Django 택1) + 클라이언트(웹=Next.js, 데스크톱=Tauri, 모바일=Flutter), DB 예: MariaDB
  - backend는 `target_stack.backend`로 선택(기본 `spring`; `nestjs`·`django` 가능)
  - 클라이언트는 `target_stack.clients`로 선택(기본 `[web]`; `desktop`·`mobile` 추가 가능)
- **언어 규칙**: 문서(README/INVENTORY/본 문서)는 한국어, 각 스킬 파일 본문은 영어
- **스킬 총계**: 32개 카테고리, **299개 스킬** (backend=spring/nestjs/django 3폴더, frontend=web/desktop/mobile 3폴더가 각각 한 카테고리)

| 카테고리 | 수 | 역할 |
|----------|----|------|
| orchestrator | 13 | 파이프라인 제어 (직접 코드 생성 안 함; app + data + doc 파이프라인) |
| docs-analyze | 6  | 입력 문서/데이터 파싱 |
| blueprint | 6  | 설계 산출물 생성 (코드 아님) + 스펙 검증기 |
| design | 6  | 디자인 시스템/토큰/플로우 + 스펙 검증기 |
| backend | 60 | 백엔드 코드 생성 — 폴더 3개(spring 20 / nestjs 20 / django 20), `target_stack.backend`로 택1 |
| frontend | 42 | 클라이언트 코드 생성 — 폴더 3개(web 21 / desktop 8 / mobile 13), `target_stack.clients`로 선택 |
| validator | 10 | 산출물 검증 (클라이언트별 mobile/desktop 검증기 포함) |
| code-change | 4  | 기존 코드 수정/리팩토링/삭제 (생성 아님; senior-programmer 위임) |
| data-change | 4  | 기존 데이터 증분 수정·참조무결성 삭제 + 자가치유 루프 (seed-data·localization·knowledge-base·data-analysis·audit; 도메인 생성기·검증기 위임) |
| doc-change | 4  | 기존 산문 문서 섹션 개정·교차참조 지킨 삭제 + 자가치유 루프 (docwriting·proposal; 생성기·게이트 위임) |
| spec-change | 3  | 기존 설계 스펙 개정·삭제 + 코드 파급 (blueprint·design; L2↔L3 브리지, code-change·validation 위임) |
| deployment | 3  | CI/CD + 환경설정 (컨테이너 없음) |
| vcs | 13 | git/VCS 운영 (브랜치 안전; **실행형**: repo init·브랜치·커밋·통합 cherry-pick/merge·changelog/PR·커밋린트) |
| codegen | 2  | 직렬화 페이로드(JSON/XML) → 언어별 타입 모델 + Kotlin 구현 위임 (독립 유틸리티) |
| research | 10 | 웹/문서/코드 리서치 (독립 파이프라인) |
| docwriting | 8  | 코드/요구사항 → 문서 (독립 파이프라인) |
| audit | 8  | 문서 규정 준수 감사 (독립 파이프라인, 검증기 포함) |
| proposal | 7  | RFP → 제안서 (독립 파이프라인, 검증기 포함) |
| asset | 7  | 2D 비주얼 에셋 생성 (독립 파이프라인) |
| seed-data | 6  | 시드/목 데이터 생성 (독립 파이프라인) |
| data-analysis | 8  | 데이터 분석·리포팅 (독립 파이프라인, 검증기 포함) |
| knowledge-base | 7  | 문서 코퍼스 → 지식 아티팩트 (독립 파이프라인, 검증기 포함) |
| localization | 5  | 제품 문자열 현지화 (독립 파이프라인) |
| game-master | 7  | TRPG 세션 준비 (여가, 독립 파이프라인) |
| story-studio | 7  | 창작 소설 (여가, 독립 파이프라인) |
| trip-planner | 7  | 여행 계획 (여가, 독립 파이프라인) |
| recipe-kitchen | 6  | 집밥/요리 (여가, 독립 파이프라인) |
| quiz-forge | 6  | 퀴즈/트리비아 (여가, 독립 파이프라인) |
| fitness-coach | 6  | 운동/트레이닝 (여가, 독립 파이프라인) |
| event-planner | 6  | 파티/모임 호스팅 (여가, 독립 파이프라인) |
| media-curator | 6  | 영화/도서 큐레이션 (여가, 독립 파이프라인) |
| music-curator | 6  | 플레이리스트 큐레이션 (여가, 독립 파이프라인) |

---

## 2. 아키텍처 계층 (Layered Architecture)

스킬은 책임에 따라 4개 계층으로 나뉩니다. 상위 계층은 하위 계층을 **호출(invoke)** 만
하고, 실제 산출물은 하위 계층이 만듭니다.

```
┌───────────────────────────────────────────────────────────────┐
│  L1  제어 계층 (Orchestrator)                                   │
│      app / blueprint / design / feature / backend / frontend   │
│      execution / validation / remediation / review / planner   │
│      → 조율·순서·리포트만. 코드 생성 절대 안 함.                │
├───────────────────────────────────────────────────────────────┤
│  L2  설계 계층 (Blueprint + Design)                             │
│      architecture / domain-model / database / api-spec /       │
│      event-topology  +  design tokens/system/flow/wireframe    │
│      → 계약·스펙·아티팩트. .tsx/.java 코드는 만들지 않음.       │
├───────────────────────────────────────────────────────────────┤
│  L3  생성 계층 (Generator)                                      │
│      backend: spring/* · nestjs/* · django/*                   │
│               (target_stack.backend로 택1)                     │
│      클라이언트: web/* (웹·Next) · desktop/* (Tauri) ·     │
│                 mobile/* (Flutter)                             │
│      → 실제 런타임 코드 생성. senior-programmer에 구현 위임.    │
├───────────────────────────────────────────────────────────────┤
│  L4  검증 계층 (Validator)                                      │
│      architecture / backend / frontend / integration /         │
│      security / performance / dependency-license / test        │
│      → pass/fail + validation_result 스키마 산출.              │
└───────────────────────────────────────────────────────────────┘

  입력 어댑터: docs-analyze/*  (문서 → 통합 요구사항)
  배포 어댑터: deployment/*    (CI/CD + env, 컨테이너 없음)
  운영 계층:   vcs/*           (git/VCS 실행 — 브랜치 안전; 생성 계층과 달리 실제 저장소 상태를 조작)
  별도 도메인: research/*      (앱 생성과 독립된 리서치 파이프라인)
             docwriting/*   (앱 생성과 독립된 문서 작성 파이프라인)
             audit/*        (앱 생성과 독립된 문서 규정 준수 감사 파이프라인)
             proposal/*     (앱 생성과 독립된 RFP→제안서 파이프라인)
             asset/*        (독립 2D 에셋 파이프라인; design→frontend에 이미지 공급)
             seed-data/*    (독립 시드/목 데이터 파이프라인; 앱을 데모 데이터로 채움)
             data-analysis/* (독립 데이터 분석 파이프라인; chart-spec→web/chart)
             knowledge-base/* (독립 지식베이스 파이프라인; 코퍼스→FAQ/온보딩/용어집)
             localization/* (독립 현지화 파이프라인; 카탈로그→web/i18n)
             game-master/*  (여가: TRPG 세션 준비)
             story-studio/* (여가: 창작 소설)
             trip-planner/* (여가: 여행 계획; research 재활용)
             recipe-kitchen/* · quiz-forge/* · fitness-coach/* (여가)
             event-planner/* (여가)
             media-curator/* · music-curator/* (여가; research 재활용)
```

**핵심 원칙**
- 오케스트레이터는 절대 직접 코드를 만들지 않는다 — 오직 위임/순서/리포트.
- 설계(L2) 산출물은 스펙/계약일 뿐, 실제 코드는 생성(L3) 몫.
- 구현 세부는 `spring-senior-programmer` / `typescript-senior-programmer` / `flutter-senior-programmer`에 위임.

---

## 3. 메인 파이프라인 (app-orchestrator)

`app-orchestrator`가 최상위 진입점이며, 아래 순서로 하위 스킬을 호출합니다.

```
app-orchestrator
├─ 1  docs-analyze/*          문서 파싱 → 통합 요구사항
├─ 2  blueprint-orchestrator  아키텍처/도메인/DB/API-spec/이벤트 토폴로지
├─ 2b design-orchestrator     디자인 파운데이션 (tokens+system, 앱당 1회)
├─ 2c <backend>-initializer / 프로젝트 스캐폴드 (feature 루프 이전 1회)
│     nextjs-initializer     backend는 spring/nestjs/django-initializer 중 택1
├─ 3  project-planner         epic/feature/story/task + 의존성 그래프
├─ 4  feature-orchestrator    feature 단위 반복
│     ├─ backend-orchestrator   → backend/* 생성기 팬아웃
│     ├─ frontend-orchestrator  → web/* 생성기 팬아웃 (웹)
│     └─ integration-generator  (외부 HTTP 전송; 직접 호출)
├─ 4b [클라이언트 타깃 확장] target_stack.clients에 따라 선택 실행
│     ├─ desktop-orchestrator   (Tauri: 웹 산출물을 네이티브 쉘로 래핑; UI 미생성)
│     └─ mobile-orchestrator    (Flutter: blueprint+design_system+api_spec → 모바일 클라이언트)
├─ 5  execution-orchestrator  의존성 해소 + 병렬 스케줄
├─ 6  validation-orchestrator validator/* 전부 실행 (리뷰 전 필수)
├─ 7  remediation-orchestrator (검증 실패 시 code-change 외과수정 또는 execution 재생성 + validation 루프)
├─ 8  review-orchestrator     커버리지/제안/잔여 태스크
├─ 8b data-pipeline-orchestrator (선택: options.compose_data — 시드데이터+현지화 채움, data-remediation 자가치유)
├─ 8c doc-pipeline-orchestrator (선택: options.compose_docs — API가이드+릴리스노트 생성, doc-remediation 자가치유)
├─ 8d vcs-orchestrator (선택: options.init_vcs — 브랜치 안전 커밋/통합(cherry-pick·merge)/changelog/PR; 보호브랜치 직접 안 건드림)
└─ 9  deployment-orchestrator (선택: cicd + env-config, 컨테이너 없음)
```

**순서 규칙**
- `design-orchestrator`의 tokens+system은 앱 레벨에서 **1회** 생성 후 전 피처가 재사용.
- 스캐폴드(`*-initializer`)는 feature 루프 **이전 1회**.
- `validation-orchestrator`는 `review-orchestrator` **이전**에 반드시 완료.
- remediation은 `max_remediation_iterations`로 상한. 미해결분은 `remaining_tasks`로 반환.
- 클라이언트 확장(4b)은 웹 feature 루프 완료 후 실행. `desktop`은 완성된 웹 산출물을 재사용하므로 web 이후에만 가능; `mobile`은 blueprint+design_system+api_spec만 있으면 독립적으로 생성.
- deployment는 검증 통과 + 리뷰 완료 후에만 실행(선택).
- vcs(8d)는 생성 이후 실행(선택) — 산출물을 **작업 브랜치**에 커밋/통합하며 보호 브랜치(main/develop)에 직접 커밋·force·history 재작성 안 함. 실제 git을 실행하는 유일한 **운영형** 계층.

---

## 4. 카테고리별 상세

### orchestrator/ (13) — 제어 계층
| 스킬 | 무엇을 호출하나 |
|------|-----------------|
| app-orchestrator | 전 파이프라인(진입점); 선택적으로 data-pipeline / doc-pipeline-orchestrator |
| data-pipeline-orchestrator | 데이터 도메인 5종 + data-remediation-orchestrator (상위 데이터 파이프라인) |
| doc-pipeline-orchestrator | docwriting-orchestrator + doc-remediation-orchestrator (상위 문서 파이프라인) |
| blueprint-orchestrator | architecture / domain-model / database / api-spec / event-topology |
| design-orchestrator | design tokens/system/ux-flow/wireframe/figma-to-component |
| feature-orchestrator | backend-orchestrator / frontend-orchestrator / integration-generator |
| backend-orchestrator | backend/* 16종 생성기 |
| frontend-orchestrator | web/* 19종 생성기 |
| validation-orchestrator | validator/* 10종 (mobile/desktop은 clients 조건부) |
| remediation-orchestrator | code-change-orchestrator(외과수정) + execution(재생성) + validation |
| project-planner / execution-orchestrator / review-orchestrator | (하위 호출 없음) |

### docs-analyze/ (6) — 입력 어댑터
`docx · pptx · xlsx · markdown · pdf` 각각을 파싱해 통합 요구사항으로 변환.
`csv`(=`docs-analyze-csv`, TSV 포함)는 테이블 데이터셋 어댑터로 data-analysis·seed-data가 재활용.

### blueprint/ (6) — 설계 산출물 (코드 아님)
`architecture · domain-model · database · api-spec · event-topology · blueprint-validator`
→ `blueprint-validator`는 스펙 내부 정합(domain↔db↔api↔event↔module)을 pass/fail 검증
(코드 검증 `validator/architecture-validator`와 별개).

### design/ (6) — 디자인 시스템
`design-tokens · design-system · ux-flow · wireframe · figma-to-component · design-validator`
→ `design-orchestrator`가 조율, 산출물을 frontend 생성기에 공급.
`design-validator`는 스펙 내부 정합(component↔token, screen↔component)을 pass/fail 검증.

### backend 멀티스택 — `target_stack.backend`로 택1
세 폴더 `spring/`·`nestjs/`·`django/`는 **모두 `category: backend`** (폴더=스택 변형, category=계층).
`backend-orchestrator`는 **라우터**로, `spring`/`nestjs`/`django` 중 하나의 스택
오케스트레이터에 위임한다. 세 스택 모두 동일한 blueprint(domain-model·database·api-spec·
event-topology) 계약을 입력으로 공유하며, 구현은 각 스택 senior-programmer가 담당.

**spring/ (20) — Spring Boot** (spring)
진입: `spring-backend-orchestrator` · 초기화: `spring-initializer` · 구현: `spring-senior-programmer`
생성기: domain · api · security · event · messaging · redis · scheduler · batch ·
migration · config-properties · observability · notification · file-storage ·
websocket · api-docs · integration · backend-test

**nestjs/ (20) — NestJS + TypeORM** (nestjs)
진입: `nestjs-backend-orchestrator` · 초기화: `nestjs-initializer` · 구현: `nestjs-senior-programmer`
생성기: domain · api · auth · event(EventEmitter2) · messaging · cache · scheduler ·
queue(BullMQ) · migration · config · observability · notification · file-storage ·
websocket(gateway) · api-docs(Nest Swagger) · integration(axios) · test(Jest)

**django/ (20) — Django + DRF** (django)
진입: `django-backend-orchestrator` · 초기화: `django-initializer` · 구현: `django-senior-programmer`
생성기: model · api(DRF) · auth · signals · celery · cache · scheduler(beat) ·
task(mgmt command) · migration · settings · observability · notification · storage ·
channels · api-docs(drf-spectacular) · integration(httpx) · test(pytest)

### web/ (21) — Next.js
초기화: `nextjs-initializer` · 구현 위임: `typescript-senior-programmer`
생성기: page · layout · component · form · table · dialog · chart · hook · state ·
data · api-client · auth · i18n · middleware · theme · toast-notification ·
realtime-client · feature · frontend-test

### desktop/ (8) — Tauri 데스크톱 클라이언트
`desktop-orchestrator`가 진입점. Tauri는 **기존 `web/*` React 산출물을 그대로 래핑**하므로
UI 생성기를 새로 만들지 않고 **네이티브 쉘 계층만** 생성.
스캐폴드 `tauri-initializer` → `desktop-shell-generator`(윈도우/메뉴/트레이) →
`native-bridge-generator`(Rust↔JS IPC command) → `desktop-storage-generator`(로컬 저장) →
`desktop-updater-generator`(자동 업데이트·코드사이닝) → `desktop-packaging-generator`
(dmg/msi/AppImage) → `desktop-test-generator`. 서버 통신은 재사용된 웹 `api-client`가 담당.

### mobile/ (13) — Flutter 모바일 클라이언트
`mobile-orchestrator`가 진입점. **자체 Dart/Flutter UI**를 생성(React 재사용 안 함).
단 `design-tokens` 값(→`flutter-theme-generator`)과 backend `api-spec`(→`flutter-api-client-generator`,
Dio)은 계약으로 재사용. 구현 위임: `flutter-senior-programmer`(Dart 관용구).
스캐폴드 `flutter-initializer` → 생성기: `flutter-screen-generator` · `flutter-widget-generator` ·
`flutter-navigation-generator`(go_router) · `flutter-state-generator`(Riverpod) ·
`flutter-api-client-generator`(Dio+Freezed) · `flutter-storage-generator` · `flutter-theme-generator`(Material 3) ·
`flutter-form-generator` · `flutter-notification-generator`(FCM+로컬) · `flutter-test-generator`.
모든 스킬은 `web/*`와의 이름 충돌 방지를 위해 `flutter-*`/`mobile-*` 접두사.

### validator/ (10) — 검증 계층
`architecture · backend · frontend · mobile · desktop-shell · integration · security · performance ·
dependency-license · test` — 각자 `validation_result` 스키마로 pass/fail 반환.
`mobile-validator`(Flutter/Dart)·`desktop-shell-validator`(Tauri 셸/설정/IPC/패키징)는
`target_stack.clients`에 해당 클라이언트가 있을 때만 실행(웹 React UI는 frontend-validator 소관).

### deployment/ (3) — 배포 (컨테이너 없음)
`deployment-orchestrator · cicd-generator · env-config-generator`
CI/CD 파이프라인 + 스크립트 + 환경별 env 템플릿. 배포 대상은 사용자 인프라에 위임.

### vcs/ (13) — git/VCS 운영 (브랜치 안전, **실행형**)
`vcs-orchestrator`가 진입점(git 직접 실행 안 함, 위임만). 생성 계층과 달리 **실제 git을
실행**하는 유일한 운영 계층이며, 전 스킬이 **브랜치 안전 운영 계약**을 강제한다: 보호
브랜치(main/develop)에 직접 커밋·force-push·history 재작성 금지 · 모든 작업은 작업 브랜치
경유 · stash-안전 · 충돌 시 클린 abort+복구 리포트 · 작업 후 원 브랜치 복귀 · 운영 전
preflight 게이트.
- **게이트(2)**: `repo-state-validator`(상태 preflight) · `commit-lint-validator`(Conventional Commit·브랜치명 준수).
- **플래너(6, git 미실행)**: `branch-strategy-planner` · `commit-message-generator` · `integration-planner` · `changelog-generator` · `pr-description-generator` · `git-hooks-generator`.
- **오퍼레이터(4, git 실행)**: `repo-initializer` · `branch-operator` · `commit-applier` · `branch-integrator`(cherry-pick/merge, 원격+보호target은 PR).
`app-orchestrator`가 `options.init_vcs`로 선택 호출(생성 이후). `changelog-generator`(기계적 로그)는
`docwriting/release-notes-generator`(편집 산문)와, `git-hooks-generator`(로컬 훅)는 `cicd-generator`(CI)와 별개.

### codegen/ (2) — 독립 코드 생성 유틸리티
`payload-model-generator`가 진입 스킬. 구체적인 JSON/XML **응답 샘플**을 입력받아 포맷을
감지하고 스키마(타입·널 가능성·배열·중첩)를 추론해, 요청 언어(Java·Kotlin·TypeScript·
Python)의 타입 모델(DTO/data class/interface)을 **직렬화 매핑**(Jackson·kotlinx.serialization·
class-transformer·Pydantic)까지 포함해 생성. XML은 attribute·child element·wrapper list·
text content를 구분해 매핑. 구현은 언어별 senior-programmer에 위임 — Java→`spring-senior-programmer`,
Kotlin→`kotlin-senior-programmer`(Kotlin 스택 폴더가 없어 codegen이 소유), TypeScript→
`typescript-senior-programmer`, Python→`django-senior-programmer`.
**앱 생성 파이프라인과 독립**이며 blueprint/design 없이 단독 호출 가능. **모델만** 산출하고
엔드포인트·HTTP 클라이언트·OpenAPI는 만들지 않음(§5 API 경계 참조).

### research/ (10) — 독립 리서치 파이프라인
`research-orchestrator`가 진입점. 검색(web/docs/github/news) → web-research →
source-validation → compare-sources → fact-check → summarize.
**앱 생성 파이프라인과 독립적**으로 동작하는 별개 도메인.

### docwriting/ (8) — 독립 문서 작성 파이프라인
`docwriting-orchestrator`가 진입점. (docs-analyze 입력) → outline → 본문 생성
(doc-draft / api-guide / release-notes / adr) → doc-style-checker → (선택) doc-translator.
코드/요구사항/변경분/결정을 사람이 읽는 문서로 변환. **앱 생성 파이프라인과 독립**이며
입력단은 `docs-analyze/*`를 재활용. 런타임 코드는 생성하지 않음.
`api-guide-generator`(산문 가이드)는 `api-docs-generator`(springdoc 애노테이션)·
`api-spec-generator`(설계 계약)와 별개.

### audit/ (8) — 독립 문서 규정 준수 감사 파이프라인
`audit-orchestrator`가 진입점. (docs-analyze 입력) → ruleset-loader(규칙 정규화) →
clause-extractor(대상 문서 절 추출) → conformance-checker(충족 판정) →
gap-analyzer(갭·개선안) → risk-scorer(위험 점수) → audit-report-generator(리포트) →
audit-validator(리포트 무결성: 규칙 커버리지·추적성·stats·verdict pass/fail).
대상 문서를 규제/정책/표준/체크리스트에 대해 **평가만** 하며, 문서 수정·코드 생성은 안 함.
증분 재감사(규칙/문서 변경 시 영향 절만 재검사)는 `data-change/*`가 담당.
`conformance-checker`(문서 준수 평가)는 `validator/*`(코드 검증)와 별개.

### proposal/ (7) — 독립 RFP→제안서 파이프라인
`proposal-orchestrator`가 진입점. (docs-analyze 입력) → rfp-analyzer(요구사항/평가기준/제약
해석) → scope-definer(스코프·산출물·가정) → effort-estimator(공수 person-days) →
pricing-generator(가격, 선택) → proposal-drafter(제안서 조립) → proposal-validator(RFP 커버리지·
스코프↔공수↔가격 정합·산술·섹션 완전성 pass/fail). **사전영업 스코핑**이며
런타임 코드나 실행 태스크 그래프는 만들지 않음. `scope-definer`/`effort-estimator`(제안 단계)는
`project-planner`(실행 태스크 분해)와 별개.

### asset/ (7) — 독립 2D 비주얼 에셋 파이프라인
`asset-orchestrator`가 진입점. (docs-analyze 브랜드 브리프, 선택) → asset-brief-analyzer(스펙) →
kind별 라우팅: icon-generator(SVG)·sprite-sheet-generator·placeholder-image-generator(직접 저작) /
image-prompt-generator(래스터·사실적 → 프롬프트 스펙) → asset-manifest-generator(매니페스트·검증).
**벡터/절차적은 외부 모델 없이 직접 저작**, 래스터는 연결된 이미지 도구에 위임하되 없으면 프롬프트
스펙까지만 산출(정직하게 degrade). `design/*`(스펙)과 별개이며 산출물을 `web/*`(public/)에 공급.

### seed-data/ (6) — 독립 시드/목 데이터 파이프라인
`seed-data-orchestrator`가 진입점. (docs-analyze 스키마, 선택) → data-schema-analyzer(필드/제약/관계·
생성순서) → mock-record-generator(레코드, FK 제외, seed 결정론적) → relationship-linker(FK 연결) →
seed-export-generator(SQL/JSON/CSV) → seed-data-validator(무결성 pass/fail). **스키마를 채우는 데이터**를
만들며 `spring/migration-generator`(스키마/DDL)와 별개. 생성된 앱을 데모/테스트 데이터로 채움.

### data-analysis/ (7) — 독립 데이터 분석·리포팅 파이프라인
`data-analysis-orchestrator`가 진입점. (docs-analyze/xlsx) → dataset-profiler(형상·타입·결측) →
data-cleaner(정제 계획·리포트) → data-analyzer(집계·추세·상관·세그먼트) →
chart-spec-generator + insight-writer → analysis-report-generator. `chart-spec-generator`(차트
**스펙**)는 `web/chart-generator`(실제 차트 코드)와 별개. 차트를 렌더하거나 코드를 만들지 않음.

### knowledge-base/ (6) — 독립 지식베이스 파이프라인
`knowledge-base-orchestrator`가 진입점. (docs-analyze) → content-chunker(청킹) →
kb-indexer(토픽 택소노미) → faq-generator / onboarding-generator / glossary-generator.
내부 코퍼스를 재사용 가능한 지식으로 조직. `research/*`(외부 웹+팩트체크)·`docwriting/*`(단일 문서
저작)와 별개. 모든 아티팩트는 chunk 출처 인용.

### localization/ (5) — 독립 제품 문자열 현지화 파이프라인
`localization-orchestrator`가 진입점. (docs-analyze) → string-extractor(키·플레이스홀더 추출) →
catalog-translator(로케일별 번역) → plural-format-handler(CLDR 복수·포맷) →
localization-validator(누락 키·플레이스홀더 패리티 pass/fail). **번역된 카탈로그**를 산출하며
`docwriting/doc-translator`(산문)·`web/i18n-generator`(런타임 코드)와 별개.

### game-master/ (7) — 독립 TRPG 세션 준비 파이프라인 (여가)
`game-master-orchestrator`가 진입점. (docs-analyze 로어 임포트, 선택) → world-builder →
npc-generator → quest-generator → encounter-generator(파티 밸런스) → session-outliner →
lore-consistency-checker(로어·참조·스탯·밸런스 pass/fail). 순수 텍스트 게임 준비물.

### story-studio/ (7) — 독립 창작 소설 파이프라인 (여가)
`story-studio-orchestrator`가 진입점. (docs-analyze 자료 임포트, 선택) → premise-developer →
character-designer → plot-outliner → chapter-drafter → style-tuner →
narrative-continuity-checker(타임라인·인물·POV pass/fail). docwriting의 픽션 쌍둥이.

### trip-planner/ (7) — 독립 여행 계획 파이프라인 (여가)
`trip-planner-orchestrator`가 진입점. **research-orchestrator 재활용**(목적지 사실) →
destination-profiler → itinerary-builder → logistics-planner + budget-estimator →
packing-list-generator → trip-feasibility-validator(이동시간·영업시간·예산 pass/fail).
가격/예약은 추정이며 실시간은 외부 도구 필요(정직하게 표기).

### recipe-kitchen (6) · quiz-forge (6) · fitness-coach (6) — 여가 파이프라인
- **recipe-kitchen**: pantry-analyzer → recipe-developer → meal-planner → shopping-list-generator
  → nutrition-validator(영양·알레르기 pass/fail). 영양은 정성적 추정.
- **quiz-forge**: quiz-blueprint-planner → question-generator → distractor-designer →
  answer-key-builder → quiz-fairness-validator(단일 정답·난이도·편향 pass/fail).
- **fitness-coach**: fitness-profiler → program-designer → workout-builder → progression-planner
  → training-safety-validator(부상 제약·볼륨·회복 pass/fail). **교육용, 의료 조언 아님.**

### event-planner (6) · media-curator (6) · music-curator (6) — 여가 파이프라인
- **event-planner**: event-brief-analyzer → theme-designer → menu-activity-planner →
  run-of-show-builder → event-feasibility-validator(예산·시간·수용·식이 pass/fail).
- **media-curator**(research 재활용): taste-profiler → title-finder → recommender →
  watch-order-planner → media-fit-validator(등급·러닝타임·가용성 pass/fail). 시청/독서 담당.
- **music-curator**(research 재활용): music-taste-profiler → track-finder → playlist-sequencer →
  playlist-annotator → playlist-flow-validator(길이·에너지 아크·explicit pass/fail). 청취 담당.
- media(시청/독서) ↔ music(청취) 별개. 둘 다 `research-orchestrator`로 실제 타이틀/트랙 수집.

---

## 5. 책임 경계 (중복 방지 규칙)

겹치기 쉬운 스킬 간 소유권을 명확히 정한 규칙입니다. (전문은 INVENTORY.md 참조)

- **API 5종 분리**: `api-generator`(런타임 코드) ↔ `api-spec-generator`(설계 문서) ↔
  `api-docs-generator`(springdoc/Swagger 애노테이션) ↔ `api-client-generator`(프론트 HTTP
  클라이언트) ↔ `payload-model-generator`(관측된 JSON/XML 샘플 → 타입 모델만). 앞의 넷은
  **api-spec 설계 계약** 기반, `payload-model-generator`는 **구체 직렬화 샘플** 기반이며
  **모델만** 산출(엔드포인트·클라이언트·OpenAPI 생성 안 함). 다섯 다 별개.
- **이벤트/메시징 3종**: `event-generator`(인프로세스 Spring 이벤트) ↔
  `messaging-generator`(브로커, Redis Pub/Sub 포함) ↔ `websocket-generator`(클라이언트 대면).
- **스케줄 vs 배치**: 스케줄 트리거는 `scheduler-generator`, 대량 처리 잡은 `batch-generator`.
- **integration 분해**: 이메일/SMS/푸시 → `notification-generator`,
  파일/오브젝트 스토리지(S3/GCS/Azure) → `file-storage-generator`,
  범용 외부 HTTP 전송만 `integration-generator`.
- **설정 3계층**: `env-config-generator`(값 공급) → `config-properties-generator`
  (`@ConfigurationProperties` 바인딩) / `spring-initializer`(기본 yml 스캐폴드).
- **프론트 데이터 계층**: `api-client-generator`(HTTP/타입) → `data-generator`
  (TanStack Query 훅) → `state-generator`(전역/UI 상태) → `hook-generator`(그 외).
  실시간 수신은 `realtime-client-generator`가 TanStack Query 캐시에 반영.
- **라우팅/인증/번역**: `middleware-generator`(엣지 라우팅) ↔ `auth-generator`(세션/가드)
  ↔ `i18n-generator`(번역). middleware는 로케일 라우팅만.
- **피드백 UI**: `toast-notification-generator`(비차단) ↔ `dialog-generator`(차단 모달).
- **테마**: `theme-generator`(런타임 provider/다크모드) ↔ `design-tokens-generator`(토큰 값).
- **검증 분리**: `dependency-license-validator`(공급망 CVE/라이선스) ↔
  `security-validator`(코드 보안/OWASP).
- `api-client-generator`는 frontend-orchestrator만 생성(중복 생성 금지).
- **클라이언트 타깃 3종**: 세 폴더 `web/`·`desktop/`·`mobile/`는 **모두 `category: frontend`**
  (폴더=타깃, category=계층). `web`(`web/*`, Next.js) ↔ `desktop`(`desktop/*`, Tauri) ↔
  `mobile`(`mobile/*`, Flutter). `target_stack.clients`로 선택(복수 공존 가능), `app-orchestrator`가 조율.
- **desktop은 UI 생성기를 만들지 않는다**: Tauri가 `web/*` React 산출물을 그대로 래핑.
  `desktop/*`는 네이티브 쉘/IPC/스토리지/업데이터/패키징/테스트만.
- **mobile은 자체 UI 생성기**(`flutter-*`): React 코드 재사용 안 함. `design-tokens` 값
  (→`flutter-theme-generator`)과 backend `api-spec`(→`flutter-api-client-generator`)만 계약으로 재사용.
- **네이밍 충돌 방지**: `flutter-state-generator`(Riverpod) ↔ `state-generator`(React),
  `flutter-api-client-generator`(Dio) ↔ `api-client-generator`(fetch),
  `flutter-theme-generator`/`flutter-form-generator` ↔ frontend 동명 스킬 — 모두 별개. mobile은 `flutter-*` 접두사로 통일.
- **초기화 소유권**: `tauri-initializer`(desktop) · `flutter-initializer`(mobile)는 각 클라이언트
  오케스트레이터가 소유. `nextjs-initializer`(web) · `spring-initializer`(backend)와 별개.
- **네이티브 브리지 vs 백엔드 통신**: `native-bridge-generator`(Tauri command: fs/dialog/notification 등 OS 기능)는
  서버 HTTP와 별개 — 서버 통신은 재사용된 웹 `api-client`가 담당.

---

## 6. 스킬 파일 규격 (Frontmatter)

모든 스킬은 아래 단일 표준을 따릅니다. 엔진 전용 필드
(`priority/entrypoint/parallel/timeout/retry`)는 **사용하지 않습니다**.

```yaml
---
name: <kebab-case, 파일명과 반드시 일치>
description: <한 줄. "무엇을 언제 쓰는지">
version: 1.0.0
category: orchestrator | docs-analyze | blueprint | backend | frontend | design | validator | code-change | data-change | doc-change | spec-change | deployment | vcs | codegen | research | docwriting | audit | proposal | asset | seed-data | data-analysis | knowledge-base | localization | game-master | story-studio | trip-planner | recipe-kitchen | quiz-forge | fitness-coach | event-planner | media-curator | music-curator
tags: [<검색용 키워드…>]
model: inherit
invokes: [<하위 스킬 name…>]   # 오케스트레이터만. DAG 단일 소스. 없으면 생략
inputs: [<입력…>]
outputs: [<출력…>]
---
```

**규칙**
- `name` = 파일명(확장자 제외)과 정확히 일치.
- `invokes`의 값은 실제 존재하는 스킬 `name`만 (dangling reference 금지).
- `model`은 기본 `inherit` (특정 모델 하드코딩 금지).
- `tags`로 통일 (`keyword` 미사용).

**본문 섹션**

생성기/오케스트레이터:
```
# Goal / # Inputs / # Output / # Workflow / # Rules / # Examples(필수)
```
검증기(validator):
```
# Goal / # Scope / # Checks / # Pass/Fail Criteria / # Output Schema(필수) / # Examples
```
- 모든 스킬에 `# Examples` 필수(최소 1개 end-to-end 예시).
- 새 스킬은 [_template.md](_template.md)로 시작.

---

## 7. 사용법

### 7.1 앱 생성 (전체 파이프라인)
`app-orchestrator`를 진입점으로 문서를 넘깁니다.

```yaml
# 입력 예시
documents: [requirements.docx, ui-design.pptx, api-spec.xlsx]
target_stack:
  backend: Spring Boot
  frontend: Next.js
  database: MariaDB
options:
  generate_tests: true
  max_remediation_iterations: 2
  deploy: true          # 선택. review 이후 deployment-orchestrator 실행
```

```
# 출력(요약) 예시
✔ analyze  → 12 requirements
✔ blueprint→ 3 modules, 8 entities
✔ plan     → 4 features, 21 tasks
✔ generate → 47 backend files, 33 frontend files
✔ validate → 2 errors
↻ remediate(1/1) → 0 errors
✔ review   → coverage 94%, 3 suggestions, 0 remaining
```

### 7.2 부분 실행
전체가 아니라 특정 단계만 필요하면 해당 오케스트레이터를 직접 호출합니다.
- 설계만: `blueprint-orchestrator`
- 디자인 파운데이션만: `design-orchestrator`
- 단일 피처만: `feature-orchestrator`
- 검증만: `validation-orchestrator`

### 7.3 리서치 (앱 생성과 독립)
근거·출처가 필요한 질의는 `research-orchestrator`를 진입점으로 사용합니다.

```yaml
user_request: "Spring Boot 3.4는 Virtual Threads를 지원하며 어떤 Java 버전이 필요한가?"
options:
  trusted_domains: [spring.io, docs.oracle.com]
  time_range: last_12_months
```

### 7.4 새 스킬 추가 절차
1. [_template.md](_template.md)를 복사해 알맞은 카테고리 폴더에 `name.md` 생성.
2. frontmatter의 `name`을 파일명과 일치시키고 규격 필드만 사용.
3. 오케스트레이터가 호출한다면 상위 `invokes`에 `name` 추가.
4. **[INVENTORY.md](INVENTORY.md)에 등록** — 목록/DAG의 단일 소스이므로 필수.
5. 겹치는 스킬이 있으면 §5 책임 경계에 "use X instead of Y" 규칙 추가.

---

## 8. 참고 파일
- [INVENTORY.md](INVENTORY.md) — 전체 스킬 목록 + 의존성 DAG + 책임 경계(단일 소스)
- [DOMAINS.md](DOMAINS.md) — 앱 생성과 독립된 18개 도메인(업무 9 + 여가 9) 한눈에 보기
- [README.md](README.md) — 프로젝트 개요 + frontmatter/본문 규격
- [_template.md](_template.md) — 스킬 작성 템플릿
- `_deprecated/` — 이전 버전 아카이브 (참고용, 신규 규격 아님)
</content>
</invoke>
