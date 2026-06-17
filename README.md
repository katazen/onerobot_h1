# onerobot_h1 — A1 Arm Reach (Isaac Lab + MuJoCo sim2sim)

End-effector pose-reaching for the Onero **A1** robotic arm, trained in
[Isaac Lab](https://github.com/isaac-sim/IsaacLab) with RSL-RL and validated in MuJoCo (sim2sim).

The task is built on Isaac Lab's official `manipulation/reach` example, adapted to the A1 right arm
(7-DoF, fixed base, end-effector `Link7`).

## Features

- **Reach task** (`Template-A1-Reach-v0`) subclassing the official `ReachEnvCfg`.
- **Reachable-by-construction targets**: instead of sampling a Cartesian box (which may be
  unreachable), a random joint configuration is sampled within the joint limits and forward
  kinematics gives the commanded end-effector pose — so every target is jointly reachable in
  position *and* orientation.
- **Multi-scale pose reward** (multiplicative position × orientation tanh kernels) so the policy
  cannot satisfy one objective while ignoring the other.
- **End-effector pose error in the observation**, which closes the control loop and improves
  tracking precision.
- **MuJoCo sim2sim** (`scripts/sim2sim.py`): observation matches the training env exactly,
  FK-sampled targets, switchable `position` / `motor` control modes, and RGB coordinate-frame
  markers on both the end-effector and the goal.

## Repository layout

```
scripts/                         # train / play / sim2sim entry points
  rsl_rl/{train,play}.py
  sim2sim.py                     # MuJoCo sim2sim
source/h1_reach/h1_reach/
  robots/a1.py                   # A1_RIGHT_CFG articulation (PD gains, armature)
  tasks/manager_based/h1_reach/  # env cfg, mdp (FK command, rewards, observations), PPO cfg
  assets/
    urdf/, meshes/               # robot description
    mjcf/A1/, mjcf/A1_dual/      # MuJoCo models (position & motor actuator versions)
```

## Installation

Requires a Python environment with Isaac Lab installed (the project was developed against
Isaac Sim / Isaac Lab with `rsl-rl-lib==5.0.1`).

```bash
python -m pip install -e source/h1_reach
```

## Usage

```bash
# list registered tasks
python scripts/list_envs.py

# train
python scripts/rsl_rl/train.py --task Template-A1-Reach-v0 --num_envs 2048 --headless

# play a trained policy
python scripts/rsl_rl/play.py  --task Template-A1-Reach-Play-v0

# sim2sim in MuJoCo (set control_mode = "position" / "motor" in SimToSimCfg)
python scripts/sim2sim.py
```

## Notes

- The URDF declares zero effort/velocity limits and no PD gains, so actuator stiffness/damping,
  effort limits and **armature** are set in `robots/a1.py`. The training env and the sim2sim model
  must use the **same** `dt` / `decimation` / `armature` for the MuJoCo `motor` mode to be stable
  and consistent with `position` mode.
- Robot mesh assets (STL/URDF) are the company's A1 model; review licensing before redistribution.
