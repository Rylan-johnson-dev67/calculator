# Simple Calculator

A tiny Python calculator package with core operations and a CLI.

CI
--

This repository includes a GitHub Actions workflow that runs the test suite on push and pull requests.

```text
```

Status badge
------------

You can add a CI status badge to the top of this README. Replace `<OWNER>` and `<REPO>` with your GitHub owner and repository name.
```markdown
[![CI](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml/badge.svg)](https://github.com/<OWNER>/<REPO>/actions/workflows/ci.yml)
```

Usage:

- As a module:

```py
from calculator import compute
print(compute('add', 2, 3))
```

- From the command line:

```powershell
python -m calculator.cli add 2 3
# or
python cli.py add 2 3
```

Run tests:

```powershell
python -m pip install -r requirements-dev.txt
pytest
```

Installable package:


Web UI
------

I added a small browser-based UI under the `web/` folder. To use it:

1. Open `web/index.html` directly in your browser (double-click the file).
2. Or serve it from the project root for correct MIME types and easier testing:

```powershell
py -3 -m http.server 8000
# then open http://localhost:8000/web/ in your browser
```

The UI supports add, subtract, multiply, and divide and shows friendly error messages for invalid input.

GitHub Pages
------------

You can publish the `web/` folder to GitHub Pages so anyone can open the calculator online. I added an Actions workflow `.github/workflows/gh-pages.yml` which will deploy the `web/` folder to GitHub Pages whenever you push to `main`.

After you push, the site will be available at:

```
https://<OWNER>.github.io/<REPO>/
```

Replace `<OWNER>` and `<REPO>` with your GitHub account/org and repository name. Once the workflow runs, visit the URL above and you should see the calculator.

How to publish (explicit)
------------------------

1. Push your `main` branch to GitHub (you said you've already committed and pushed).
2. Open the repository on github.com and go to the `Actions` tab. Select the `Deploy Pages` workflow.
3. You can either wait for the workflow to run after a push or click `Run workflow` (manual dispatch) in the Actions UI to start it now.
4. After a successful run, go to `Settings` -> `Pages` in the repository to verify the site URL and domain. It should show the `gh-pages` deployment and the public URL.
5. Visit `https://<OWNER>.github.io/<REPO>/` to see the live site (may take a minute).

If there's a problem, check the workflow run logs in Actions for errors and the Pages settings for the publishing source.
```powershell
# From project root
python -m pip install -e .

# After installation you get a `calculator` console script:
calculator add 2 3
calculator div 5 2
```

If you prefer `python -m` without installing:

```powershell
python -m calculator add 2 3
```

Docker (serve the web UI)
------------------------

Build and run a small Docker container that serves the `web/` folder with nginx:

```powershell
docker build -t calculator-web .
docker run -p 8080:80 calculator-web
# then open http://localhost:8080/
```
