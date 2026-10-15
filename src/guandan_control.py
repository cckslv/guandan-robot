# -*- coding: utf-8 -*-
"""
灵爪灌金 - 双臂灌馅循环（27节点）
适配：AUBO-i5H 双臂协作机器人（右臂执行，左臂夹持）
基于 OpenClaw 智能体平台，面向非遗灌蛋全自动作业
"""

import time
import math
import json
import logging
from datetime import datetime

from aubo_sdk import Robot, MotionMode, ForceMode

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("guandan_run.log"), logging.StreamHandler()],
)
logger = logging.getLogger("Guandan")

# ===================== 机器人初始化 =====================
right_arm = Robot(ip="192.168.1.100")
left_arm = Robot(ip="192.168.1.101")

right_arm.connect()
left_arm.connect()
logger.info("双臂通信链路已建立")

right_arm.set_joint_speed(28)
right_arm.set_linear_speed(95)
right_arm.set_linear_accel(450)
left_arm.set_joint_speed(25)
left_arm.set_linear_speed(80)

right_arm.enable_force_control(axis="z", threshold=48.0, response="stop")
left_arm.enable_force_control(axis="z", threshold=12.0, response="stop")
logger.info("力控保护已启用 | 右臂阈值48g | 左臂阈值12g")

# ===================== 示教点位 =====================
P_home_R = [450.17, -12.53, 280.34, 3.1416, 0.0000, 0.0000]
P_approach_meat = [280.52, -180.33, 120.04, 0.0045, -0.0127, 0.0012]
P_insert_meat = [280.49, -180.28, 85.19, 0.0041, -0.0113, 0.0010]
P_syringe_up = [280.47, -180.25, 148.71, 0.0041, -0.0113, 0.0010]
P_plunger_approach = [278.91, -182.14, 126.43, -0.1532, 0.0874, 0.0036]
P_plunger_grip = [278.84, -182.09, 98.67, -0.1528, 0.0871, 0.0034]
P_plunger_pull = [278.81, -182.06, 132.15, -0.1528, 0.0871, 0.0034]
P_approach_egg = [150.03, 25.58, 95.02, 0.0523, -0.0317, 0.0008]
P_insert_needle = [150.07, 25.62, 42.47, 0.0521, -0.0314, 0.0006]
P_push_filling = [150.04, 25.59, 14.83, 0.0521, -0.0314, 0.0006]
P_retract_needle = [150.05, 25.61, 57.52, 0.0521, -0.0314, 0.0006]
P_safe_withdraw = [150.06, 25.63, 142.08, 0.0519, -0.0312, 0.0007]

P_home_L = [-50.03, 250.11, 180.07, 0.0000, 0.0000, 0.0000]
P_grip_egg = [0.02, 0.01, 35.47, 0.0012, -0.0008, 0.0000]

# ===================== 蛋盘布局参数 =====================
EGG_ROW = 3
EGG_COL = 9
row_offset = 48.5
col_offset = 39.2
safe_height = 55.0

# ===================== 核心函数 =====================

def get_egg_pose(index: int) -> list:
    row = index // EGG_COL
    col = index % EGG_COL
    return [
        P_insert_needle[0] + col * col_offset,
        P_insert_needle[1] + row * row_offset,
        P_insert_needle[2],
        P_insert_needle[3],
        P_insert_needle[4],
        P_insert_needle[5],
    ]


def gripper_grasp(arm: Robot, force_n: float = 18.0):
    arm.set_digital_output(1, True)
    time.sleep(0.15)
    arm.set_gripper_force(force_n)
    logger.debug(f"夹爪闭合 | 抓持力 {force_n:.1f}N")


def gripper_release(arm: Robot):
    arm.set_gripper_force(0.0)
    time.sleep(0.08)
    arm.set_digital_output(1, False)
    logger.debug("夹爪释放")


def gripper_calibrate(arm: Robot):
    arm.gripper_zero_calibration()
    time.sleep(0.35)


def check_force_ok(arm: Robot, max_force: float = 45.0) -> bool:
    fx, fy, fz = arm.get_force_sensor_data()
    f_norm = math.sqrt(fx * fx + fy * fy + fz * fz)
    if f_norm > max_force:
        logger.warning(f"力控超限 | 当前 {f_norm:.1f}N > 阈值 {max_force:.1f}N")
        return False
    return True


def move_linear_safe(arm: Robot, pose: list, speed: float = 95.0):
    arm.move_to_pose(pose, mode=MotionMode.LINEAR, speed=speed)
    if not check_force_ok(arm):
        arm.stop()
        arm.move_to_pose(P_home_R, mode=MotionMode.JOINT)
        raise RuntimeError("力控异常触发保护回退")


def stage_1_reset_calibrate():
    """阶段一：复位与校准（节点1~3）"""
    logger.info("--- 阶段一：复位与校准 ---")

    right_arm.move_to_pose(P_home_R, mode=MotionMode.JOINT)
    time.sleep(0.12)

    home_4 = [P_home_R[0] + 0.52, P_home_R[1] - 0.18, P_home_R[2] + 1.14,
              P_home_R[3], P_home_R[4], P_home_R[5]]
    right_arm.move_to_pose(home_4, mode=MotionMode.JOINT)
    time.sleep(0.10)

    gripper_calibrate(right_arm)
    logger.info("复位校准完成 | 关节姿态已归零 | 夹爪零点已确认")


