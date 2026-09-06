# legal

Shared, publicly hosted legal documents for active Enila Studio / App Factory apps, served via GitHub Pages.

Each active app folder contains localized URLs for:

- `privacy_policy.<locale>.html`
- `manage_consent.<locale>.html`
- `terms_of_use.<locale>.html`

The legal text is generated from one canonical fact matrix per locale so the three document URLs cannot drift semantically. Supported locales must be discovered dynamically from each app's current localization files; the list is not fixed and is expected to grow.

## Active apps

- [number_puzzle](number_puzzle/privacy_policy.hu.html) — SzámKirakó / Number Puzzle
- [magnet_grid](magnet_grid/privacy_policy.en.html) — Magnet Grid
- [word_album](word_album/privacy_policy.hu.html) — Word Album
- [clusters](clusters/privacy_policy.en.html) — Clusters / Four Clues
- [household](household/privacy_policy.hu.html) — Heti Menü / Meal Planner
- [cryptogram](cryptogram/privacy_policy.hu.html) — Kódfejtő / Cryptogram

## Legacy

`quest_word_search/` is not an active app and is intentionally excluded from the active compliance matrix. Keep or remove the legacy folder only after confirming that no released/store build still links to those URLs.

## Compliance workflow

The `/legal-docs` workflow must always audit actual app code/SDK use, current official legal/platform requirements, account deletion, UMP/ATT/Analytics behavior and semantic parity for every supported locale before publishing. A Privacy Policy must never be used to hide an implementation mismatch.