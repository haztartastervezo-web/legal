# Household / Meal Planner legal audit — 2026-09-19

Scope reviewed:
- current files under `household/` in this repository
- current Flutter `lib` source supplied with the project
- current `pubspec.yaml`
- current Apple / Google Play / Google AdMob / Firebase / Google Drive compliance guidance

## Result

The existing legal pages are not yet safe to treat as final. Several statements do not match the current implementation, and two implementation issues must be fixed before the documents can truthfully describe a compliant state.

## Critical implementation blockers

### 1. Android UMP / AdMob consent ordering
`AppStartupService._initMobileAds()` runs the UMP consent flow only on iOS, then initializes Mobile Ads on Android without first running UMP. For EEA/UK/Switzerland traffic this needs review/fix so advertising storage/personalization consent is handled before ad requests where required.

### 2. Account deletion does not delete associated cloud data
`AuthService.deleteAccount()` re-authenticates and calls Firebase Auth `user.delete()`, but it does not delete account-linked Firestore data. `CookEventService` stores records at `users/{uid}/cook_events`. Apple and Google Play expect account deletion to cover associated account data (subject to lawful retention exceptions).

Google Play also requires an external web resource where account deletion can be requested.

## Material mismatches in current Privacy Policy

1. The policy says cloud sync content is stored in Cloud Firestore. Current primary recipe/menu sync is actually Google Drive `appDataFolder`.
2. The policy says shopping list, food diary and settings are synced. Current `SyncState` contains recipes, deleted recipe tombstones, weekly menu and weekly notes. Do not claim categories are synced unless code actually does so.
3. Recipe images can be uploaded to Google Drive during sync; the existing wording says photos are only local.
4. Firestore is nevertheless used for:
   - account-linked cooking events;
   - daily poll votes;
   - language preference;
   - user feedback;
   - selected first-party analytics/statistical events.
5. Poll and language-preference records can use a locally generated random UUID (`device_id`).
6. The current feedback sender stores the message/status/timestamp, but does not automatically attach the device model, OS version, app version or language as the policy currently claims.
7. Firebase Analytics is active and app-open analytics is logged at startup. Some analytics events are additionally written to Firestore with `store: true`, including device language/country/app language and recipe-count snapshots.
8. “By using the app you agree to this privacy policy” should be removed. A privacy notice is a transparency document, not a blanket GDPR consent mechanism.
9. The statement “if ATT is denied, only non-personalized ads are shown” is too absolute and should be removed. ATT and Google advertising consent are separate controls.
10. “Non-personalized advertising = legitimate interest” is too categorical. Advertising storage/identifiers may still require consent under applicable ePrivacy/GDPR rules. The wording should be conditional on jurisdiction and actual CMP configuration.
11. International transfer wording should not mention only SCCs. Use a neutral formulation covering the provider’s applicable transfer mechanism(s), including adequacy / EU-US DPF where applicable and SCCs where needed.
12. Retention is too vague for custom Firestore collections. Define and implement a real retention/deletion schedule before promising specific periods.

## Permissions / data access found in current source

### User-facing/system permissions or authorizations
- Notifications: Firebase Messaging requests alert/badge/sound permission.
- iOS tracking: App Tracking Transparency.
- Camera / photo library: via ImagePicker when the user selects camera/gallery.
- Google Drive OAuth: `drive.appdata` scope for app-specific hidden Drive data.
- Google / Apple sign-in authorization.
- User-selected file access via FilePicker / system picker.
- Receiving explicitly shared content from other apps.

### No current normal-feature access found
- precise/approximate location
- contacts
- microphone
- call/SMS data

### Network/SDK processing
- Firebase Authentication
- Firebase Analytics
- Cloud Firestore
- Firebase Cloud Messaging
- Firebase Remote Config
- Google AdMob / Google Mobile Ads / UMP
- Google Sign-In / Drive API
- Sign in with Apple
- external recipe/image/video URLs, including YouTube where used

## Notes / potentially sensitive content

The new personal Notes feature is local-only in the reviewed code (`personal_notes_v1`). Weekly menu notes are included in Drive sync. Because users may enter allergy reactions or health-related observations, avoid claiming the app intentionally processes health data for profiling. If any health-revealing free text is later synced to a controller-managed backend, review GDPR Article 9 implications and obtain an appropriate legal basis where required.

## Terms of Use changes required

- Remove/qualify “as is, no warranties” language so it does not purport to waive mandatory EU/Hungarian consumer digital-content/service rights.
- State that nutrition figures and recommendations can be estimates and are not medical/dietetic diagnosis or advice.
- Add user responsibility for rights in imported recipes/images/external content.
- Make clear that rewarded-ad access is temporary/feature-specific unless otherwise stated.
- Avoid “continued use automatically means acceptance” as the sole mechanism for material adverse changes.
- Preserve mandatory consumer protections of the user’s habitual-residence country.

## Consent page changes required

- Do not say rejection always results in non-personalized ads.
- Explain that ATT and Google UMP/CMP choices are separate.
- Android instructions should not assume one fixed Settings path across all Android versions.
- Mention camera/photos/notifications as separate OS permissions rather than advertising consent.
- If analytics requires consent in a given jurisdiction/configuration, collection must be technically gated before it starts.

## Store declarations that must match

After the code is corrected, re-check:
- Google Play Data safety
- App Store Privacy Nutrition Labels
- Google Play account deletion URL
- in-app privacy-policy link
- AdMob Privacy & messaging / CMP configuration
- ATT declaration and tracking data categories

## Recommended publication sequence

1. Fix Android UMP ordering.
2. Make account deletion remove all account-linked Firestore data (and any other account-linked backend data).
3. Decide and implement retention for custom Firestore collections.
4. Decide whether analytics is consent-gated in jurisdictions where required and make code + CMP behavior match.
5. Rewrite Privacy Policy, Terms and Consent pages to exactly match the resulting code.
6. Add HU/EN external account-deletion pages.
7. Update Play Data safety and App Store privacy labels from the same final data map.

Do not publish a “perfect” legal text that describes behavior the current binary does not actually implement; store policies specifically require the disclosures to match the app.
