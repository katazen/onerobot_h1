# OneRobotics A1 2026 source model

This directory contains the current OneRobotics A1 right- and left-arm URDF
models and their referenced meshes. The source files were imported without
geometric or inertial edits from the OneRobotics SDK asset bundle whose
SHA-256 is:

```text
9dfa9f0e1b7fa8d05b12b47dd67ab0484bc376b4db60ce541ee832455a0be8c9
```

## Published contents

- `a1_r.urdf`: independent right-arm 7-DoF source model;
- `a1_l.urdf`: independent left-arm 7-DoF source model;
- `meshes/a1_r/` and `meshes/a1_l/`: eight referenced STL files per arm;
- `model_parameters.yaml`: shared model and simulation-control metadata.

This directory does not contain or declare an A1 2026 bimanual model. The 18
robot-model files and `model_parameters.yaml` are Copyright 2026 OneRobotics
and are distributed under CC BY 4.0 as declared in the repository's
`ASSET_LICENSE_STATUS.md`.

## Hardware overlay

The URDF contains the model geometry, link inertias, joint transforms, position
limits, and nominal effort fields. The actuator and control values confirmed by
OneRobotics for simulation are recorded in `model_parameters.yaml` and applied
by the Isaac Lab integration rather than rewriting the source URDF.

The 4340 actuator is used for joints 1--3 with a 48.19 reduction ratio. The
4310 actuator is used for joints 4--7 with a 10:1 reduction ratio. Both use a
motor-side rotor inertia of `2.193e-5 kg m^2`; the joint-side armature is the
rotor inertia multiplied by the square of the reduction ratio.

The confirmed joint-output rated/peak torques are `15.0/26.859 N m` for
joints 1--3 and `3.0/5.975 N m` for joints 4--7. The simulation uses the peak
values as its static solver saturation limits and retains the rated values as
actuator metadata. A peak-duration transition and thermal derating are not
modeled; they are not required to apply the supplied peak value as a simple
hard torque bound.

## Known source limitation

Both source URDFs explicitly identify the Link7 mass (`0.20 kg`) and inertia as
a temporary v1 flange placeholder. The values are retained exactly as supplied;
they are not presented as measured bare-flange parameters. A future source-model
revision should replace them when measured mass, center of mass, and inertia are
available.
