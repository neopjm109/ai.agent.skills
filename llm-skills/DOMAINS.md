# 독립 도메인 한눈에 보기

앱 생성 파이프라인(`app-orchestrator`)과 **독립적으로 동작**하는 파이프라인들의 요약입니다.
각 도메인은 자체 진입 오케스트레이터를 가지며, 단독으로 호출하거나 앱 생성 결과물과 조합해
쓸 수 있습니다.

> 상세 목록·DAG는 [INVENTORY.md](INVENTORY.md), 규격은 [README.md](README.md),
> 전체 아키텍처는 [ARCHITECTURE.md](ARCHITECTURE.md) 참조.

---

## 공통 원칙 (18개 도메인 공유)

- **오케스트레이터는 위임만** — 순서·라우팅·리포트만 하고 직접 산출물을 만들지 않음.
- **입력 어댑터 재활용** — 문서 입력은 전부 기존 `docs-analyze/*`(docx/pptx/xlsx/markdown/pdf/csv)로 파싱.
- **런타임 코드 생성 안 함** — 이 도메인들은 앱 코드가 아니라 문서·리포트·에셋·데이터를 만듦.
- **근거 추적성** — 모든 산출물은 입력 소스로 추적 가능; 근거 없는 주장/생성 금지.
- **결정론·pass/fail** — 검증·점수 단계는 재현 가능한 결정론적 판정을 반환.

---

## 도메인 요약표

### 업무 도메인 (9)
| 도메인 | 진입점 | 입력 → 출력 | 스킬 수 |
|--------|--------|-------------|:------:|
| [research](research/) | `research-orchestrator` | 질의 → 근거 기반 요약(출처 인용) | 10 |
| [docwriting](docwriting/) | `docwriting-orchestrator` | 코드/요구사항 → 문서(가이드·매뉴얼·릴리스노트·ADR) | 8 |
| [audit](audit/) | `audit-orchestrator` | 문서 + 룰셋 → 준수 갭 리포트(risk) (검증 pass/fail) | 8 |
| [proposal](proposal/) | `proposal-orchestrator` | RFP → 스코프·공수·가격·제안서 (검증 pass/fail) | 7 |
| [asset](asset/) | `asset-orchestrator` | 브리프 → 2D 에셋(SVG·스프라이트·플레이스홀더) + 매니페스트 | 7 |
| [seed-data](seed-data/) | `seed-data-orchestrator` | 스키마 → 시드/목 데이터(SQL·JSON·CSV) | 6 |
| [data-analysis](data-analysis/) | `data-analysis-orchestrator` | 데이터셋 → 분석·차트 스펙·인사이트 리포트 (검증 pass/fail) | 8 |
| [knowledge-base](knowledge-base/) | `knowledge-base-orchestrator` | 문서 코퍼스 → FAQ·온보딩·용어집 (검증 pass/fail) | 7 |
| [localization](localization/) | `localization-orchestrator` | 문자열 → 로케일별 번역 카탈로그 | 5 |

### 여가 도메인 (9)
| 도메인 | 진입점 | 입력 → 출력 | 스킬 수 |
|--------|--------|-------------|:------:|
| [game-master](game-master/) | `game-master-orchestrator` | 캠페인 전제 → 실행 가능한 TRPG 세션 팩 | 7 |
| [story-studio](story-studio/) | `story-studio-orchestrator` | 전제 → 초안 픽션(인물·플롯·챕터) | 7 |
| [trip-planner](trip-planner/) | `trip-planner-orchestrator` | 여행 요청 → 일정·동선·예산·짐 (research 재활용) | 7 |
| [recipe-kitchen](recipe-kitchen/) | `recipe-kitchen-orchestrator` | 재료/식단 → 레시피·식단표·장보기 (영양 검증) | 6 |
| [quiz-forge](quiz-forge/) | `quiz-forge-orchestrator` | 주제/난이도 → 문제·오답·정답키 (공정성 검증) | 6 |
| [fitness-coach](fitness-coach/) | `fitness-coach-orchestrator` | 목표/장비 → 프로그램·세션·진행 (안전 검증, 교육용) | 6 |
| [event-planner](event-planner/) | `event-planner-orchestrator` | 행사/예산 → 테마·메뉴·타임라인 (실현성 검증) | 6 |
| [media-curator](media-curator/) | `media-curator-orchestrator` | 취향 → 영화/도서 추천·시청 순서 (research 재활용) | 6 |
| [music-curator](music-curator/) | `music-curator-orchestrator` | 무드 → 플레이리스트·에너지 아크 (research 재활용) | 6 |

