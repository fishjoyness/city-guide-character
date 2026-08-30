# Quality Score — city-guide-character v0.2

| Dimension | Score | Evidence | Gap |
|---|---:|---|---|
| Purpose Clarity | 10/10 | `SKILL.md` Purpose defines one optional, subordinate city-map guide character. | None. |
| Scope | 10/10 | IN/OUT boundaries exclude personal IP, attraction art, animation, central hero art, runtime code, and uncontrolled batch production while allowing controlled cross-city pose review. | None. |
| Trigger Precision | 15/15 | Frontmatter names city character, guide role, placement, STYLE TEST, QA, and body-template repetition intents. | None. |
| False Trigger Resistance | 10/10 | Frontmatter and non-trigger evals distinguish personal IP, attraction stickers, and implementation work. | None. |
| Workflow | 15/15 | Seven phases cover style inheritance, city cues, pre-generation pose lock, safe placement, prompt, generation, individual QA, and cross-city pose QA. | None. |
| Input / Output Contract | 10/10 | Required style/map context, `POSE_SIGNATURE`, placement config, prompt, transparent PNG, QA, and hidden fallback are explicit. | None. |
| Reliability | 10/10 | Unapproved style, unsafe layout, stereotypes, unavailable tools, and hierarchy failure each have a defined fallback. | None. |
| Maintainability | 10/10 | Pose enums, Manifest schema, prompt repair, deterministic chroma cleanup, showcase builder, and QA rules are separated from the preserved style system. | None. |
| Context Efficiency | 5/5 | `SKILL.md` loads only the phase-specific reference and reuses the companion PNG inspector. | None. |
| Testability | 5/5 | Evals include 7 normal, 4 edge, and 3 non-trigger cases, including body-template repetition and the 70% face-direction threshold; four revised characters include detail, alpha inspection, 14% previews, and a horizontal review. | Runtime integration remains out of scope. |
| **Total** | **100/100** | Skill is structurally complete for v0.2 and the four-city pose-diversity forward test passes. | Production approval remains a user decision. |

## Validation evidence

- Built-in `quick_validate.py`: PASS.
- Skill Architect `validate_skill.py` with eval file and duplicate scan: PASS, 0 errors, 0 warnings.
- Example JSON and relative-link scan: PASS.
- Companion `inspect_sticker.py --self-test`: PASS.
- Automatic revision: none required after UTF-8 metadata correction.
- Forward test: Shanghai, Guilin, Nanjing, and Beijing revised candidates, transparent masters, visible-alpha bounds, detail previews, exact 14% viewport previews, and horizontal `CROSS_CITY_POSE_REVIEW` created; no production integration performed.
- Pose review: all six diversity gates and `SAME_SYSTEM_DIFFERENT_CHARACTER` pass; repeated `both-hands-center-hold` is absent.
