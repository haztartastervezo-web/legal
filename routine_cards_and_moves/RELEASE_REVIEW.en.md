# Routine Cards & Moves — legal release review

## Update 2026-10-19 (afternoon) — Firebase Analytics live as opt-in, UMP connected

Folder renamed `family_cards_and_moves` → `routine_cards_and_moves` (store name). Evidence: the app repository working tree on 2026-10-19 (uncommitted changes on top of `c97d55a`).

- `analytics_service.dart` + `firebase_options.dart`: Firebase project `cardsmoves-enila` (Android + iOS). Collection is **off natively** (`firebase_analytics_collection_enabled` / `FIREBASE_ANALYTICS_COLLECTION_ENABLED` false, Consent Mode defaults denied) and turned on only after the parent's yes (`FamilyStore.analyticsConsent`, device-only; asked once when the parent area first opens; switch in Settings → Data). A later no calls `setAnalyticsCollectionEnabled(false)`, denies analytics storage and `resetAnalyticsData()`. Debug builds never collect.
- Event payloads: counts, durations, yes/no flags, built-in content ids (own content = `custom`), KIT rating as fixed code, rewarded-video outcome, backup/reset actions, rate-prompt and cross-promo ids; 3 user properties (routine-count band, has custom routine, reminders on). Never names, child labels, notes, school entries, mood answers, files, PIN, typed text, dates or a user id (mood was removed from `routine_feedback`).
- Identifiers: AD_ID / ADSERVICES permissions removed (manifest `tools:node="remove"`), `google_analytics_adid_collection_enabled` / `ssaid` false, iOS IDFV collection false, `$FirebaseAnalyticsWithoutAdIdSupport`, ad-personalisation signals false, ad storage / ad user data denied.
- AdMob: own IDs in release (test IDs in debug), non-personalised, child age treatment, G rating; UMP `gatherConsent()` before `MobileAds.initialize()`, `canRequestAds()` before every load, "Manage consent" shown when `getPrivacyOptionsRequirementStatus() == required`. No ATT prompt.

