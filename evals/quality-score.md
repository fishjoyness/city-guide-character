# Quality Score — city-guide-character v0.1

| Dimension | Score | Evidence | Gap |
|---|---:|---|---|
| Purpose Clarity | 10/10 | `SKILL.md` Purpose defines one optional, subordinate city-map guide character. | None. |
| Scope | 10/10 | IN/OUT boundaries exclude personal IP, attraction art, animation, central hero art, runtime code, and batch production. | None. |
| Trigger Precision | 15/15 | Frontmatter names city character, guide role, corner atmosphere, placement, STYLE TEST, and QA intents. | None. |
| False Trigger Resistance | 10/10 | Frontmatter and non-trigger evals distinguish personal IP, attraction stickers, and implementation work. | None. |
| Workflow | 15/15 | Seven phases cover style inheritance, city cues, safe placement, prompt, optional generation, QA, and delivery. | None. |
| Input / Output Contract | 10/10 | Required style/map context, locks, placement config, prompt, optional PNG, QA, and hidden fallback are explicit. | None. |
| Reliability | 10/10 | Unapproved style, unsafe layout, stereotypes, unavailable tools, and hierarchy failure each have a defined fallback. | None. |
| Maintainability | 10/10 | Character, research, placement, data/assets, prompt, and QA rules are separated; shared style and the 4–4.5-head base system are versioned. | None. |
| Context Efficiency | 5/5 | `SKILL.md` loads only the phase-specific reference and reuses the companion PNG inspector. | None. |
| Testability | 5/5 | Evals include 6 normal, 3 edge, and 3 non-trigger cases; Shanghai and Guilin forward tests include detail and exact 14% map previews. | Runtime integration remains out of scope. |
| **Total** | **100/100** | Skill is structurally complete for v0.1 and has two city-differentiation forward tests. | Production approval remains a user decision. |

## Validation evidence

- Built-in `quick_validate.py`: PASS.
- Skill Architect `validate_skill.py` with eval file and duplicate scan: PASS, 0 errors, 0 warnings.
- Example JSON and relative-link scan: PASS.
- Companion `inspect_sticker.py --self-test`: PASS.
- Automatic revision: none required after UTF-8 metadata correction.
- Forward test: Shanghai and Guilin experimental candidates, transparent masters, visible-alpha bounds, detail previews, and exact 14% viewport previews created; no production integration performed.
