# Copyright (c) 2022-2025, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for the Onero A1 right arm (7-DoF).

Reference: robot_assets/onero_description/urdf/A1/a1_right.urdf
"""

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

##
# Configuration
##

# Absolute path to the USD exported from a1_right.urdf.
A1_RIGHT_USD_PATH = "/home/woan/workspace/h1_arm/h1_reach/source/h1_reach/h1_reach/assets/urdf/A1/a1_right/a1_right.usd"

A1_RIGHT_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=A1_RIGHT_USD_PATH,
        activate_contact_sensors=False,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        # regex keys so they match whether the importer kept hyphens or replaced them
        joint_pos={
            "joint1.*": 0.0,
            "joint2.*": -0.6,
            "joint3.*": 0.0,
            "joint4.*": 1.0,
            "joint5.*": 0.0,
            "joint6.*": 0.5,
            "joint7.*": 0.0,
        },
    ),
    actuators={
        # NOTE: the URDF declares effort/velocity limits of 0 and no PD gains, so they are set here.
        # armature = reflected rotor inertia of the motor (ideally I_motor * gear_ratio^2 from the
        # datasheet). It is set non-zero so the wrist joints have realistic inertia -- with armature=0
        # the distal joints' inertia is ~1e-5, which makes an explicit-PD (MuJoCo "motor" mode)
        # sim2sim numerically unstable. 0.05 is a placeholder; replace with the real value if known.
        "arm_proximal": ImplicitActuatorCfg(
            joint_names_expr=["joint[1-4].*"],
            effort_limit_sim=30.0,
            velocity_limit_sim=3.0,
            stiffness=60.0,
            damping=6.0,
            armature=0.05,
        ),
        "arm_distal": ImplicitActuatorCfg(
            joint_names_expr=["joint[5-7].*"],
            effort_limit_sim=12.0,
            velocity_limit_sim=3.0,
            stiffness=30.0,
            damping=3.0,
            armature=0.05,
        ),
    },
    soft_joint_pos_limit_factor=1.0,
)
"""Configuration of the Onero A1 right arm."""
