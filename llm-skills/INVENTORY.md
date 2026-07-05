# INVENTORY — 전체 스킬 목록 & 의존성 그래프(DAG)

참조의 **단일 소스**. 새 스킬을 추가하거나 `invokes`를 적을 때는 반드시 여기 등록된 `name`만 사용한다.
`(new)` = _deprecated/에 없던 신규, `(fix)` = _deprecated/에서 이름/오타 수정, 나머지는 이관.

## orchestrator/ (13)
| name | invokes |
|------|---------|
| app-orchestrator | docs-analyze-* (docx/pptx/xlsx/markdown/pdf), blueprint-orchestrator, design-orchestrator, spring-initializer, nextjs-initializer, project-planner, feature-orchestrator, desktop-orchestrator *(선택: clients에 desktop)*, mobile-orchestrator *(선택: clients에 mobile)*, execution-orchestrator, validation-orchestrator, remediation-orchestrator, review-orchestrator, data-pipeline-orchestrator *(선택: options.compose_data)*, doc-pipeline-orchestrator *(선택: options.compose_docs)*, deployment-orchestrator |
| blueprint-orchestrator | architecture-generator, domain-model-generator, database-generator, api-spec-generator, event-topology-generator, blueprint-validator |
| design-orchestrator *(new)* | design-tokens-generator, design-system-generator, ux-flow-generator, wireframe-generator, figma-to-component, design-validator |
| project-planner | — |
| feature-orchestrator | backend-orchestrator, frontend-orchestrator, integration-generator |
| backend-orchestrator *(router)* | spring-backend-orchestrator, nestjs-backend-orchestrator, django-backend-orchestrator *(target_stack.backend로 1개 선택)* |
| frontend-orchestrator | page-generator, layout-generator, component-generator, form-generator, table-generator, dialog-generator, chart-generator, hook-generator, state-generator, data-generator, api-client-generator, auth-generator, i18n-generator, middleware-generator, theme-generator, toast-notification-generator, realtime-client-generator, feature-generator, frontend-test-generator |
| execution-orchestrator | — |
| validation-orchestrator | architecture-validator, backend-validator, frontend-validator, integration-validator, security-validator, performance-validator, dependency-license-validator, test-validator |
| remediation-orchestrator | execution-orchestrator, code-change-orchestrator *(외과적 수정)*, validation-orchestrator |
| review-orchestrator | — |
| deployment-orchestrator *(new, deployment/)* | cicd-generator, env-config-generator |
| data-pipeline-orchestrator *(new, 상위 데이터 파이프라인)* | seed-data-orchestrator, localization-orchestrator, knowledge-base-orchestrator, data-analysis-orchestrator, audit-orchestrator, data-remediation-orchestrator |
| doc-pipeline-orchestrator *(new, 상위 문서 파이프라인)* | docwriting-orchestrator, proposal-orchestrator, doc-remediation-orchestrator |

## docs-analyze/ (6)
docs-analyze-docx, docs-analyze-pptx, docs-analyze-xlsx, docs-analyze-markdown, docs-analyze-pdf *(new)*,
docs-analyze-csv *(new: 테이블 데이터셋/TSV 입력 어댑터; data-analysis·seed-data가 재활용)*

## blueprint/ (6) — 설계 산출물만, 코드 생성 아님
architecture-generator, domain-model-generator, database-generator, api-spec-generator,
event-topology-generator *(new)*, blueprint-validator *(new: 스펙 내부 정합 pass/fail; blueprint-orchestrator가 호출)*

## spring/ (20) — Spring Boot (backend 스택 중 spring 타깃)
spring-backend-orchestrator *(new: 기존 backend-orchestrator 역할을 계승, 아래 16 생성기 팬아웃)*,
spring-initializer, domain-generator, api-generator, security-generator, redis-generator,
messaging-generator, event-generator, scheduler-generator, batch-generator, migration-generator,
integration-generator, config-properties-generator, observability-generator,
notification-generator, file-storage-generator, websocket-generator,
api-docs-generator, spring-test-generator, spring-senior-programmer *(구현 위임, _deprecated/shared)*

## nestjs/ (19) — NestJS 백엔드 (backend 스택 중 nestjs 타깃; TypeORM)
| name | invokes |
|------|---------|
| nestjs-backend-orchestrator *(new)* | nestjs-initializer, nestjs-domain-generator, nestjs-api-generator, nestjs-auth-generator, nestjs-event-generator, nestjs-messaging-generator, nestjs-cache-generator, nestjs-scheduler-generator, nestjs-queue-generator, nestjs-migration-generator, nestjs-config-generator, nestjs-observability-generator, nestjs-notification-generator, nestjs-file-storage-generator, nestjs-websocket-generator, nestjs-api-docs-generator, nestjs-test-generator |
| nestjs-initializer *(new)* | — |
| nestjs-senior-programmer *(new, 구현 위임; 오케스트레이터 invokes 아님)* | — |
| nestjs-domain-generator · nestjs-api-generator · nestjs-auth-generator · nestjs-event-generator · nestjs-messaging-generator · nestjs-cache-generator · nestjs-scheduler-generator · nestjs-queue-generator · nestjs-migration-generator · nestjs-config-generator · nestjs-observability-generator · nestjs-notification-generator · nestjs-file-storage-generator · nestjs-websocket-generator · nestjs-api-docs-generator · nestjs-test-generator *(new)* | — |

