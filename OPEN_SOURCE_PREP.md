# OneRobotics A1 Open-Source Preparation Report

Audit date: 2026-08-14

Repository baseline: `b060df94bbdeb7d05f7fb2ef2e648d180c4d8ba2`

Isaac Lab review target: `release/3.0.0-beta2` at `2e44ddb2e19536579140496023b5ccb060bc4152`

## 1. Summary of Phase 1 changes

Phase 1 makes the existing external project portable and reviewable without choosing an upstream directory layout. It corrects public branding, removes developer-local runtime paths, packages the existing robot descriptions, cleans project metadata, records unresolved asset rights, removes unused template UI code, and applies narrowly scoped Isaac Lab 3.0 compatibility fixes.

The OneRobotics A1 joint definitions, inertial and collision data, mesh geometry, actuator gains and limits, reach-task reward weights and formulas, and MuJoCo dynamics were not changed. The URDF edits only replace unresolved ROS `package://` mesh URIs with equivalent file-relative URIs. The MuJoCo command-line additions preserve the existing control and `wxyz` observation defaults.

This working tree is **not cleared for an asset-bearing public release or upstream pull request**. `ASSET_LICENSE_DECISION = REVIEW_REQUIRED` remains the controlling status.

## 2. Files modified, added, and deleted

Project and packaging:

- Modified `.gitattributes`, `.gitignore`, `.pre-commit-config.yaml`, `pyproject.toml`, `README.md`, `source/h1_reach/setup.py`, `source/h1_reach/config/extension.toml`, and `source/h1_reach/docs/CHANGELOG.rst`.
- Added `source/h1_reach/MANIFEST.in`.
- Added `ASSET_LICENSE_STATUS.md`, `THIRD_PARTY_NOTICES.md`, `LICENSES/IsaacLab-BSD-3-Clause.txt`, and this report.

Runtime and scripts:

- Modified `source/h1_reach/h1_reach/robots/a1.py`.
- Modified the three URDF files under `source/h1_reach/h1_reach/assets/urdf/` only to make mesh paths relative.
- Modified the reach task's `mdp/__init__.py`, `fk_pose_command.py`, `observations.py`, `rewards.py`, and `h1_reach_env_cfg.py` for the target API and URDF-importer naming behavior; normalized the missing final newline in `agents/__init__.py`.
- Modified `scripts/list_envs.py`, `scripts/rsl_rl/train.py`, and `scripts/sim2sim.py`.
- Modified `source/h1_reach/h1_reach/__init__.py` and deleted the unused `ui_extension_example.py` template demonstration.

## 3. Branding and naming corrections

- Public-facing legacy misspellings were corrected to **OneRobotics A1**.
- The README title is `OneRobotics A1 — Isaac Lab Integration` and links to <http://www.onerobot.com/>.
- Extension metadata now uses the user-supplied project identity, repository URL, description, and relevant keywords.
- Metadata identifies the project; it is not evidence of copyright ownership, asset title, redistribution authority, or Isaac Lab endorsement.
- The repository slug, Python package and directory names containing `h1_reach`, class names such as `H1ReachEnvCfg`, and legacy `Template-A1-Reach-*` Gym IDs are intentionally unchanged. Renaming them is a Phase 2 compatibility decision.

## 4. Code licensing findings

- The root `LICENSE` is BSD-3-Clause and names only `Copyright (c) 2026, 万昕`. It does not name OneRobotics, and Phase 1 does not alter that ownership statement.
- `source/h1_reach/setup.py` previously declared Apache-2.0. It now declares BSD-3-Clause for the Python/code package, consistent with the root code license and source SPDX identifiers.
- Twelve retained files have Isaac Lab Project Developers `2022-2025` BSD-3-Clause headers and ten have `2022-2026` headers. These notices were not rewritten.
- The complete Isaac Lab BSD-3-Clause notice is included in `LICENSES/IsaacLab-BSD-3-Clause.txt` and referenced from `THIRD_PARTY_NOTICES.md`.
- `scripts/sim2sim.py` has no ownership header in the baseline. Its authorship is ambiguous, so Phase 1 does not invent or replace one.
- Local wheel construction is used only as an installation check. No wheel may be published while the bundled asset rights remain unresolved; final distribution-level placement of license and notice files follows the maintainer-approved repository/package split.

## 5. Physical assets requiring explicit license confirmation

The working tree contains 41 A1 model files totaling 28,566,305 bytes:

| Class | Count | Bytes | Scope |
| --- | ---: | ---: | --- |
| STL meshes | 33 | 28,481,472 | Single left arm, single right arm, and dual arm |
| URDF models | 3 | 45,423 | Left, right, and dual-arm robot descriptions |
| MuJoCo/MJCF XML | 5 | 39,410 | Raw and actuated right/dual-arm models |

