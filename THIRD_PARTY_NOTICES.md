# Third-Party Notices

This file records third-party material identified during the 2026-08-14 Phase 1 audit. It does not change the license of any file.

## Isaac Lab template-derived source

Several Python scripts, configuration files, and task modules were copied or substantially derived from the Isaac Lab external-project and manipulation/reach templates.

The retained per-file notices comprise 12 files with a `2022-2025` copyright range and 10 files with a `2022-2026` range. No file header was normalized or replaced during this cleanup.

The complete upstream BSD-3-Clause notice is included at [`LICENSES/IsaacLab-BSD-3-Clause.txt`](LICENSES/IsaacLab-BSD-3-Clause.txt) and must accompany redistribution of the derived files. The upstream license is also available at <https://github.com/isaac-sim/IsaacLab/blob/main/LICENSE>.

No blanket copyright-header replacement was performed. Extension-package metadata now identifies the project as requested for this repository; metadata is not evidence of copyright ownership, asset title, redistribution authority, or endorsement by Isaac Lab.

## SolidWorks to URDF Exporter attribution

The three URDF files contain their original generated-file comment identifying SolidWorks to URDF Exporter, commit `1.6.0-4-g7f85cfe`, and Stephen Brawner as the exporter author. The exporter source code is not vendored in this repository. Its attribution is preserved, but its software license does not grant rights to the OneRobotics A1 CAD geometry or generated robot assets.

## External runtime dependencies

Isaac Sim, the Isaac Lab runtime distribution, RSL-RL, MuJoCo, PyTorch, Gymnasium, NumPy, and their dependencies are external runtime dependencies and are not vendored here. The Isaac Lab template-derived source files copied into this repository are handled separately above. Users and downstream distributors must follow the licenses supplied by the external projects and their installed distributions.

No other third-party model, mesh, texture, or material notice was found. The unresolved physical-asset scope is documented separately in `ASSET_LICENSE_STATUS.md`.