## django/ (19) — Django + DRF 백엔드 (backend 스택 중 django 타깃)
| name | invokes |
|------|---------|
| django-backend-orchestrator *(new)* | django-initializer, django-model-generator, django-api-generator, django-auth-generator, django-signals-generator, django-celery-generator, django-cache-generator, django-scheduler-generator, django-task-generator, django-migration-generator, django-settings-generator, django-observability-generator, django-notification-generator, django-storage-generator, django-channels-generator, django-api-docs-generator, django-test-generator |
| django-initializer *(new)* | — |
| django-senior-programmer *(new, 구현 위임; 오케스트레이터 invokes 아님)* | — |
| django-model-generator · django-api-generator · django-auth-generator · django-signals-generator · django-celery-generator · django-cache-generator · django-scheduler-generator · django-task-generator · django-migration-generator · django-settings-generator · django-observability-generator · django-notification-generator · django-storage-generator · django-channels-generator · django-api-docs-generator · django-test-generator *(new)* | — |

## web/ (21) — Next.js
nextjs-initializer *(fix)*, page-generator, layout-generator, component-generator, form-generator,
table-generator, dialog-generator, chart-generator, hook-generator, state-generator, data-generator,
api-client-generator, auth-generator, i18n-generator, middleware-generator *(new)*, theme-generator *(new)*,
toast-notification-generator *(new)*, realtime-client-generator *(new)*, feature-generator,
frontend-test-generator, typescript-senior-programmer *(구현 위임, _deprecated/shared)*

## desktop/ (8) — Tauri 데스크톱 클라이언트 (web/* React 재사용, 쉘만 생성)
| name | invokes |
|------|---------|
| desktop-orchestrator *(new)* | tauri-initializer, desktop-shell-generator, native-bridge-generator, desktop-storage-generator, desktop-updater-generator, desktop-packaging-generator, desktop-test-generator |
| tauri-initializer *(new)* | — |
| desktop-shell-generator *(new)* | — |
| native-bridge-generator *(new)* | — |
| desktop-storage-generator *(new)* | — |
| desktop-updater-generator *(new)* | — |
| desktop-packaging-generator *(new)* | — |
| desktop-test-generator *(new)* | — |

## mobile/ (13) — Flutter 모바일 클라이언트 (자체 UI; design-tokens 값 + api-spec 재사용)
| name | invokes |
|------|---------|
| mobile-orchestrator *(new)* | flutter-initializer, flutter-screen-generator, flutter-widget-generator, flutter-navigation-generator, flutter-state-generator, flutter-api-client-generator, flutter-storage-generator, flutter-theme-generator, flutter-form-generator, flutter-notification-generator, flutter-test-generator |
| flutter-initializer *(new)* | — |
| flutter-senior-programmer *(new, 구현 위임; 오케스트레이터 invokes 아님)* | — |
| flutter-screen-generator *(new)* | — |
| flutter-widget-generator *(new)* | — |
| flutter-navigation-generator *(new)* | — |
| flutter-state-generator *(new)* | — |
| flutter-api-client-generator *(new)* | — |
| flutter-storage-generator *(new)* | — |
| flutter-theme-generator *(new)* | — |
| flutter-form-generator *(new)* | — |
| flutter-notification-generator *(new)* | — |
| flutter-test-generator *(new)* | — |

## design/ (6) — 디자인 시스템 생성 (design-orchestrator가 조율, frontend에 공급)
design-tokens-generator, design-system-generator, figma-to-component,
wireframe-generator, ux-flow-generator, design-validator *(new: 스펙 내부 정합 pass/fail; design-orchestrator가 호출)*

## validator/ (8)
architecture-validator, backend-validator, frontend-validator, integration-validator,
security-validator, performance-validator *(new)*, dependency-license-validator *(new)*, test-validator

## code-change/ (4) — 기존 코드 수정/리팩토링/삭제 (생성이 아니라 변경; senior-programmer에 위임)
| name | invokes |
|------|---------|
| code-change-orchestrator *(new)* | code-modifier, code-refactorer, code-remover |
| code-modifier *(new)* | spring-senior-programmer, nestjs-senior-programmer, django-senior-programmer, typescript-senior-programmer, flutter-senior-programmer *(stack로 택1)*, validation-orchestrator *(게이트)* |
| code-refactorer *(new)* | spring-senior-programmer, nestjs-senior-programmer, django-senior-programmer, typescript-senior-programmer, flutter-senior-programmer *(stack로 택1)*, validation-orchestrator *(게이트)* |
| code-remover *(new)* | spring-senior-programmer, nestjs-senior-programmer, django-senior-programmer, typescript-senior-programmer, flutter-senior-programmer *(stack로 택1)*, validation-orchestrator *(게이트)* |

> 모든 `*-generator`는 신규 코드를 **생성**(재실행 시 덮어씀)하는 반면, `code-change/*`는
> 기존 코드를 **읽고 변경**한다. 언어별 코드 작성은 `change_contract.stack`으로 계층
> senior-programmer에 위임(`spring|nestjs|django|typescript|flutter`; nextjs·Tauri/desktop UI는
> typescript-senior-programmer). 모든 변경은 `validation-orchestrator` 게이트로 종료
> (data/doc/spec-change의 도메인 validator와 대칭). 문서/데이터 변경은 각 도메인 소관
> — code-change는 **코드 변경 전용**.