**독립 도메인 스킬 합계: 123** (전체 280개 중) — 업무 66 + 여가 57

> 변경 계층 참고: `data-change/*`(4)는 이 도메인들을 **생성이 아니라 변경**한다 —
> seed-data·localization·knowledge-base·data-analysis 산출물을 입력 델타만 증분 upsert하거나
> 참조무결성을 지키며 삭제하고, 각 도메인 validator(seed-data·localization·knowledge-base·
> data-analysis-validator)로 pass/fail 종료. `data-remediation-orchestrator`는 검증 실패를
> 재검증까지 자가치유(코드의 `remediation-orchestrator` 대응). 코드 대상은 `code-change/*` 참조.
>
> 문서 변경 계층 `doc-change/*`(4)는 docwriting 산문 문서를 **생성이 아니라 개정**한다 —
> 영향 섹션만 개정(modify)하거나 교차참조/TOC를 지키며 삭제(delete)하고 `doc-style-checker` pass로 종료.
> `doc-remediation-orchestrator`는 style 실패를 재검사까지 자가치유하며 상위는 `doc-pipeline-orchestrator`
> (app `compose_docs`로 노출). **대상: docwriting·proposal**(proposal은 `proposal-validator` 게이트 신설).
> audit는 `audit-validator` 게이트 신설 후 `data-change/*`에 5번째 도메인으로 편입 — 규칙/문서 변경 시
> 영향 절만 증분 재감사(modify)하거나 규칙 제거(delete). blueprint·design 스펙 개정은 `spec-change/*`가 담당 —
> 스펙 요소 개정/삭제 후 `blueprint-validator`/`design-validator`로 게이트하고 `code-change`로
> 코드에 파급, `validation-orchestrator`로 코드 게이트하는 L2↔L3 브리지.

---

## 파이프라인 흐름

### research — 근거 기반 리서치
```
질의 → 검색(web / docs / github / news) → web-research(사실 추출)
     → source-validation → compare-sources → fact-check → summarize
```
출처가 필요한 기술 질의에 사용. 앱 생성과 완전 독립.

### docwriting — 코드/요구사항 → 문서
```
(docs-analyze) → outline → 본문 생성
   ├ user-guide/reference → doc-draft
   ├ api-guide            → api-guide (산문; springdoc 애노테이션과 별개)
   ├ release-notes        → release-notes
   └ adr                  → adr
→ doc-style-checker → (선택) doc-translator
```
앱 파이프라인의 **역방향 보완재**(코드 → 문서).

### audit — 문서 규정 준수 감사
```
(docs-analyze) → ruleset-loader(규칙 정규화) → clause-extractor(대상 절 추출)
   → conformance-checker(충족 판정) → gap-analyzer(갭·개선안)
   → risk-scorer(위험 점수) → audit-report-generator(verdict)
```
`validator/*`(코드 검증)와 별개로 **문서**를 규제/정책/표준에 대해 평가.

### proposal — RFP → 제안서
```
(docs-analyze) → rfp-analyzer(요구사항·평가기준·제약)
   → scope-definer(스코프·산출물·가정) → effort-estimator(공수 person-days)
   → pricing-generator(가격, 선택) → proposal-drafter(제안서 조립)
```
**사전영업(pre-sales)** 스코핑. `project-planner`(실행 태스크 분해)와 별개.

### asset — 2D 비주얼 에셋
```
(docs-analyze 브랜드 브리프, 선택) → asset-brief-analyzer(스펙)
   → kind별 라우팅:
       icon(SVG) / sprite-sheet / placeholder   ← 외부 모델 없이 직접 저작
       raster·사실적 → image-prompt-generator    ← 프롬프트 스펙까지만(degrade)
   → asset-manifest-generator(매니페스트·검증)
```
벡터/절차적은 결정론적 직접 저작, 래스터는 연결된 이미지 도구 위임(없으면 프롬프트 스펙).
`design/*`(스펙)과 별개이며 산출물을 `web/*`(public/)에 공급.