All 41 files, and any USD or other derivatives produced from them, require written confirmation from the asset rights holder. The exact groups and required evidence are listed in `ASSET_LICENSE_STATUS.md`. No USD, USDZ, OBJ, DAE, texture, or separate material asset is currently tracked.

No Git LFS pointers exist. The largest STL is 1,553,084 bytes, below the repository's existing 2,000 KiB size check, so Phase 1 does not add STL to LFS without a demonstrated need.

## 6. Third-party findings

- The external-project scaffolding, launcher scripts, and reach-task code include material copied or substantially derived from Isaac Lab. Existing file-level headers are retained, and the full upstream license is included separately.
- The URDF generated-file comments identify SolidWorks to URDF Exporter and Stephen Brawner. That identifies the generating tool only; its software license is not an asset license for A1 CAD or generated descriptions.
- Isaac Sim, Isaac Lab runtime packages, RSL-RL, MuJoCo, PyTorch, Gymnasium, NumPy, and their dependency trees are external and are not bundled as runtime distributions here.
- No additional third-party mesh, texture, material, or model notice was found. This is an audit finding, not proof of origin.

## 7. Template artifacts and intentionally retained legacy surface

Removed or corrected:

- generic template title, description, keywords, authorship, repository URL, TODO blocks, and unused extension dependencies;
- eager import of the toy UI extension and the unused UI example file;
- broken pre-commit license hooks that referenced missing `.github/LICENSE_HEADER*.txt` files, plus the unrelated mimic-specific hook;
- stale changelog wording and the `.gitignore` rule that prevented future tests from being tracked.

Intentionally retained pending maintainer feedback:

- `h1_reach` package and task directory names, `H1Reach*` class names, and `Template-A1-Reach-*` IDs;
- the top-level eager task registration and non-lazy local `__init__.py` exports;
- the deprecated RSL-RL `policy=RslRlPpoActorCriticCfg` form, which beta2 currently migrates through a compatibility path;
- the current `0.1.0` release identity and legacy changelog history;
- the existing USD-ignore/Git-LFS rules. No USD is tracked, and the final asset-hosting strategy is undecided.

An authentic Isaac Lab render of the A1 at the all-joint-zero pose was captured during the headed smoke test and added at `media/onerobotics-a1-zero-pose.png`. The render is derived from the same `REVIEW_REQUIRED` physical asset set and does not establish or expand redistribution rights.

## 8. Isaac Lab `release/3.0.0-beta2` compatibility review

Straightforward fixes applied:

- `ArticulationCfg` is imported from the current public package path.
- The missing developer-local USD is replaced by `UrdfFileCfg` conversion from the packaged right-arm URDF.
- URDF mesh references are clone-relative and resolve from an installed wheel.
- ProxyArray-backed articulation data used by Torch math is accessed explicitly through `.torch`.
- Command classes and `JointPositionActionCfg` use explicit public imports; this avoids beta2 lazy-export wildcard failures.
- Joint/body regular expressions match both legacy names and the identifiers generated by the Isaac Sim 6.0 URDF importer.
- Python metadata targets Python 3.12 and Isaac Sim 6.0; the training launcher checks for RSL-RL 5.0.1.
- MuJoCo can explicitly reorder its internal `wxyz` quaternion fields to `xyzw` for beta2-trained policies while retaining the legacy default.

Deferred because migration could alter policy behavior or public APIs:

- converting the PPO configuration from deprecated `policy=` to the beta2 `actor=` / `critic=` model configuration;
- changing the legacy sim2sim quaternion default from `wxyz` to `xyzw`;
- adopting the exact upstream `.pyi` lazy-export structure;
- renaming local packages, classes, or Gym IDs.

## 9. Checks run and results

Passed on 2026-08-14:

- Ruff 0.12 lint and formatting checks and `git diff --check`.
- Python syntax compilation for repository Python files.
- Precise scans found no developer home paths, Windows-drive paths, temporary local paths, usernames, unresolved ROS package mesh URIs, or legacy public-facing brand names. The official `onerobot.com` domain and repository slug are intentional.
- All 66 URDF mesh references resolve; all three URDF documents parse.
- MuJoCo 3.8.0 loads all five XML models: right raw `(nq=7, nv=7, nu=0)`, right position `(7, 7, 7)`, right motor `(7, 7, 7)`, dual raw `(14, 14, 0)`, and dual actuated `(14, 14, 14)`.
- Custom forward kinematics was compared with MuJoCo over 1,000 random joint configurations: maximum position error `5.82e-16 m`, maximum rotation error `7.30e-8 rad`.
- A Python 3.12 wheel builds and installs non-editably from an arbitrary temporary path. Both direct wheel and source-distribution-to-wheel builds pass and contain identical file contents: 13 Python files and all 41 model assets. Installed `A1_RIGHT_CFG.spawn.asset_path` resolves inside `site-packages`.
- The two legacy Gym environments register after non-editable installation. Script `--help` checks pass for train, play, and sim2sim.
- Against the exact target branch source at `2e44ddb`, an Isaac Sim 6.0.1 headless CPU smoke test converted and spawned one packaged A1, resolved seven actuated joints and eight bodies, created the complete manager-based environment, produced a `(1, 35)` policy observation and `(1, 7)` action, and completed three steps with finite reward and no termination.

