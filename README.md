# legal

Shared, publicly hosted legal documents (Privacy Policy, Manage Consent,
Terms of Use) for App Factory apps, served via GitHub Pages.

Each app has its own top-level folder, named after the app's store
name in snake_case (e.g. `Sum & Pair` → `sum_and_pair`), containing one HTML file per document per supported
language:

```
<app_name_snake_case>/
├── privacy_policy.<locale>.html
├── manage_consent.<locale>.html
└── terms_of_use.<locale>.html
```

These files are generated and kept up to date by each app's `/legal-docs`
Claude Code skill run. Do not edit them by hand in an app's own repo — edit
the app, then re-run `/legal-docs` there, which pushes the refreshed files
here.

## Apps

- [meal_plan](meal_plan/privacy_policy.hu.html) — Meal Plan / Heti Menü (meal-planning app)
- [decode_quest](decode_quest/privacy_policy.hu.html) — Decode Quest (Kódfejtő) (decode-the-quote word puzzle)
- [sum_and_pair](sum_and_pair/privacy_policy.hu.html) — Sum & Pair
- [four_clues](four_clues/privacy_policy.en.html) — Four Clues (icon-grouping puzzle game)
- [word_album](word_album/privacy_policy.hu.html) — Word Album
- [magnet_grid](magnet_grid/privacy_policy.en.html) — Magnet Grid
- [nectar_flow](nectar_flow/privacy_policy.en.html) — Nectar Flow
- [quick_daily_fitness](quick_daily_fitness/privacy_policy.hu.html) — Quick Daily Fitness (short daily home-workout app)
- [clue_riddles](clue_riddles/privacy_policy.en.html) — Clue Riddles (visual logic-grid puzzle game)
- [quest_word_search](quest_word_search/privacy_policy.hu.html) — Szókereső (Quest Word Search)