### seed-data — 시드/목 데이터
```
(docs-analyze 스키마, 선택) → data-schema-analyzer(필드·제약·관계·생성순서)
   → mock-record-generator(레코드, FK 제외, seed 결정론적)
   → relationship-linker(FK 연결, dangling 0)
   → seed-export-generator(SQL / JSON / CSV) → seed-data-validator(무결성 pass/fail)
```
`spring/migration-generator`(스키마/DDL)와 별개 — migration은 스키마, seed-data는 데이터.

### data-analysis — 데이터 분석·리포팅
```
(docs-analyze/xlsx·csv) → dataset-profiler(형상·타입·결측) → data-cleaner(정제 계획·리포트)
   → data-analyzer(집계·추세·상관·세그먼트)
   → chart-spec-generator(차트 스펙) + insight-writer(source-traced 인사이트)
   → analysis-report-generator → data-analysis-validator(출처추적·차트유효·수치정합 pass/fail)
```
`chart-spec-generator`(스펙)는 `web/chart-generator`(실제 차트 코드)와 별개.

### knowledge-base — 코퍼스 → 지식 아티팩트
```
(docs-analyze) → content-chunker(청킹+출처) → kb-indexer(토픽 택소노미)
   → faq-generator / onboarding-generator / glossary-generator (모두 chunk 인용)
   → knowledge-base-validator(인용 무결성·용어 일관성 pass/fail)
```
내부 코퍼스를 조직. `research/*`(외부 웹+팩트체크)·`docwriting/*`(단일 문서)와 별개.

### localization — 제품 문자열 현지화
```
(docs-analyze) → string-extractor(키·플레이스홀더) → catalog-translator(로케일별 번역)
   → plural-format-handler(CLDR 복수·포맷) → localization-validator(패리티 pass/fail)
```
**번역된 카탈로그** 산출. `doc-translator`(산문)·`web/i18n-generator`(코드)와 별개.

### game-master — TRPG 세션 준비 (여가)
```
(docs-analyze 로어, 선택) → world-builder → npc-generator → quest-generator
   → encounter-generator(파티 밸런스) → session-outliner
   → lore-consistency-checker(로어·참조·스탯·밸런스 pass/fail)
```
순수 텍스트 게임 준비물. 외부 도구 불필요.

### story-studio — 창작 소설 (여가)
```
(docs-analyze 자료, 선택) → premise-developer → character-designer → plot-outliner
   → chapter-drafter → style-tuner
   → narrative-continuity-checker(타임라인·인물·POV pass/fail)
```
docwriting의 픽션 쌍둥이(구조 동일, 산출물은 소설).

### trip-planner — 여행 계획 (여가)
```
research-orchestrator(목적지 사실) → destination-profiler → itinerary-builder
   → logistics-planner + budget-estimator → packing-list-generator
   → trip-feasibility-validator(이동시간·영업시간·예산 pass/fail)
```
`research` 도메인을 끌어 쓰는 조합 쇼케이스. 가격/예약은 추정(실시간은 도구 필요).

### recipe-kitchen — 집밥/요리 (여가)
```
pantry-analyzer → recipe-developer → meal-planner → shopping-list-generator
   → nutrition-balancer(영양·알레르기 pass/fail)
```
영양은 정성적 추정(정확 열량은 별도 도구).

### quiz-forge — 퀴즈/트리비아 (여가)
```
quiz-blueprint-planner → question-generator → distractor-designer → answer-key-builder
   → quiz-fairness-validator(단일 정답·난이도·편향 pass/fail)
```

### fitness-coach — 운동 계획 (여가)
```
fitness-profiler → program-designer → workout-builder → progression-planner
   → training-safety-validator(부상 제약·볼륨·회복 pass/fail)
```
일반 교육용, 의료 조언 아님.

### event-planner — 파티/모임 (여가)
```
event-brief-analyzer → theme-designer → menu-activity-planner → run-of-show-builder
   → event-feasibility-validator(예산·시간·수용·식이 pass/fail)
```

### media-curator — 영화/도서 큐레이션 (여가)
```
research-orchestrator(실제 타이틀) → taste-profiler → title-finder → recommender
   → watch-order-planner → media-fit-validator(등급·러닝타임·가용성 pass/fail)
```
시청/독서 담당. `music-curator`(청취)와 별개.

