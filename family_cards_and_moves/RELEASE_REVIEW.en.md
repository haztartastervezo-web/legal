# English and Hungarian legal documents — release review

Reviewed on October 18, 2026 against the supplied `lib 2.zip` and `assets.zip`.
Provider identity was retained from this repository's existing provider notice.

## Public pages

- `privacy_policy.en.html`: local data, selected files, notifications, manual exports, platform backups, support, providers, rights and children.
- `terms_of_use.en.html`: family use, licence, user content, safety, service limits and statutory rights.
- `manage_consent.en.html`: permissions and privacy choices; no advertising-consent form in this version.
- `data_deletion.en.html`: reset limits, complete local deletion and support-email requests.
- `children_privacy.en.html`: parent-facing child privacy information.
- `movement_safety.en.html`: movement, medication and everyday-task safety.
- `support.en.html`: provider and support contact.
- Matching `.hu.html` pages provide all seven documents in Hungarian.
- `index.en.html` and `index.hu.html`: language-specific document directories.
- `index.html`: English default directory, with a Hungarian language link.

Unqualified document `.html` paths contain the same bytes as the `.en.html` pages. All public pages have language navigation, and document links stay in the selected language. Existing in-app privacy and terms URLs remain valid. The Hungarian privacy policy dated October 18 was compared against the supplied implementation; its incompatible claims about image selection, deletion and permissions were replaced. The three earlier Hungarian pages were rewritten to match the English content, and the four missing Hungarian pages were added. Public English and Hungarian pages use the October 18 revision date.

## Evidence and corrections

- `lib/core/constants/app_constants.dart` defines the app, package, support email and hosted legal URL paths.
- `lib/data/family_store.dart` saves family content to SharedPreferences. Exports omit daily progress, music files, image files and the PIN. `reset()` removes only `family_data_v1`, leaving a possible `family_data_v1_broken` recovery key.
- `lib/features/settings/settings_screen.dart` exports a JSON file into temporary storage and opens the share sheet. Reset attempts to remove imported images and audio; it does not clear all preferences or temporary export files.
- `lib/providers/parent_lock_provider.dart` stores the PIN as a local string. PIN, language and theme survive reset.
- `lib/services/goal_images.dart` and `routine_music.dart` import selected files. The earlier notice's claim of no photo access was inaccurate for selected goal images.
- `lib/services/routine_reminders.dart` requests notification permission and schedules local reminders. The earlier no-permissions wording was inaccurate.
- `lib/services/app_update_service.dart` uses Google Play update APIs. No Android Internet-permission claim is made because native manifests were not supplied.
- `lib/services/analytics_service.dart` logs only in debug mode and has no analytics backend in the supplied source. No Firebase, ad network or billing integration was identified in this source.
- The supplied `lib/widgets/legal_about_section.dart` uses `LaunchMode.externalApplication`, but repository commit `031b5569f26f09db04a0913eeaa08b334da4c7ec` reports a newer in-app legal viewer. Both policies therefore describe the common verified privacy implication: documents are loaded from GitHub Pages and GitHub receives a network request. They do not impose a browser or viewer implementation. Check the final release separately.
- The optional parent PIN is not proof of adulthood or verifiable parental consent. Public child notices do not promise that all outbound actions are gated.

## Checks still required on the release binary

These pages are drafted for the supplied version. They are not a certification of the final Android/iOS build or a complete licence inventory.

1. Review `pubspec.yaml`, `pubspec.lock`, transitive dependencies, native manifests, entitlements and release network behaviour; these were not supplied. Confirm absence of hidden collection or advertising SDKs and actual permissions/backup rules.
2. Ensure store privacy labels, Google Play Data safety, target age groups and content declarations match the actual binary. Local-only processing is not automatically off-device collection; platform services and SDK behaviour still need assessment. Do not infer that a family app has an adult-only audience.
3. Review external links, cross-promotion, review prompts and backup sharing in child-accessible flows. An optional PIN is not verified parental consent. A written notice cannot substitute for a required working parental gate. For an Apple Kids Category release, verify the actual implementation against Guidelines 1.3 and 5.1.4.
4. Review the movement and health-related store declarations for actual features and marketing claims. Do not claim therapeutic or neurological outcomes without suitable evidence and regulatory assessment.
5. Compile the actual third-party copyright/licence notices from locked dependencies, including the external `fitness_engine` package, and make them accessible as required by their licences. No dependency licence text or asset ownership was invented. Confirm rights for bundled illustrations, app promotion images, fonts and the four music files in `assets/audio/`; source and asset archives do not establish those rights. Keep evidence of permissions and any attribution obligations. No open-source licence for the app itself has been added.
6. Reassess documents and consent before adding rewarded ads, remote analytics, online music embeds, accounts or cloud sync. Earlier product plans do not establish that those features exist in this archive.
7. Check whether release fixes should remove the recovery key and export cache during a complete in-app deletion. The public deletion page accurately describes their current limitations. The supplied app's reset labels still say all data is deleted, and the short in-app privacy summary omits manual exports. Those UI strings should be corrected in the release source or the corresponding behaviour changed before release. This legal-repository update does not change app source or claim that deletion behaviour was fixed.

## Official references checked

- Google Play User Data: https://support.google.com/googleplay/android-developer/answer/10144311?hl=en
- Google Play Families: https://support.google.com/googleplay/android-developer/answer/9893335?hl=en
- Apple App Review Guidelines: https://developer.apple.com/app-store/review/guidelines/
- GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
- GitHub Pages IP logging: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- NAIH: https://www.naih.hu/
- FTC COPPA FAQ: https://www.ftc.gov/business-guidance/resources/complying-coppa-frequently-asked-questions

Legal requirements depend on actual distribution, audience and processing. Review material changes against current rules before release. No signatures, consent logs, asset licence grants, company registrations or release-binary compliance have been invented.
