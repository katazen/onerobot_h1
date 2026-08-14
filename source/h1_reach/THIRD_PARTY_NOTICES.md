# Third-Party Notices

This file records third-party material identified during the 2026-08-14 Phase 1 audit. It does not change the license of any file.

## Isaac Lab template-derived source

Several Python scripts, configuration files, and task modules were copied or substantially derived from the Isaac Lab external-project and manipulation/reach templates.

The retained per-file notices comprise 12 files with a `2022-2025` copyright range and 10 files with a `2022-2026` range. No file header was normalized or replaced during this cleanup.

The complete upstream BSD-3-Clause notice is included at [`LICENSES/IsaacLab-BSD-3-Clause.txt`](LICENSES/IsaacLab-BSD-3-Clause.txt) and must accompany redistribution of the derived files. The upstream license is also available at <https://github.com/isaac-sim/IsaacLab/blob/main/LICENSE>.

No blanket copyright-header replacement was performed. The project code and OneRobotics A1 assets have separate license scopes; neither project metadata nor the OneRobotics asset license implies endorsement by Isaac Lab.

## SolidWorks to URDF Exporter attribution

The three URDF files contain their original generated-file comment identifying SolidWorks to URDF Exporter, commit `1.6.0-4-g7f85cfe`, and Stephen Brawner as the exporter author. The exporter source code is not vendored in this repository. Its attribution is preserved, and its software license is separate from the CC BY 4.0 license that OneRobotics applies to the A1 model assets.

## External runtime dependencies

Isaac Sim, the Isaac Lab runtime distribution, RSL-RL, MuJoCo, PyTorch, Gymnasium, NumPy, and their dependencies are external runtime dependencies and are not vendored here. The Isaac Lab template-derived source files copied into this repository are handled separately above. Users and downstream distributors must follow the licenses supplied by the external projects and their installed distributions.

No other third-party model, mesh, texture, or material was found vendored under `source/h1_reach/h1_reach/assets/`. The OneRobotics-owned physical-asset scope and required attribution are documented separately in `ASSET_LICENSE_STATUS.md`.

## README visualization

`media/onerobotics-a1-zero-pose.png` was captured from the inherited Isaac Lab reach scene and includes third-party Isaac Lab/Isaac Sim/NVIDIA scene elements such as the environment table, grid, and pose markers. It is included as documentation. The OneRobotics CC BY 4.0 grant covers the underlying A1 model assets, not the screenshot as a whole or those third-party scene elements.