## data-change/ (4) — 기존 데이터 산출물 증분 수정/참조무결성 삭제 + 자가치유 (생성 아님; 도메인 생성기·검증기에 위임)
| name | invokes |
|------|---------|
| data-change-orchestrator *(new)* | data-modifier, data-remover |
| data-remediation-orchestrator *(new, 데이터 자가치유 루프)* | data-change-orchestrator, seed-data-orchestrator, localization-orchestrator, knowledge-base-orchestrator, data-analysis-orchestrator, audit-orchestrator |
| data-modifier *(new)* | data-schema-analyzer, mock-record-generator, relationship-linker, seed-export-generator, seed-data-validator, string-extractor, catalog-translator, plural-format-handler, localization-validator, content-chunker, kb-indexer, faq-generator, onboarding-generator, glossary-generator, knowledge-base-validator, dataset-profiler, data-cleaner, data-analyzer, chart-spec-generator, insight-writer, analysis-report-generator, data-analysis-validator, ruleset-loader, clause-extractor, conformance-checker, gap-analyzer, risk-scorer, audit-report-generator, audit-validator *(domain으로 택1 세트)* |
| data-remover *(new)* | relationship-linker, seed-export-generator, seed-data-validator, plural-format-handler, localization-validator, kb-indexer, knowledge-base-validator, analysis-report-generator, data-analysis-validator, risk-scorer, audit-report-generator, audit-validator *(domain으로 택1 세트)* |

> `seed-data`·`localization`·`knowledge-base`·`data-analysis`·`audit` 오케스트레이터가 산출물을 **생성**(재실행
> 시 재-롤)하는 반면, `data-change/*`는 기존 산출물을 **읽고 델타만 upsert / 참조무결성 삭제**한다. 데이터는
> 리팩토링 대상이 아니므로 modify/delete 2연산만. 언어별 코드 작성이 아니라 도메인 생성기·검증기에 위임하며,
> 모든 변경은 도메인 validator(`seed-data-validator`/`localization-validator`/`knowledge-base-validator`/
> `data-analysis-validator`/`audit-validator`) pass로 종료. **5개 데이터 도메인 전체 지원**(각 도메인에 결정론적 validator 존재).
> data-analysis·audit는 파생 리포트라 modify=영향 슬라이스 재분석/재감사, delete=지표·규칙 제거로 동작.
> 진입점 2개: `data-change-orchestrator`(단일 변경 요청 라우팅) vs `data-remediation-orchestrator`
> (검증 실패 → data-change 외과수정 또는 도메인 재생성 → 재검증 루프; 코드의 `remediation-orchestrator`에 대응).
> **설계 노트(의도된 트레이드오프)**: `data-modifier`의 invokes가 넓은 것(5도메인 생성기·검증기 합집합)은
> "공용 트리오(변경 로직 1벌) + 5도메인 외과 수술"의 내재적 비용이다. per-domain 어댑터로 쪼개면 invokes는
> 좁아지나 modify/delete 로직이 도메인마다 중복되므로, 여기서는 공용 워커 + `domain`별 델리게이트 택1을 유지한다.

## doc-change/ (4) — 기존 산문 문서 섹션 개정/삭제 + 자가치유 (생성 아님; docwriting·proposal 생성기·게이트에 위임)
| name | invokes |
|------|---------|
| doc-change-orchestrator *(new)* | doc-modifier, doc-remover |
| doc-remediation-orchestrator *(new, 문서 자가치유 루프)* | doc-change-orchestrator, docwriting-orchestrator, proposal-orchestrator |
| doc-modifier *(new)* | doc-outline-generator, doc-draft-generator, api-guide-generator, release-notes-generator, adr-generator, doc-style-checker, scope-definer, effort-estimator, pricing-generator, proposal-drafter, proposal-validator *(doc_domain으로 택1 세트)* |
| doc-remover *(new)* | doc-outline-generator, doc-draft-generator, doc-style-checker, pricing-generator, proposal-drafter, proposal-validator *(doc_domain으로 택1 세트)* |

> `docwriting-orchestrator`·`proposal-orchestrator`가 문서를 **생성**(재실행 시 통째 재저작)하는 반면,
> `doc-change/*`는 기존 문서를 **읽고 영향 섹션만 개정 / 교차참조 지키며 삭제**한다. 산문은 리팩토링
> 대상이 아니므로 modify/delete 2연산만. `doc_domain`별 생성기(docwriting: doc-draft/api-guide/
> release-notes/adr; proposal: scope-definer/effort-estimator/pricing-generator/proposal-drafter)에
> 위임하고, 모든 변경은 도메인 게이트(docwriting=`doc-style-checker`, proposal=`proposal-validator`
> +`doc-style-checker`) pass로 종료. **대상: docwriting·proposal**(둘 다 결정론적 게이트 보유);
> 구조적 스펙(blueprint·design, 코드로 파급)은 별도.
> 진입점 2개: `doc-change-orchestrator`(단일 개정 요청 라우팅) vs `doc-remediation-orchestrator`
> (게이트 실패 → doc-change 외과수정 또는 재저작 → 재검사 루프; 상위는 `doc-pipeline-orchestrator`).

## spec-change/ (3) — 기존 설계 스펙 개정/삭제 + 코드 파급 (L2↔L3 브리지; 스펙 생성기·검증기·code-change에 위임)
| name | invokes |
|------|---------|
| spec-change-orchestrator *(new)* | spec-modifier, spec-remover |
| spec-modifier *(new)* | architecture-generator, domain-model-generator, database-generator, api-spec-generator, event-topology-generator, blueprint-validator, design-tokens-generator, design-system-generator, ux-flow-generator, wireframe-generator, figma-to-component, design-validator, code-change-orchestrator, validation-orchestrator *(spec_domain으로 택1 세트)* |
| spec-remover *(new)* | database-generator, api-spec-generator, design-system-generator, blueprint-validator, design-validator, code-change-orchestrator, validation-orchestrator *(spec_domain으로 택1 세트)* |

