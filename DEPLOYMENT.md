# Preview and production handoff

1. Push the `portfolio-revamp` branch and verify its Vercel preview.
2. Confirm the project framework is Next.js, repository root is selected and output directory is `.next` rather than the previous Vite `dist`.
3. Without DATABASE_URL or AI keys, check the read-only library and guided project explorer. All bundled articles should be reachable.
4. For full publishing, configure hosted PostgreSQL, initialise its schema and import content. Use fresh admin credentials and durable image storage.
5. Rotate the previously exposed NVIDIA test key. Add the replacement as a private Vercel environment variable, with models available to the account. No key is included in this repository.
6. Review the AI-assisted article drafts before public promotion. They are research designs, not completed studies.
7. Verify sitemap.xml, robots.txt, canonical URLs, share cards and representative article routes on the preview.
8. Merge to the production branch only after reviewing the preview. Confirm that the existing umer-amin.vercel.app domain remains attached to the project.

The previous site remains available in Git history at commit ea2b20e899e1afa7f1ac4d43b99d89cdfe186569. No force push is needed.
