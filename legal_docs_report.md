# Legal Docs Compliance Report — 2026-09-06

## Overall status

**NEEDS_FIX (documents refreshed; source-code compliance blockers remain)**

The legal text has been rebuilt from a single canonical fact matrix and localized for every currently supported locale of the active apps. This removes the major wording inconsistencies found in the previous documents. However, a legal notice cannot cure an implementation problem. Confirmed automatic Firebase guest accounts require a compliant deletion path in the affected apps before the portfolio should be described as fully store-compliant.

## Active portfolio and locale matrix

| App / legal folder | Source repo | Supported legal locales after this change |
| --- | --- | --- |
| Clusters / Four Clues — `clusters` | `icon_groups` | cs, de, el, en, es, fr, hu, id, it, nl, pl, pt, pt_BR, ro, tr |
| SzámKirakó / Number Puzzle — `number_puzzle` | `number_puzzle` | cs, de, el, en, es, fr, hu, id, it, ja, ko, nl, pl, pt, pt_BR, ro, tr |
| Kódfejtő / Cryptogram — `cryptogram` | `cryptogram` | el, en, hu, it, ro |
| Magnet Grid — `magnet_grid` | `MagnetGrid` | ar, cs, da, de, el, en, es, fi, fr, hi, hu, id, it, ja, ko, nb, nl, pl, pt, pt_BR, ro, ru, sv, th, tr, uk, vi, zh, zh_TW |
| Heti Menü / Meal Planner — `household` | `MealPlan` | en, hu |
| Word Album — `word_album` | current source repository unavailable/empty at audit time | el, en, hu, it, ro |

`quest_word_search` is excluded from the active portfolio at the user's instruction. It remains legacy-only until old live links are confirmed unused.

## What was already good

- Every app used separate public Privacy Policy / Manage Consent / Terms URLs.
- Controller/provider contact information was generally present.
- Existing documents already disclosed AdMob/UMP, Firebase and ATT in many relevant apps.
- Consent pages correctly stated that native UMP/ATT dialogs are the operative controls rather than the web page itself.
- Mandatory consumer-law carve-outs were already present in several Terms versions.
- The shared GitHub Pages repository gives stable store-compatible public URLs.

## Material issues found and corrected in the documents

1. **Privacy Policy treated as consent.** Phrases such as “By using the app you agree to this Privacy Policy” were removed from the canonical text. A privacy notice is transparency information; optional processing requires its own valid mechanism when consent is the legal basis.
2. **“Anonymous” used too broadly.** Firebase Auth UID, Analytics app-instance/user-pseudo IDs and similar identifiers are now described as pseudonymous technical identifiers rather than automatically anonymous data.
3. **Uninstall was too easily conflated with deletion.** New text explicitly separates local uninstall/reset from Firebase account, Firestore, analytics, advertising and provider-side records.
4. **Ad refusal was oversimplified.** The old “decline = non-personalized ads” promise was removed. The new text allows for Google's current personalized / non-personalized / limited / technical delivery modes depending on consent signals and eligibility.
5. **ATT and UMP were conflated.** They are now described as separate controls; denying ATT means IDFA cannot be used for cross-app/site tracking, but it is not described as disabling every type of advertising or analytics processing.
6. **Analytics was conflated with advertising consent.** Firebase Analytics is disclosed separately and advertising consent is not described as blanket Analytics consent.
7. **General 16+ usage limit was incorrect.** A data-protection consent age is no longer presented as a blanket minimum age for using a general-audience puzzle app.
8. **Retention periods are no longer invented.** Where a provider/configuration-specific period was not verified, the policy describes the governing purpose/configuration/security/legal criteria instead of making up a fixed number.
9. **Number Puzzle language telemetry is now disclosed.** Device locale, selected app locale, platform and the best-effort daily Firestore language-stat event are explicitly covered.
10. **Magnet Grid ATT status is preserved accurately.** Current implementation is described as not requesting ATT.
11. **Semantic parity architecture changed.** For a given locale, Privacy Policy / Manage Consent / Terms URLs point to the same canonical localized legal page and auto-scroll to the requested section. This prevents later drift between the three documents.

## Verified code facts

### Clusters
- Automatic Firebase anonymous sign-in exists for cloud sync.
- Cloud data is stored under `users/{uid}` and the cloud snapshot can include the app's SharedPreferences state.
- Current source locales match the 15-locale legal set.

### Number Puzzle
- Automatic `signInAnonymously()` is used when there is no Firebase user.
- Cloud data is stored under `users/{uid}`.
- Firebase Analytics records gameplay, ad, feedback, onboarding and cross-promo events.
- Device locale, selected app locale and platform are measured; a Firestore language-demand signal is also used.
- UMP and iOS ATT are implemented; privacy options are exposed in Settings when required.
- Current source locales match the 17-locale legal set.

