# Ralph workflow presentation

A standalone React 19 + TypeScript + Vite 7 presentation using `@xyflow/react`. The inherited visualization is attributed in the [root provenance record](../README.md#origins-and-jds-contribution); JD's recorded code delta corrects initial render-time ref access. It explains intended agent behavior; it does not invoke Amp, execute stories or verify completion.

## Local setup (visualization only)

Use Node **20.19+ on the 20.x line, or 22.12+** with npm, as required by the locked Vite/plugin engines. CI selects Node 20; use a sufficiently recent patch release. No Amp account, authentication or environment secret is needed for this visualization.

From the repository root:

```bash
cd flowchart
npm ci --ignore-scripts
npm run dev -- --host 127.0.0.1
```

Open the local URL printed by Vite, with the configured `/ralph/` base path. Binding loopback avoids intentionally exposing the server to other machines. Dependency retrieval still requires registry network access. `--ignore-scripts` avoids dependency lifecycle scripts; the documented lint/build commands intentionally execute the local development toolchain.

## Local validation and production-output preview

From `flowchart/`:

```bash
npm run lint
npm run build
npm run preview -- --host 127.0.0.1
```

`build` runs `tsc -b && vite build`, producing `dist/`. `preview` serves that output for local inspection; it is not a production deployment. There is **no `test` script**. These commands do not validate agent behavior, credentials or service integration. Check the PR's verification record for what was actually run; setup instructions alone are not passing test evidence.

## Source-backed behavior and limits

- [`src/App.tsx`](src/App.tsx) defines the steps, notes, reveal controls, node positions and connections. Next/previous/reset controls change the visible sequence; nodes can be dragged and edges connected/reconnected.
- Those interactive changes are in-memory. There is no inspected save/export or persistence feature; reload is not a saved-diagram workflow.
- [`vite.config.ts`](vite.config.ts) fixes the base to `/ralph/`; hosting at a different subpath requires deliberate configuration work, not just copying a URL.
- [CI](../.github/workflows/ci.yml) runs lint, TypeScript and build. The separate [Pages workflow](../.github/workflows/deploy.yml) runs on pushes to `main` or manual dispatch and requires Pages configuration/permissions. It is preserved unchanged; no Pages setup, deployment or live-site validation is performed as part of this documentation work.
- The diagram narrates a desired workflow. Branch selection, test success and commits are requested in the agent prompt, not enforced by the React application or independently verified by the shell.

For an editable, portable explanation with explicit enforced/requested boundaries, use the [Excalidraw source and preview](../docs/README.md). For runner permissions, state-path ambiguity and cost/privacy cautions, read the [root README](../README.md#agent-runner-separate-privileged-and-potentially-billable). For inherited code/artwork rights, read [license status](../LICENSE-STATUS.md).
