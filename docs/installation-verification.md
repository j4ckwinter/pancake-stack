# Installation verification

The [Codex installation and refresh recipe](codex-installation.md) was tested on Codex CLI 0.160.0 on 14 October 2026. A local checkout installed 0.21.6, refreshed to 0.21.7 after a fast-forward pull and repeated add, and retained matching cached manifest and skill resources. A further add at 0.21.7 preserved those resources. The tested versions have identical skill contents, so this establishes version refresh and resource identity, not replacement of changed skill text. See the [refresh evidence](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/codex-refresh.md).

Version 0.21.8 adds Design candidate-isolation guidance and updates verification documentation. Its source-skill and package checks are described in [verification](verification.md). The refresh experiment above is not an installed 0.21.8 workflow trial.

Version 0.21.3 installed in separate temporary profiles on Codex 0.160.0 and Claude Code 2.1.291 on 9 October 2026. Both hosts discovered all 19 namespaced skills, and installed manifests and skill resources matched the tested source. No global configuration changed.

Fresh installed Codex trials completed a compatibility migration with one default independent reviewer and a read-only Challenge with two requested reviewers. Trusted artifact checks passed. Claude authenticated workflows and visible app picker behavior remain unverified. These scoped checks do not cover every skill or host configuration.

The detailed historical record remains in [pancake-stack-evals](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/installation-verification.md) and [source history](https://github.com/j4ckwinter/pancake-stack/blob/795dc890ee0b0acf24e743d82362c4a92e4202e1/docs). The [installed reviewer report](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/reviewer-consolidation.md) and its [evidence](https://github.com/j4ckwinter/pancake-stack-evals/blob/main/docs/evidence/reviewer-consolidation-2026-10-09.json) retain the newer trials. See [verification](verification.md) for current checks and evidence limits.
