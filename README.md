# legal

Shared, publicly hosted legal documents (Privacy Policy, Manage Consent,
Terms of Use) for App Factory apps, served via GitHub Pages.

Each app has its own top-level folder, named after its `pubspec.yaml`
`name:` field, containing one HTML file per document per supported
language:

```
<pubspec-name>/
├── privacy_policy.<locale>.html
├── manage_consent.<locale>.html
└── terms_of_use.<locale>.html
```

These files are generated and kept up to date by each app's `/legal-docs`
Claude Code skill run. Do not edit them by hand in an app's own repo — edit
the app, then re-run `/legal-docs` there, which pushes the refreshed files
here.

## Apps

- [number_puzzle](number_puzzle/privacy_policy.hu.html) — SzámKirakó (Number Puzzle)
