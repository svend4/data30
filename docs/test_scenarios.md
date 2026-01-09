# Test scenarios

## CRUD scenarios

### Functions
1. Create: add a new Function with a unique `id`, `module_id`, and `version`.
2. Read: retrieve by `id` and verify fields.
3. Update: change `version` and `status`.
4. Delete: remove the Function and ensure no UseCase references remain.

### Modules
1. Create: add a new Module with `status=active`.
2. Read: list modules and filter by `status`.
3. Update: change `name` and `version`.
4. Delete: ensure related Functions/UseCases are updated or blocked.

### UseCases
1. Create: add a UseCase that references existing Modules/Functions.
2. Read: verify `module_ids` and `function_ids`.
3. Update: add/remove a referenced Function.
4. Delete: remove UseCase and ensure Macros are updated or blocked.

### Macros
1. Create: add a Macro with existing UseCase references.
2. Read: verify `use_case_ids`.
3. Update: update `version` or `status`.
4. Delete: remove the Macro.

## Relationship scenarios
1. Function references Module: `functions.module_id` must exist in `modules`.
2. UseCase references Functions/Modules: `use_cases.function_ids` and `module_ids` must exist.
3. Macro references UseCases: `macros.use_case_ids` must exist.

## Versioning scenarios
1. Function version bump: update `fn_calculate_risk` from `1.1.0` to `1.2.0`.
2. Module version bump: update `mod_reporting` from `0.9.0` to `1.0.0`.
3. UseCase version alignment: update `uc_generate_report` to match `mod_reporting` version.
4. Macro version alignment: update `macro_reporting_preview` to match `uc_generate_report`.