> `blueprint-orchestrator`·`design-orchestrator`가 스펙을 **생성**하는 반면, `spec-change/*`는 기존
> 스펙을 **읽고 요소만 개정/삭제한 뒤 코드로 파급**한다. 스펙은 코드가 의존하는 계약이라 변경은 2단:
> ① 스펙 요소 개정(blueprint/design 생성기) → 스펙 게이트(`blueprint-validator`/`design-validator`)
> → ② 의존 코드 파급(`code-change`) → 코드 게이트(`validation-orchestrator`). 즉 L2(스펙)↔L3(코드)
> 브리지이며, code/data/doc-change가 산출물 내부만 다루는 것과 달리 **계층을 가로지른다**.

## deployment/ (3) — 배포 (컨테이너 없음: CI/CD + 스크립트 + 환경설정)
deployment-orchestrator *(new)*, cicd-generator *(new)*, env-config-generator *(new)*

## research/ (10)
research-orchestrator, web-search, docs-search, github-search, news-search,
web-research, compare-sources, fact-check, source-validation *(fix: was search-validation)*, summarize

## docwriting/ (8) — 문서/산출물 작성 (앱 생성과 독립, docs-analyze 입력 재활용)
| name | invokes |
|------|---------|
| docwriting-orchestrator *(new)* | docs-analyze-* (docx/pptx/xlsx/markdown/pdf), doc-outline-generator, doc-draft-generator, api-guide-generator, release-notes-generator, adr-generator, doc-style-checker, doc-translator |
| doc-outline-generator *(new)* | — |
| doc-draft-generator *(new)* | — |
| api-guide-generator *(new)* | — |
| release-notes-generator *(new)* | — |
| adr-generator *(new)* | — |
| doc-style-checker *(new)* | — |
| doc-translator *(new)* | — |

## audit/ (8) — 문서 규정 준수 감사 (앱 생성과 독립, docs-analyze 입력 재활용)
| name | invokes |
|------|---------|
| audit-orchestrator *(new)* | docs-analyze-* (docx/pptx/xlsx/markdown/pdf), ruleset-loader, clause-extractor, conformance-checker, gap-analyzer, risk-scorer, audit-report-generator, audit-validator |
| ruleset-loader *(new)* | — |
| clause-extractor *(new)* | — |
| conformance-checker *(new)* | — |
| gap-analyzer *(new)* | — |
| risk-scorer *(new)* | — |
| audit-report-generator *(new)* | — |
| audit-validator *(new)* | — |

## proposal/ (7) — RFP → 제안서 (앱 생성과 독립, docs-analyze 입력 재활용)
| name | invokes |
|------|---------|
| proposal-orchestrator *(new)* | docs-analyze-* (docx/pptx/xlsx/markdown/pdf), rfp-analyzer, scope-definer, effort-estimator, pricing-generator, proposal-drafter, proposal-validator |
| rfp-analyzer *(new)* | — |
| scope-definer *(new)* | — |
| effort-estimator *(new)* | — |
| pricing-generator *(new)* | — |
| proposal-drafter *(new)* | — |
| proposal-validator *(new)* | — |

## asset/ (7) — 2D 비주얼 에셋 생성 (앱 생성과 독립, design→frontend에 이미지 공급)
| name | invokes |
|------|---------|
| asset-orchestrator *(new)* | docs-analyze-* (docx/pdf/pptx), asset-brief-analyzer, icon-generator, sprite-sheet-generator, placeholder-image-generator, image-prompt-generator, asset-manifest-generator |
| asset-brief-analyzer *(new)* | — |
| icon-generator *(new)* | — |
| sprite-sheet-generator *(new)* | — |
| placeholder-image-generator *(new)* | — |
| image-prompt-generator *(new)* | — |
| asset-manifest-generator *(new)* | — |

## seed-data/ (6) — 시드/목 데이터 생성 (앱 생성과 독립, 데모/테스트 데이터 공급)
| name | invokes |
|------|---------|
| seed-data-orchestrator *(new)* | docs-analyze-* (xlsx/csv/docx/markdown), data-schema-analyzer, mock-record-generator, relationship-linker, seed-export-generator, seed-data-validator |
| data-schema-analyzer *(new)* | — |
| mock-record-generator *(new)* | — |
| relationship-linker *(new)* | — |
| seed-export-generator *(new)* | — |
| seed-data-validator *(new)* | — |

## data-analysis/ (8) — 데이터 분석·리포팅 (앱 생성과 독립, docs-analyze/xlsx + web/chart 재활용)
| name | invokes |
|------|---------|
| data-analysis-orchestrator *(new)* | docs-analyze-* (xlsx/csv/markdown), dataset-profiler, data-cleaner, data-analyzer, chart-spec-generator, insight-writer, analysis-report-generator, data-analysis-validator |
| dataset-profiler *(new)* | — |
| data-cleaner *(new)* | — |
| data-analyzer *(new)* | — |
| chart-spec-generator *(new)* | — |
| insight-writer *(new)* | — |
| analysis-report-generator *(new)* | — |
| data-analysis-validator *(new)* | — |

## knowledge-base/ (7) — 문서 코퍼스 → 지식 아티팩트 (앱 생성과 독립, docs-analyze 재활용)
| name | invokes |
|------|---------|
| knowledge-base-orchestrator *(new)* | docs-analyze-* (docx/pptx/markdown/pdf/xlsx), content-chunker, kb-indexer, faq-generator, onboarding-generator, glossary-generator, knowledge-base-validator |
| content-chunker *(new)* | — |
| kb-indexer *(new)* | — |
| faq-generator *(new)* | — |
| onboarding-generator *(new)* | — |
| glossary-generator *(new)* | — |
| knowledge-base-validator *(new)* | — |