Runtime limitations:

- The local wheel/source distribution is an installation test, not a publishable artifact: both omit the repository-level legal reports/licenses, the wheel additionally omits the checkout-level extension manifest, and the source distribution warns that its package root has no standard README. Their final placement depends on the asset/package split; publishing remains prohibited while asset rights are unresolved.
- The isolated beta2 smoke disabled only the upstream reach scene's remote ground/table assets to avoid a blocking Nucleus download; the A1, managers, observations, rewards, and physics steps were exercised.
- The same smoke reached the complete action manager on CUDA, but the local dirty runtime combines Torch `2.11.0+cu130` with Isaac Sim's CUDA 12.8 libraries and could not load `libnvrtc-builtins.so.13.0` through Kit. CPU execution passed, so this is recorded as a local GPU-runtime limitation rather than a repository failure.
- A headed Kit visualization loaded one A1 reach environment on CPU and held all seven joint targets at `0 rad`; the resulting render is included in the README. No long training or trained-policy quality evaluation was run.

## 10. Items blocked on maintainer or rights-holder feedback

- Written ownership and redistribution terms for every URDF, MJCF/XML, STL, and converted USD asset.
- Whether assets must be moved to a dedicated OneRobotics repository before an issue or PR.
- Final placement in `isaaclab_contrib`, `isaaclab_assets`, or another upstream location.
- Whether the validation reach task is in scope for upstream review.
- Final package/API naming and compatibility aliases.
- The exact upstream-required headers, documentation location, tests, changelog fragment, and lazy-export layout.
- Maintainer confirmation that the current A1 render is suitable for the final asset README, or guidance on a replacement render format/resolution.

## 11. Recommended Phase 2 structure

After rights are cleared, open the Proposal issue before restructuring. Present the A1 physical model and `A1_RIGHT_CFG` as the primary contribution and the reach environment as optional validation material. Ask maintainers to choose among:

1. a dedicated OneRobotics asset repository plus a small upstream articulation configuration referencing its approved hosted asset;
2. placement of the asset/configuration in `isaaclab_assets`;
3. placement in `isaaclab_contrib` or another maintainer-selected package.

Only after that decision should Phase 2 select the final `h1_reach` to `a1` / `onerobotics_a1` migration, move or adapt the reach task, add upstream smoke tests and documentation, adopt exact lazy-export and header conventions, adapt the screenshot to the final asset-repository format if requested, add the changelog fragment, replace conversion paths with the approved hosted USD location if requested, and prepare the final pull request.

## Working-tree snapshot

`git status --short` at the end of Phase 1:

```text
 M .gitattributes
 M .gitignore
 M .pre-commit-config.yaml
 M README.md
 M pyproject.toml
 M scripts/list_envs.py
 M scripts/rsl_rl/train.py
 M scripts/sim2sim.py
 M source/h1_reach/config/extension.toml
 M source/h1_reach/docs/CHANGELOG.rst
 M source/h1_reach/h1_reach/__init__.py
 M source/h1_reach/h1_reach/assets/urdf/A1/a1_left.urdf
 M source/h1_reach/h1_reach/assets/urdf/A1/a1_right.urdf
 M source/h1_reach/h1_reach/assets/urdf/A1_dual/A1_dual.urdf
 M source/h1_reach/h1_reach/robots/a1.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/agents/__init__.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/h1_reach_env_cfg.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/mdp/__init__.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/mdp/fk_pose_command.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/mdp/observations.py
 M source/h1_reach/h1_reach/tasks/manager_based/h1_reach/mdp/rewards.py
 D source/h1_reach/h1_reach/ui_extension_example.py
 M source/h1_reach/setup.py
?? ASSET_LICENSE_STATUS.md
?? LICENSES/
?? OPEN_SOURCE_PREP.md
?? THIRD_PARTY_NOTICES.md
?? media/
?? source/h1_reach/MANIFEST.in
```

Concise diff summary: 23 tracked paths changed (22 modified, one deleted), with 352 insertions and 320 deletions in the tracked diff. Six new untracked report/license/image/manifest paths are ready for review. No commit or push was performed.
