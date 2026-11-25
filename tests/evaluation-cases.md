# Evaluation cases (synthetic, proposed; not executed)

Evaluate the workbook against the original prompt. Record tool availability, actual tests, outputs and exceptions. Do not label planned checks as passed.

## A — Investment timing
Synthetic case: investment 100 at t=0, construction during years 0–1, operating net free cash flows of 60 at each year-end 2 and 3, discount rate 10% annually. No terminal value. Expected NPV: -100 + 60/1.1^2 + 60/1.1^3 ≈ -5.33. Check no revenue during construction, time alignment and two equivalent NPV calculations.

## B — Working capital
Synthetic annual revenue 365, annual COGS 182.5, 30 receivable days, 40 inventory days, 20 payable days, 365-day year. Expected AR 30, inventory 20, AP 10, operating working capital 40. Check roll-forward and cash-flow signs.

## C — Scenario and integrity
Change a material input, observe linked changes in results and scenario summary, then restore delivery scenario. Check source ledger, formula integrity, balance sheet balance when applicable, cash tie-out, and visual readability.

## D — Missing data
Supply an investment case without reliable discount rate or operating costs. Mark missing assumptions and affected outputs; do not fabricate sources or pretend the model is fully validated.
