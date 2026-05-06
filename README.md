# LongBanana Review Code

This repository is an anonymous review code scaffold for the LongBanana
benchmark and evaluation release.

The full code package is not attached yet. The planned release will include:

- benchmark construction utilities;
- reference data validation scripts;
- evaluation harnesses for multi-reference long-horizon image generation;
- metric aggregation and table-generation scripts;
- minimal examples for reproducing the paper's reported protocol.

The repository currently contains a small executable check so reviewers can
verify that the anonymous code repository is reachable and installable.

## Quick Check

```bash
python scripts/check_review_code.py
```

Expected output:

```text
LongBanana anonymous review code is reachable.
```

## Status

This is a draft anonymous preview repository for review infrastructure testing.
The complete implementation will be added after release packaging.
