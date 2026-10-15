# Umer Amin Durrani — Portfolio

Next.js portfolio with an interactive skills map, project directory, case studies, research library and project-exploration chat.

## Run locally

Use Node.js 22, run `npm ci`, then `npm run dev`.

The public pages work without secrets or a database. The bundled library includes the introductory project notes and 75 clearly labelled research-design drafts. These proposals do not claim completed experiments or original findings.

## Vercel

This replaces the repository's previous Vite application. `vercel.json` selects Next.js, `npm run build` and `.next`. Keep the Vercel project root at the repository root. Review any old dashboard overrides for Vite or `dist`.

Set `SITE_URL=https://umer-amin.vercel.app` for production. A branch deployment provides a preview before merging into the production branch. The public site runs in read-only mode without DATABASE_URL; publishing requires a hosted PostgreSQL connection.

### Optional environment variables

| Variable | Purpose |
| --- | --- |
| SITE_URL | Canonical public origin; production defaults to the existing portfolio domain on Vercel |
| DATABASE_URL | Hosted PostgreSQL URL; do not use a local 127.0.0.1 connection in Vercel |
| ADMIN_EMAIL | Publishing account email |
| ADMIN_PASSWORD_HASH | Scrypt hash generated with `node scripts/password.mjs` |
| SESSION_SECRET | Random secret of at least 32 characters |
| NVIDIA_API_KEY | Private NVIDIA hosted API key |
| NVIDIA_MODEL | Default chat model |
| NVIDIA_MODEL_TECHNICAL | Optional technical-workflow model |
| NVIDIA_MODEL_RESEARCH | Optional research-workflow model |
| OPENAI_API_KEY / OPENAI_MODEL | Alternative chat provider |

Never commit environment files. Create fresh production credentials; local test keys and admin credentials must not be reused.

## Publishing and storage

After configuring PostgreSQL, run `npm run db:setup` and `node scripts/import-library.mjs` from an authorised environment. Importing preserves existing slugs. When a database is configured it becomes the content source, replacing bundled read-only content.

Local filesystem uploads are disabled on Vercel. Use HTTPS image URLs until durable object storage is configured. Existing public images are bundled with the application. The admin stays disabled without its credential variables.

The chat uses server-side keys, bounded input, same-origin checks and an in-process development rate limiter. Configure shared abuse controls, spending limits and provider permissions before enabling the public chat at scale. Guided responses remain available without an AI key.

## Validation

`npm test` checks authentication helpers and project routing. `npm run build` verifies compilation and types. `scripts/check-library.mjs` can audit the article routes against a running local server.

The sitemap uses only published eligible posts, with canonical article routes and topic hubs. Search indexing requires a public deployment. Rankings, AI citations and backlinks are not guaranteed by metadata or publication volume.
