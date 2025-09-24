Deploying web/ to your user GitHub Pages site

This repository contains a GitHub Actions workflow that can push the contents of the `web/` folder to your user site repository `Rylan-johnson-dev67/Rylan-johnson-dev67.github.io`.

What I added

- `.github/workflows/deploy-to-user-site.yml` — uses `peaceiris/actions-gh-pages` to publish `./web` to the `main` branch of the destination repo.

What you must do (one-time setup)

1. Create a Personal Access Token (PAT)
   - Go to https://github.com/settings/tokens (or Settings → Developer settings → Personal access tokens).
   - Click "Generate new token" → "Tokens (classic)" (or the appropriate flow on your account).
   - Give it a name like `pages-deploy-token`.
   - Scopes: At minimum, check `repo` (full repo access) so the action can push to `Rylan-johnson-dev67.github.io`. If you prefer more restricted access, give only the repository-level permissions for the destination repo.
      - Generate the token and copy it now. (You won't be able to see it again.)

2. Add the token as a repository secret in this `calculator` repository
   - In GitHub, open this repository → Settings → Secrets and variables → Actions → New repository secret.
   - Name: `PAGES_REPO_TOKEN`
   - Value: paste the PAT you created.
   - Save the secret.

How to run the deploy workflow

- The workflow is triggered on push to `main` and can also be started manually from the Actions tab using `Run workflow`.
- After you add the secret, push a small commit (or trigger the workflow manually). The workflow will run and attempt to push `./web` into the `main` branch of `Rylan-johnson-dev67/Rylan-johnson-dev67.github.io`.

Verifying the site

- After the workflow completes, check the destination repo (https://github.com/Rylan-johnson-dev67/Rylan-johnson-dev67.github.io) to confirm files were pushed.
- Wait a few minutes, then open https://Rylan-johnson-dev67.github.io/ to see the user site at the canonical URL.

Security notes

- Treat the PAT like a password. Don't paste it into issues, PRs, or chats.
- If you prefer, you can create a dedicated machine user for deployments and generate a PAT for that user instead.

If you want, I can:
- Add the secret for you if you provide the token (not recommended for security).
- Trigger the workflow once you confirm the secret is added.