Remaining before release (see the app's `legal_docs_report.md`): link Google Analytics to the Firebase project and set event-data retention to **2 months** (the documents state 2 months), keep Google Signals and Google Ads links off; Play Data safety / Apple App Privacy answers; target-audience / Families decisions; Apple Kids Category not to be selected (third-party analytics + ads).

---

## Original review (earlier on 2026-10-19)

Reviewed October 19, 2026. This supersedes the no-advertising/no-remote-analytics assessment of October 18.

## Evidence

Authoritative Dart source: the newly uploaded `lib.zip` (SHA-256 `b7235a9807d33f18d86bacd259b101d7ad0b29ed49c4abb1ef7ec85238641c79`), rather than the older `lib 2.zip`. The developer separately confirmed that Firebase Analytics will be added for button/feature usage. The app repository at `c97d55a5961a7927da9b046a1e2eb39159838dfe` supplies additional dependency/native context; it is not proof that those native files are paired with this exact archive.

- `app_constants.dart`: display name **Routine Cards & Moves**, package `com.enila.cardsmoves`. Existing hosted routes remain unchanged.
- `main.dart` and `ad_service.dart`: Mobile Ads starts at launch, uses Google's test IDs, non-personalised requests, child age treatment and G content rating.
- `shell.dart`, Settings and parent-key flow: native placements in parent planning/settings when the daily key is closed; no mounted banner/native placements on home or routine/movement players. Optional daily-key and separate support videos are different flows. Unavailable daily-key advertising grants access; early dismissal does not. Support does not unlock the daily key.
- `analytics_service.dart`: debug-only `app_open`, `settings_open` and review-prompt hooks. Firebase initialisation and remote Analytics are not implemented in this archive. Public pages disclose Firebase as planned and do not invent an event schema, console retention period or working opt-out.
- Settings still has a permanently false consent visibility callback and an empty action. No connected advertising-consent or Analytics consent flow was found. Child ad treatment does not establish Analytics consent or certify compliance.
- `family_store.dart`: optional child labels and day-specific routine steps; paused routines; end-of-routine feedback (latest 200); approximately 60 days of saved daily completion history. Daily parent entitlement survives reset.
- `movement_preferences.dart`: movement favourites, feedback and custom sequences use separate preference keys. Family reset does not clear them and the family JSON export does not include them.
- Family JSON export includes routine feedback and optional child labels but omits daily progress, paused runs, image/audio files, PIN, daily key and separately stored movement/app preferences. Export files are readable and unencrypted; temporary copies can remain.
- `legal_doc_screen.dart`: documents are fetched from GitHub Pages, converted to text and shown in-app, with an in-memory cache.
- PIN, palette/theme/language, dismissed tips and review-prompt preferences are separately stored. A disabled PIN permits parent-area entry without age verification; the forgotten-PIN arithmetic is not verifiable parental consent.
- The music service and credit dialog name three Kevin MacLeod tracks under CC BY 4.0 and two generated loops. Observed attribution is not independent verification of the audio files or every asset's rights.

All seven public documents have English and Hungarian versions. Obsolete feature branding was removed from public copy. English aliases are byte-identical; current app routes are preserved.

## Required before production release or Firebase activation

1. Review startup SDK operations, actual release ad requests and merged permissions. Replace test ad/App IDs only after configuration is ready. Non-personalised requests are not a blanket consent exemption.
2. Implement any required consent collection, choice reopening and withdrawal before consent-dependent SDK operations. The hidden consent entry and unconditional startup initialisation require review. Written notices do not implement UMP.
3. Add minimal Firebase events for non-sensitive interface actions. Do not log routine titles, child labels, school entries, free text, mood/health values, files or PINs. Review automatic events, screen names, identifiers and user properties as well as explicit button events; avoid sensitive behavioural inferences.
4. Set collection and consent defaults before initialisation and implement separate Analytics enable/disable and withdrawal handling. UMP does not automatically prove the correct Firebase configuration. Evaluate basic/advanced consent mode, including denied-consent requests.
5. Choose and verify Analytics event/user-level retention, reset-on-activity, advertising-personalisation eligibility, Google Signals/ad-sharing links, advertising identifiers and any exports. Publish the actual retention period and available controls before enabling Analytics. No console setting is guessed here.
6. Assess actual child users separately for advertising and Analytics. A parent-labelled screen or 16+ store rating does not prove children never use the app. Match Play audience declarations and any Apple Kids Category requirements to actual use.
7. Update Play Data safety and App Store privacy labels for all actual SDK data, not just family files/custom button payloads. Review identifiers, interactions, approximate location and diagnostics against locked SDKs and the actual release binary. Do not declare the entire app “no data collected”.
8. Establish the provider agreements, transfer safeguards and Google-held-data rights/deletion workflow. Local reset/uninstall does not erase remote records; support email alone may not identify a pseudonymous installation.
9. Correct in-app “no data collected” and “all data deleted” summaries, or implement corresponding behaviour. Public deletion pages disclose the actual limits; this legal-only update does not change source behaviour.
10. Verify dependency licences and bundled asset rights from the final project. Keep music credits accessible and verify source/attribution/edit requirements. No licence grant or ownership is invented.

Firebase disclosures remain preparatory until integration, consent controls and retention are finalised. These documents are not certification of the production binary.

## Official references

- https://developers.google.com/admob/android/privacy/play-data-disclosure
- https://developers.google.com/admob/flutter/targeting
- https://developers.google.com/admob/flutter/privacy/ad-serving-modes
- https://developers.google.com/admob/flutter/privacy/gdpr
- https://developers.google.com/admob/flutter/privacy/consent-mode
- https://support.google.com/analytics/answer/11593727?hl=en
- https://firebase.google.com/docs/analytics/configure-data-collection
- https://firebase.google.com/support/privacy
- https://support.google.com/googleplay/android-developer/answer/10144311?hl=en
- https://support.google.com/googleplay/android-developer/answer/9893335?hl=en
- https://developer.apple.com/app-store/review/guidelines/
- https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