## localization/ (5) — 제품 문자열 현지화 (앱 생성과 독립, web/i18n 연계)
| name | invokes |
|------|---------|
| localization-orchestrator *(new)* | docs-analyze-* (xlsx/markdown), string-extractor, catalog-translator, plural-format-handler, localization-validator |
| string-extractor *(new)* | — |
| catalog-translator *(new)* | — |
| plural-format-handler *(new)* | — |
| localization-validator *(new)* | — |

## game-master/ (7) — TRPG 세션 준비 (여가, 앱 생성과 독립)
| name | invokes |
|------|---------|
| game-master-orchestrator *(new)* | docs-analyze-* (markdown/pdf/docx), world-builder, npc-generator, quest-generator, encounter-generator, session-outliner, lore-consistency-checker |
| world-builder *(new)* | — |
| npc-generator *(new)* | — |
| quest-generator *(new)* | — |
| encounter-generator *(new)* | — |
| session-outliner *(new)* | — |
| lore-consistency-checker *(new)* | — |

## story-studio/ (7) — 창작 소설 (여가, 앱 생성과 독립)
| name | invokes |
|------|---------|
| story-studio-orchestrator *(new)* | docs-analyze-* (markdown/docx), premise-developer, character-designer, plot-outliner, chapter-drafter, style-tuner, narrative-continuity-checker |
| premise-developer *(new)* | — |
| character-designer *(new)* | — |
| plot-outliner *(new)* | — |
| chapter-drafter *(new)* | — |
| style-tuner *(new)* | — |
| narrative-continuity-checker *(new)* | — |

## trip-planner/ (7) — 여행 계획 (여가, research 재활용, 앱 생성과 독립)
| name | invokes |
|------|---------|
| trip-planner-orchestrator *(new)* | research-orchestrator, destination-profiler, itinerary-builder, logistics-planner, budget-estimator, packing-list-generator, trip-feasibility-validator |
| destination-profiler *(new)* | — |
| itinerary-builder *(new)* | — |
| logistics-planner *(new)* | — |
| budget-estimator *(new)* | — |
| packing-list-generator *(new)* | — |
| trip-feasibility-validator *(new)* | — |

## recipe-kitchen/ (6) — 집밥/요리 (여가, 앱 생성과 독립)
| name | invokes |
|------|---------|
| recipe-kitchen-orchestrator *(new)* | pantry-analyzer, recipe-developer, meal-planner, shopping-list-generator, nutrition-balancer |
| pantry-analyzer *(new)* | — |
| recipe-developer *(new)* | — |
| meal-planner *(new)* | — |
| shopping-list-generator *(new)* | — |
| nutrition-balancer *(new)* | — |

## quiz-forge/ (6) — 퀴즈/트리비아 (여가, 앱 생성과 독립)
| name | invokes |
|------|---------|
| quiz-forge-orchestrator *(new)* | quiz-blueprint-planner, question-generator, distractor-designer, answer-key-builder, quiz-fairness-validator |
| quiz-blueprint-planner *(new)* | — |
| question-generator *(new)* | — |
| distractor-designer *(new)* | — |
| answer-key-builder *(new)* | — |
| quiz-fairness-validator *(new)* | — |

## fitness-coach/ (6) — 운동/트레이닝 (여가, 교육용, 앱 생성과 독립)
| name | invokes |
|------|---------|
| fitness-coach-orchestrator *(new)* | fitness-profiler, program-designer, workout-builder, progression-planner, training-safety-validator |
| fitness-profiler *(new)* | — |
| program-designer *(new)* | — |
| workout-builder *(new)* | — |
| progression-planner *(new)* | — |
| training-safety-validator *(new)* | — |

## event-planner/ (6) — 파티/모임 호스팅 (여가, 앱 생성과 독립)
| name | invokes |
|------|---------|
| event-planner-orchestrator *(new)* | event-brief-analyzer, theme-designer, menu-activity-planner, run-of-show-builder, event-feasibility-validator |
| event-brief-analyzer *(new)* | — |
| theme-designer *(new)* | — |
| menu-activity-planner *(new)* | — |
| run-of-show-builder *(new)* | — |
| event-feasibility-validator *(new)* | — |

## media-curator/ (6) — 영화/TV/도서 큐레이션 (여가, research 재활용, 앱 생성과 독립)
| name | invokes |
|------|---------|
| media-curator-orchestrator *(new)* | research-orchestrator, taste-profiler, title-finder, recommender, watch-order-planner, media-fit-validator |
| taste-profiler *(new)* | — |
| title-finder *(new)* | — |
| recommender *(new)* | — |
| watch-order-planner *(new)* | — |
| media-fit-validator *(new)* | — |

## music-curator/ (6) — 플레이리스트 큐레이션 (여가, research 재활용, 앱 생성과 독립)
| name | invokes |
|------|---------|
| music-curator-orchestrator *(new)* | research-orchestrator, music-taste-profiler, track-finder, playlist-sequencer, playlist-annotator, playlist-flow-validator |
| music-taste-profiler *(new)* | — |
| track-finder *(new)* | — |
| playlist-sequencer *(new)* | — |
| playlist-annotator *(new)* | — |
| playlist-flow-validator *(new)* | — |

---