### music-curator — 플레이리스트 (여가)
```
research-orchestrator(실제 트랙) → music-taste-profiler → track-finder → playlist-sequencer
   → playlist-annotator → playlist-flow-validator(길이·에너지 아크·explicit pass/fail)
```
청취 담당. `media-curator`(시청/독서)와 별개.

---

## 앱 생성 파이프라인과의 조합 (시너지)

독립 도메인이지만 앱 생성 결과물과 엮으면 강력합니다. (강결합 없이 선택적 연결)

```
app-orchestrator → Spring + Next.js 코드
        │
        ├── docwriting     → 그 코드/요구사항으로 인수인계 문서·API 가이드 생성
        ├── asset          → 프론트의 아이콘·플레이스홀더·스프라이트 채움 (public/)
        ├── seed-data      → 도메인 모델을 데모/테스트 데이터로 채움 (SQL fixture)
        ├── data-analysis  → seed/운영 데이터 분석 → chart-spec을 web/chart로
        ├── knowledge-base → 산출 문서를 FAQ·온보딩·용어집으로 조직
        ├── localization   → 프론트 문자열 카탈로그를 다국어로 번역
        └── audit          → 산출 문서/정책의 규정 준수 검토
```

- **정식 배선(신규)**: `app-orchestrator`의 `options.compose_data`가 켜지면 Step 8b에서
  `data-pipeline-orchestrator`를 호출 — 생성된 도메인 모델을 seed-data `schema_source`로,
  프론트 문자열을 localization `source`로 넘겨 데이터/카탈로그를 채우고, 각 도메인 validator
  실패 시 `data-remediation-orchestrator`로 자가치유해 **검증 통과 데이터**를 돌려준다.
  (seed-data·localization은 이 경로로 자동 합성; knowledge-base·data-analysis는 직접 요청 시 동일 파이프라인에서 처리.)
- **asset + seed-data**: 코드만 생성된 앱을 **데모 가능한 상태**로 채움 —
  seed 레코드의 이미지 필드를 `asset_manifest` 항목으로 가리키게 연결 가능(옵션).
- **docwriting**: 생성된 코드에서 API 가이드·릴리스노트를 뽑아 인수인계 공백을 메움.
- **research / proposal**: 앱과 무관하게 단독 업무(리서치·제안)로도 사용.

---

## 참고: 클라이언트 생성 도메인 (독립 도메인 아님)

`desktop/`(Tauri, 8) · `mobile/`(Flutter, 13)는 위 독립 도메인과 달리 **앱 생성 파이프라인의
클라이언트 타깃**(L3 생성 계층)입니다. `app-orchestrator`가 `target_stack.clients` 선택에 따라
웹 feature 루프 완료 후(4b 단계) `desktop-orchestrator`/`mobile-orchestrator`를 호출합니다.

- **desktop**(Tauri): `web/*` React 산출물을 그대로 래핑 — UI는 재사용, 네이티브 쉘/IPC/패키징만 생성.
- **mobile**(Flutter): 자체 Dart UI 생성, `design-tokens` 값 + backend `api-spec`만 계약으로 재사용.

상세는 [ARCHITECTURE.md](ARCHITECTURE.md) §4(desktop/·mobile/)와 [INVENTORY.md](INVENTORY.md) 참조.

---

## 새 독립 도메인 추가 절차

1. `<domain>/` 폴더 생성, 진입 오케스트레이터 + 하위 워커 스킬을 [_template.md](_template.md)로 작성.
2. 각 스킬 frontmatter의 `category`를 새 도메인명으로 지정(파일명 = `name`).
3. 오케스트레이터 `invokes`에 하위 스킬 `name` 등록(문서 입력이 필요하면 `docs-analyze-*` 재활용).
4. **[INVENTORY.md](INVENTORY.md)** 에 도메인 섹션 + DAG + 책임 경계 규칙 등록.
5. **[ARCHITECTURE.md](ARCHITECTURE.md)** (카테고리 표·계층도·§4·frontmatter enum), **[README.md](README.md)**
   (트리·enum), 그리고 이 문서(DOMAINS.md)의 요약표·흐름에 반영.