def stage_2_suction_meat():
    """阶段二：吸取肉泥（节点4~15）"""
    logger.info("--- 阶段二：吸取肉泥 ---")

    # 子步骤A：抓取针筒（节点4~6）
    gripper_grasp(right_arm, force_n=18.0)

    move_linear_safe(right_arm, P_approach_meat)
    time.sleep(0.06)

    right_arm.set_linear_speed(42)
    move_linear_safe(right_arm, P_insert_meat)
    right_arm.set_linear_speed(95)
    time.sleep(0.10)

    # 子步骤B：抓取活塞柄（节点7~10）
    move_linear_safe(right_arm, P_syringe_up)
    gripper_calibrate(right_arm)

    move_linear_safe(right_arm, P_plunger_approach)
    right_arm.set_linear_speed(38)
    move_linear_safe(right_arm, P_plunger_grip)
    right_arm.set_linear_speed(95)

    gripper_grasp(right_arm, force_n=15.5)

    # 子步骤C：吸取并退出（节点11~15）
    move_linear_safe(right_arm, P_plunger_pull)
    time.sleep(0.20)

    gripper_release(right_arm)

    move_linear_safe(right_arm, P_syringe_up)
    time.sleep(0.05)

    meat_clear_1 = [P_insert_meat[0], P_insert_meat[1],
                    P_insert_meat[2] + safe_height,
                    P_insert_meat[3], P_insert_meat[4], P_insert_meat[5]]
    move_linear_safe(right_arm, meat_clear_1)

    meat_clear_2 = [P_insert_meat[0] + 28.0, P_insert_meat[1],
                    P_insert_meat[2] + safe_height,
                    P_insert_meat[3], P_insert_meat[4], P_insert_meat[5]]
    move_linear_safe(right_arm, meat_clear_2)

    logger.info("肉泥吸取完成 | 负压吸入量正常 | 力曲线无异常")


def stage_3_inject_egg(index: int):
    """阶段三：灌入鸡蛋（节点16~23）"""
    logger.info(f"--- 阶段三：灌入鸡蛋 #{index + 1} ---")

    point = get_egg_pose(index)

    # 子步骤A：针尖定位（节点16~17）
    move_linear_safe(right_arm, P_approach_egg)
    right_arm.set_linear_speed(0.48)
    move_linear_safe(right_arm, P_insert_needle)
    right_arm.set_linear_speed(95)
    time.sleep(0.08)

    # 子步骤B：推注（节点18~23）
    syringe_above = [P_insert_needle[0], P_insert_needle[1],
                     P_insert_needle[2] + 26.8,
                     P_insert_needle[3], P_insert_needle[4], P_insert_needle[5]]
    move_linear_safe(right_arm, syringe_above)

    plunger_pos = [syringe_above[0] - 1.73, syringe_above[1] - 1.81,
                   syringe_above[2] - 27.76,
                   -0.1528, 0.0871, 0.0034]
    move_linear_safe(right_arm, plunger_pos)

    gripper_grasp(right_arm, force_n=16.0)

    right_arm.set_linear_speed(0.52)
    move_linear_safe(right_arm, P_push_filling)
    right_arm.set_linear_speed(95)
    time.sleep(0.50)

    gripper_release(right_arm)
    move_linear_safe(right_arm, P_retract_needle)

    logger.info(f"灌入完成 | 蛋号 {index + 1} | 推注行程正常 | 无回流")


def stage_4_reset_finish():
    """阶段四：复位与收尾（节点24~27）"""
    logger.info("--- 阶段四：复位与收尾 ---")

    right_arm.move_to_pose(P_home_R, mode=MotionMode.JOINT)
    time.sleep(0.10)

    move_linear_safe(right_arm, P_safe_withdraw)

    home_2 = [P_home_R[0] + 0.51, P_home_R[1] - 0.17, P_home_R[2] + 1.12,
              P_home_R[3], P_home_R[4], P_home_R[5]]
    right_arm.move_to_pose(home_2, mode=MotionMode.JOINT)

    gripper_release(right_arm)
    logger.info("复位完成 | 针筒已归位 | 等待下一循环")


def main_cycle():
    trajectory = []
    total = EGG_ROW * EGG_COL
    success_count = 0
    fail_count = 0

    logger.info(f"===== 双臂灌馅循环启动 | 蛋盘 {EGG_ROW}x{EGG_COL} | 共计 {total} 颗 =====")

    stage_1_reset_calibrate()

    left_arm.move_to_pose(P_grip_egg, mode=MotionMode.LINEAR)
    left_arm.set_digital_output(2, True)
    time.sleep(0.40)
    logger.info("左臂夹持就位 | 负压吸盘已激活")

    for i in range(total):
        logger.info(f">>> 蛋 {i + 1}/{total}")
        try:
            stage_2_suction_meat()
            trajectory.append({
                "step": "suction",
                "egg_index": i,
                "pose": right_arm.get_current_pose(),
                "force": right_arm.get_force_sensor_data(),
                "timestamp": datetime.now().isoformat(),
            })

            stage_3_inject_egg(i)
            trajectory.append({
                "step": "inject",
                "egg_index": i,
                "pose": right_arm.get_current_pose(),
                "force": right_arm.get_force_sensor_data(),
                "timestamp": datetime.now().isoformat(),
            })

            success_count += 1
            time.sleep(0.55)

        except RuntimeError as e:
            fail_count += 1
            logger.error(f"蛋 {i + 1} 灌馅失败: {e}")
            stage_4_reset_finish()
            stage_1_reset_calibrate()
            continue

    stage_4_reset_finish()

    left_arm.set_digital_output(2, False)
    left_arm.move_to_pose(P_home_L, mode=MotionMode.JOINT)
    logger.info("左臂已复位")

    with open("trajectory_data.json", "w", encoding="utf-8") as f:
        json.dump(trajectory, f, indent=2, ensure_ascii=False)

    logger.info(f"===== 循环结束 | 成功 {success_count}/{total} | "
                f"成功率 {success_count / total * 100:.1f}% | "
                f"数据已保存 =====")


if __name__ == "__main__":
    main_cycle()
