---
name: financial-modelling
description: Build, update or audit editable Excel financial models for business cases, investment appraisal, forecasting, valuation, budgets and cash flow using the user's canonical v2 modelling standards.
---
# Financial modelling (Excel)
Read [the original financial modelling prompt v2](references/Prompt_Xay_Mo_Hinh_Tai_Chinh_Excel_v2.md) in full before building, updating or auditing a model. This is the authoritative user-supplied standard. Do not replace it with slide-design rules or a generic financial template.

## Execution
1. Establish the decision, scope, model type, units, currency and timing. Ask up to three focused questions only if missing details materially change the model; otherwise state reasonable assumptions and proceed.
2. Preserve source data and record traceable sources, assumptions, missing inputs and scenario drivers. Do not invent numbers or sources.
3. Choose one aligned time axis when applicable. Create a formula-driven, editable .xlsx with summary first, inputs, operating schedules, linked statements, investment appraisal, comparisons, sensitivity and checks as appropriate to the task. Keep the scope proportionate.
4. Follow the original financial and formatting requirements: correct investment and operating timing, single-source inputs, linked calculations, project versus equity cash flows, meaningful sensitivity and checks, and no double counting.
5. Recalculate and validate if tools support it; test changed assumptions then restore the delivery scenario. Inspect the actual workbook and preview where available. Report checks run, limitations, discrepancies and any unresolved financial conventions. Never hide formula errors or claim unexecuted checks.
6. Deliver the workbook, previews when possible, concise Vietnamese interpretation and rationale, key assumption cells and Q&A preparation according to the original prompt. If .xlsx generation is unavailable, provide the specified cell-level blueprint instead.

## Guardrails
Use the original prompt as the default, adapting only to the actual case and explicit user requirements. Flag material accounting or valuation inconsistencies rather than silently applying an inappropriate convention. Do not treat NPV/equity ranking alone as proof of optimal allocation under discrete constraints; verify feasibility and the stated objective. Keep company data private. Do not install dependencies or publish model outputs without permission.