### Cryptogram
- Automatic Firebase anonymous sign-in and `users/{uid}` cloud backup are present.
- Restore-code records are stored in `restore_codes/{code}`.
- AdMob, Firebase Analytics and iOS ATT dependencies are present.

### Magnet Grid
- Automatic Firebase anonymous sign-in and `users/{uid}` cloud backup are present.
- Restore codes are stored in `restore_codes/{code}`.
- AdMob/UMP and Firebase Analytics are present.
- Current source has no ATT dependency/request.
- Source localization contains 29 locales, while the previous legal repo had only EN/HU. This update fills the missing legal locale coverage.

### Heti Menü / Meal Planner
- Source dependencies include Firebase Auth/Firestore/Analytics/Remote Config/Cloud Messaging, Google/Apple sign-in, AdMob/UMP/ATT and Google APIs/Drive-related functionality.
- Current app localization is EN/HU.
- Account deletion implementation was not proven by the repository search used in this audit and must be verified before final PASS.

### Word Album
- Existing legal docs and the last accessible source configuration described Firebase Auth/Firestore/Analytics, AdMob/UMP, iOS ATT and local notifications.
- During this audit the previous `word_search` repository became unavailable and the `WordAlbum` repository is currently empty; current source behavior therefore could not be fully re-verified. The legal set is retained for its 5 known locales, but source verification remains required.

## Confirmed / remaining blockers

### BLOCKER — in-app account deletion
Confirmed automatic Firebase guest/anonymous account creation exists in Clusters, Number Puzzle, Cryptogram and Magnet Grid. Current legal text therefore does **not** pretend that an email-only route is automatically enough. Before final store-compliance PASS, each affected app must offer the account/data deletion flow required by the applicable store rules and remove associated Firestore user data/restore-code mappings as appropriate.

### BLOCKER / REVIEW — Analytics consent and Google Consent Mode
The apps use Firebase Analytics. The current Google UMP documentation supports Consent Mode and `analytics_storage` handling, but each app's actual initialization/default consent state must be verified end-to-end. A UMP advertising form alone must not be assumed to solve all analytics/ePrivacy requirements.

### REVIEW — `canRequestAds()` enforcement
Several consent services expose `canRequestAds()`. The ad request call sites must be verified to ensure ads are not requested before Google says requests are allowed in regulated regions.

### REVIEW — Meal Planner account lifecycle
Because Firebase Auth plus Google/Apple sign-in are dependencies, the account create/link/delete lifecycle and Sign in with Apple revocation behavior must be verified against the current implementation.

### REVIEW — Word Album source truth
Current source code was not available in an auditable non-empty repository at the end of this audit. Legal documents are improved, but final source-code verification is still required.

## Current official requirements checked

- EU GDPR Regulation (EU) 2016/679: transparency, lawful bases, consent, data-subject rights, erasure, international transfers.
- ePrivacy Directive 2002/58/EC Article 5(3) and EDPB guidance: terminal storage/access is a separate layer from GDPR lawful-basis analysis.
- Google Play User Data / Data Safety / account-deletion requirements.
- Google UMP for Flutter, including consent-info refresh, privacy options, `canRequestAds()`, Consent Mode and current ad-serving modes.
- Apple App Review privacy requirements, App Tracking Transparency and account deletion, including automatically created guest accounts.

## Language QA

Canonical localized pages created for the union of active locales:

`ar, cs, da, de, el, en, es, fi, fr, hi, hu, id, it, ja, ko, nb, nl, pl, pt, pt_BR, ro, ru, sv, th, tr, uk, vi, zh, zh_TW`

Each active app receives only the locale URLs its source/localization set currently supports. Default language-less `.html` aliases point to English for compatibility.

## Generator/workflow change

The revised `/legal-docs` specification is maintained separately as `legal_docs_updated.md`. Its key rule is dynamic locale discovery on every run: supported app locales are the source of truth; the language list is never hard-coded. A run cannot report SUCCESS if any currently supported locale is missing one of the three legal URLs or fails semantic parity.

## Final QA result

- Document legal framing: **PASS / substantially corrected**
- Active locale coverage: **PASS after commit**
- Semantic parity design: **PASS by canonical-per-locale architecture**
- Code truth: **PARTIAL — blockers/reviews above**
- Store declaration consistency: **REQUIRES console-by-console verification after code fixes**
- Portfolio final status: **NEEDS_FIX until code blockers are resolved**