## 스킬 간 책임 경계 (중복 방지 규칙)
- **backend 멀티스택**: 세 폴더 `spring/`·`nestjs/`·`django/`는 **모두 `category: backend`** (폴더=스택, category=계층). 즉 backend는 폴더 3개짜리 단일 카테고리(58 스킬). `backend-orchestrator`는 **라우터** — `target_stack.backend` ∈ {spring, nestjs, django}로 `spring-backend-orchestrator`/`nestjs-backend-orchestrator`/`django-backend-orchestrator` 중 **하나만** 위임. 세 스택은 동일한 blueprint(domain-model·database·api-spec·event-topology) 계약을 공유하고, 구현은 각 스택 senior-programmer(spring/nestjs/django)가 담당. `feature-orchestrator`는 변경 없이 `backend-orchestrator`만 호출.
- **스택별 역량 대응**(같은 역량, 다른 관용구): event→ `event-generator`(Spring)/`nestjs-event-generator`(EventEmitter2)/`django-signals-generator`(signals); messaging→ messaging/`nestjs-messaging-generator`/`django-celery-generator`; batch→ batch/`nestjs-queue-generator`(BullMQ)/`django-task-generator`(management command); scheduler→ scheduler/`nestjs-scheduler-generator`/`django-scheduler-generator`(Celery beat); api-docs→ springdoc/`nestjs-api-docs-generator`(Nest Swagger)/`django-api-docs-generator`(drf-spectacular); config→ config-properties/`nestjs-config-generator`/`django-settings-generator`. 이름은 스택 프리픽스로 구분되어 충돌 없음.
- **api-generator**(backend, 런타임 코드) ↔ **api-spec-generator**(blueprint, 설계 문서) ↔ **api-docs-generator**(런타임 springdoc/Swagger 애노테이션) ↔ **api-guide-generator**(docwriting, 개발자용 산문 사용 가이드): 넷 다 별개. 코드→애노테이션은 api-docs, 설계 계약은 api-spec, 사람이 읽는 가이드는 api-guide.
- **doc-style-checker**(docwriting, 산문 톤/용어/일관성 검증) ↔ **validator/***(코드 산출물 검증): 문서는 전자, 코드는 후자.
- **docwriting/***(신규 카테고리): 코드/요구사항/변경분/결정 → 사람이 읽는 문서(가이드·매뉴얼·릴리스노트·ADR). 앱 생성 파이프라인과 독립이며 입력단은 **docs-analyze/*** 파서를 재활용. 런타임 코드는 절대 생성하지 않음.
- **audit/***(신규 카테고리): 대상 문서 + 룰셋(규제·정책·표준·체크리스트) → 준수 갭 리포트(verdict/finding/risk). 앱 생성과 독립이며 입력단은 **docs-analyze/*** 재활용. 대상 문서를 **평가만** 하고 수정/코드 생성은 안 함.
- **audit/conformance-checker**(문서가 규칙을 충족하는지 평가) ↔ **validator/***(코드 산출물 검증) ↔ **security-validator**(코드 OWASP). 규제/정책 문서 준수는 audit, 코드는 validator.
- **audit** 내부 소유권: 규칙 정규화=ruleset-loader, 대상 문서 절 추출=clause-extractor, 충족 판정=conformance-checker, 갭 서술·개선안=gap-analyzer, 위험 점수=risk-scorer, 리포트 조립=audit-report-generator. 서로 역할을 침범하지 않음.
- **proposal/***(신규 카테고리): RFP → 스코프·공수·가격·제안서. 앱 생성과 독립이며 입력단은 **docs-analyze/*** 재활용. **사전영업(pre-sales) 스코핑**이며 런타임 코드나 실행 태스크 그래프는 생성하지 않음.
- **proposal/scope-definer + effort-estimator**(사전영업 스코프·공수 산정) ↔ **project-planner**(앱 파이프라인의 실행용 epic/feature/story/task 분해): 전자는 제안 단계, 후자는 실행 계획. 별개.
- **proposal-drafter**(제안서 조립)는 **docwriting/*** 문서 생성기와 별개 — proposal 전용이며 docwriting 스킬을 호출하지 않음.
- **proposal** 내부 소유권: RFP 해석=rfp-analyzer, 스코프 정의=scope-definer, 공수 산정=effort-estimator, 가격 산출=pricing-generator, 문서 조립=proposal-drafter.
- **asset/***(신규 카테고리): 실제 2D 이미지 파일/마크업(SVG 아이콘·스프라이트 시트·플레이스홀더) 생성. 벡터/절차적은 **직접 저작**(외부 모델 불필요), 래스터/사실적은 연결된 이미지 도구에 위임하되 없으면 `image-prompt-generator`가 **프롬프트 스펙까지만** 산출. `design/*`(디자인 시스템·토큰·와이어프레임=스펙)과 별개이며 asset은 그 산출물을 스타일 입력으로 소비해 `web/*`(public/)에 공급.
- **asset** 내부 소유권: 스펙 정규화=asset-brief-analyzer, SVG 아이콘=icon-generator, 스프라이트=sprite-sheet-generator, 플레이스홀더=placeholder-image-generator, 래스터 프롬프트=image-prompt-generator, 매니페스트·검증=asset-manifest-generator.
- **seed-data/***(신규 카테고리): 스키마를 채우는 **데이터 행**(SQL/JSON/CSV fixture) 생성. `spring/migration-generator`(스키마/DDL·Flyway)와 별개 — migration은 스키마, seed-data는 그 스키마를 채우는 데이터. seed는 `options.seed`로 결정론적.
- **seed-data** 내부 소유권: 스키마 분석=data-schema-analyzer, 레코드 생성(FK 제외)=mock-record-generator, FK 연결=relationship-linker, 직렬화=seed-export-generator, 무결성 검증=seed-data-validator. `seed-data-validator`(데이터 무결성)는 `validator/*`(코드 검증)와 별개.
- **data-analysis/***(신규 카테고리): 테이블 데이터 → 프로파일·정제·분석·차트 스펙·인사이트 리포트. `chart-spec-generator`(차트 **스펙**)는 `web/chart-generator`(실제 React 차트 코드)와 별개 — 스펙은 전자, 렌더는 후자(design→frontend와 동일 분리). 앱 생성과 독립, `docs-analyze/xlsx` 재활용.
- **knowledge-base/***(신규 카테고리): 내부 문서 코퍼스 → 청킹·인덱싱 후 FAQ·온보딩·용어집. `research/*`(외부 웹 소스+팩트체크)·`docwriting/*`(단일 문서 저작)와 별개 — KB는 내부 코퍼스를 재사용 가능한 지식으로 조직. 모든 아티팩트는 chunk `source_refs` 인용.
- **localization/***(신규 카테고리): 제품 문자열/메시지 카탈로그 추출→번역→복수·포맷→검증. `docwriting/doc-translator`(산문 문서 번역)·`web/i18n-generator`(런타임 i18n 배선/코드)와 별개 — localization은 **번역된 카탈로그**를 산출(코드 아님). `catalog-translator`(키-값+플레이스홀더)는 `doc-translator`(산문)와 구분.
- **localization-validator**(카탈로그 완전성/플레이스홀더 패리티) ↔ `validator/*`(코드) ↔ `seed-data-validator`(데이터): 각자 다른 산출물 검증.
- **여가 도메인 3종**(game-master·story-studio·trip-planner): 업무용과 동일한 오케스트레이터+워커+검증 패턴이나 산출물이 놀이/창작/여행 계획. 모두 앱 생성과 독립.
- **연속성/일관성 검증기 3종 명명 분리**: `lore-consistency-checker`(game-master, 로어·밸런스) ↔ `narrative-continuity-checker`(story-studio, 타임라인·인물) ↔ `trip-feasibility-validator`(trip-planner, 이동시간·영업시간). 도메인별 별개, 이름 충돌 없음.
- **story-studio ↔ docwriting**: story-studio는 **픽션**(premise→chapter), docwriting은 기술/업무 문서. `style-tuner`(픽션 문체)는 `doc-style-checker`(문서 톤/용어)와 별개.
- **trip-planner ↔ research**: trip-planner-orchestrator가 `research-orchestrator`를 호출해 목적지 사실을 수집(교차 도메인 재활용). `budget-estimator`(여행 추정가)는 `proposal/pricing-generator`(제안 견적)와 별개.
- **여가 도메인 추가 6종**(recipe-kitchen·quiz-forge·fitness-coach·event-planner·media-curator·music-curator): 업무용과 동일 패턴(오케스트레이터+워커+검증기). 모두 앱 생성과 독립, 순수 텍스트/플랜 산출.
- **research 재활용 3종**: trip-planner·media-curator·music-curator가 `research-orchestrator`를 호출해 실제 사실/타이틀/트랙을 수집. 근거 없는 생성 금지, 출처 인용.
- **media-curator ↔ music-curator**: 전자는 시청/독서(영화·TV·도서), 후자는 청취(트랙·플레이리스트). `taste-profiler`(media) ↔ `music-taste-profiler`(music), `title-finder`(media) ↔ `track-finder`(music) 별개.
- **여가 검증기**는 각 도메인 전용: nutrition-balancer(영양)·quiz-fairness-validator(퀴즈 공정성)·training-safety-validator(운동 안전)·event-feasibility-validator(행사 실현성)·media-fit-validator(시청 제약)·playlist-flow-validator(재생 흐름). 모두 `validator/*`(코드)와 별개.
- **fitness-coach**는 일반 교육용이며 의료 조언이 아님(안전 검증기·오케스트레이터에 명시). **recipe-kitchen** 영양은 정성적 추정(정확 열량은 별도 도구).
- **명명 재사용 주의(도메인 스코프)**: `question-generator`(quiz-forge)는 `quest-generator`(game-master)와 철자·역할 모두 별개. `shopping-list-generator`(recipe-kitchen)·`taste-profiler`(media-curator)·`theme-designer`(event-planner)는 각 도메인 고유.
- **event-generator**(인프로세스 Spring 이벤트) ↔ **messaging-generator**(브로커) ↔ **websocket-generator**(클라이언트 대면 실시간). Redis Pub/Sub은 **messaging-generator 소유**.
- **scheduler-generator**(스케줄) ↔ **batch-generator**(대량 처리 잡). 스케줄 트리거는 scheduler 소유.
- **integration-generator**(범용 외부 HTTP 전송)에서 분리: 이메일/SMS/푸시는 **notification-generator 소유**, 파일/오브젝트 스토리지(S3/GCS/Azure)는 **file-storage-generator 소유**.
- **spring-initializer**(기본 logback·profile·application.yml 스캐폴드) ↔ **observability-generator**(구조적 로깅·메트릭·트레이싱·헬스) / **config-properties-generator**(피처별 타입 config). 스캐폴드는 initializer, 확장은 각 전용 스킬.
- 프론트 데이터 계층: **api-client-generator**(HTTP 클라이언트/타입) → **data-generator**(TanStack Query 훅) → **state-generator**(전역/UI 상태) → **hook-generator**(그 외 커스텀 훅). 태그는 `tanstack-query`로 통일.
- **realtime-client-generator**(push/subscription 채널)는 **data-generator**(요청/응답 쿼리 훅)와 별개. 실시간 수신분은 TanStack Query 캐시에 반영.
- **middleware-generator**(엣지 `middleware.ts`: 인증/리다이렉트/로케일 라우팅) ↔ **auth-generator**(클라이언트 세션/가드) ↔ **i18n-generator**(번역). middleware는 로케일 *라우팅*만.
- **toast-notification-generator**(비차단 임시 피드백) ↔ **dialog-generator**(차단형 모달).
- **theme-generator**(런타임 provider/switcher/다크모드) ↔ **design-tokens-generator**(light/dark 토큰 값).
- **design-orchestrator**가 design/ 5종을 조율해 `design_system`(tokens+system, +선택 flows/wireframes)을 산출 → **frontend-orchestrator**가 이를 입력으로 소비. design/ 산출물은 계약/스펙/아티팩트일 뿐 `.tsx` 코드는 frontend 생성기 몫.
- **app-orchestrator** 파이프라인 순서: blueprint-orchestrator → **design-orchestrator** → project-planner → feature-orchestrator → … → review-orchestrator → **deployment-orchestrator**(선택). 앱 레벨 디자인 파운데이션(tokens+system)은 1회 생성 후 전 피처 재사용.
- **event-topology-generator**(blueprint, 설계 시점 이벤트/메시징 토폴로지) ↔ 런타임 생성기: **event-generator**(인프로세스) / **messaging-generator**(브로커) / **websocket-generator**(클라이언트 대면). 토폴로지가 어느 생성기가 소유할지를 결정.
- **deployment/**(신규 카테고리, 컨테이너 없음): **cicd-generator**(빌드/테스트/배포 파이프라인+스크립트) + **env-config-generator**(환경별 env 템플릿/시크릿 매핑). 배포 대상은 사용자 인프라에 위임(deploy-hook).
- **env-config-generator**(배포/런타임 env 변수·시크릿 주입) ↔ **config-properties-generator**(Java `@ConfigurationProperties` 타입 바인딩) ↔ **spring-initializer**(기본 application.yml 스캐폴드). 앞의 것이 값을 공급, 뒤의 둘이 소비.
- **dependency-license-validator**(의존성 CVE/라이선스/버전) ↔ **security-validator**(코드 보안/OWASP). 공급망은 전자, 코드 취약점은 후자.
- **api-client-generator**는 frontend-orchestrator만 생성한다(feature-orchestrator가 직접 부르는 integration-generator는 외부 HTTP 전송만; 중복 생성 금지).
- **feature-orchestrator**가 `integration-generator`를 직접 호출한다(얇은 integration-orchestrator 계층은 제거됨). 초기화(`spring-initializer`/`nextjs-initializer`)는 **app-orchestrator**가 feature 루프 이전 1회 실행.
- **클라이언트 멀티타깃**: 세 폴더 `web/`·`desktop/`·`mobile/`는 **모두 `category: frontend`** (폴더=타깃, category=계층). 즉 frontend는 폴더 3개짜리 단일 카테고리(42 스킬). `target_stack.clients`로 선택(기본 `[web]`): `web`=`web/*`(Next.js) ↔ `desktop`=`desktop/*`(Tauri) ↔ `mobile`=`mobile/*`(Flutter). backend(택1)와 달리 clients는 **복수 공존 가능**. `app-orchestrator`가 웹 feature 루프 완료 후 4b 단계에서 선택된 클라이언트 오케스트레이터(`desktop-orchestrator`/`mobile-orchestrator`)를 실행. 웹은 `frontend-orchestrator`가 담당(이름 유지).
- **desktop/**(신규 카테고리, Tauri): **UI 생성기를 만들지 않는다** — Tauri가 `web/*` React 산출물을 그대로 래핑. `desktop/*`는 네이티브 쉘(`desktop-shell-generator`)·IPC(`native-bridge-generator`)·로컬 저장(`desktop-storage-generator`)·자동 업데이트(`desktop-updater-generator`)·패키징(`desktop-packaging-generator`, dmg/msi/AppImage)·테스트만. 스캐폴드는 `tauri-initializer`. 컨테이너 없음.
- **native-bridge-generator**(Tauri command: fs/dialog/notification 등 OS 기능)는 서버 HTTP와 별개 — 서버 통신은 재사용된 웹 `api-client-generator` 산출물이 담당.
- **mobile/**(신규 카테고리, Flutter): **자체 Dart/Flutter UI 생성**(React 재사용 안 함). `design-tokens` 값(→`flutter-theme-generator`, Material 3)과 backend `api-spec`(→`flutter-api-client-generator`, Dio+Freezed)만 계약으로 재사용. 구현 위임은 `flutter-senior-programmer`(생성기가 위임; 오케스트레이터 invokes 아님 — `spring-senior-programmer`/`typescript-senior-programmer`와 동일 패턴).
- **mobile 이름 충돌 방지**: mobile 스킬은 전부 `flutter-*`/`mobile-*` 접두사. `flutter-state-generator`(Riverpod) ↔ `state-generator`(frontend, React), `flutter-api-client-generator`(Dio) ↔ `api-client-generator`(frontend, fetch), `flutter-theme-generator` ↔ `theme-generator`, `flutter-form-generator` ↔ `form-generator` 모두 별개.
- **초기화 소유권 4종**: `spring-initializer`(backend) · `nextjs-initializer`(web) · `tauri-initializer`(desktop) · `flutter-initializer`(mobile). 서로 별개이며 각 스택 스캐폴드만 담당.
