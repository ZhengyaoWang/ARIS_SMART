# direct_kinematics

from math import acos, cos, sin, atan2, atan, degrees, radians, hypot


def calculate_arm1_top_boarder(theta, arm_length, arm_width):
    RT_phi = atan(arm_width / 2 / arm_length)
    RT_radius = hypot(arm_length, (arm_width / 2))
    RT_theta = theta - RT_phi
    RT_x = RT_radius * cos(RT_theta)
    RT_y = RT_radius * sin(RT_theta)

    LT_phi = atan(arm_width / 2 / arm_length)
    LT_radius = hypot(arm_length, (arm_width / 2))
    LT_theta = theta + LT_phi
    LT_x = LT_radius * cos(LT_theta)
    LT_y = LT_radius * sin(LT_theta)

    RB_theta = theta - radians(90)
    RB_x = arm_width / 2 * cos(RB_theta)
    RB_y = arm_width / 2 * sin(RB_theta)

    LB_theta = theta + radians(90)
    LB_x = arm_width / 2 * cos(LB_theta)
    LB_y = arm_width / 2 * sin(LB_theta)

    return RT_x, RT_y, LT_x, LT_y, RB_x, RB_y, LB_x, LB_y


def direct_kinematics(theta1, theta2, arm1_length, arm2_length, a1_width):
    #theta1 and theta2 are provided in radians

    elbow_x = arm1_length * cos(theta1)  # arm1 end point x
    print(f"direct theta1 = {theta1}")
    print(f"direct elbow_x = {elbow_x}")
    elbow_y = arm1_length * sin(theta1)  # arm1 end point y
    tool_x = elbow_x + arm2_length * cos(theta1 + theta2)  # tool end x
    tool_y = elbow_y + arm2_length * sin(theta1 + theta2)  # tool end y

    # Calculate the arm boarder points
    RT_x, RT_y, LT_x, LT_y, RB_x, RB_y, LB_x, LB_y = calculate_arm1_top_boarder(theta1, arm1_length, a1_width)

    return {
        'elbow_x': elbow_x,
        'elbow_y': elbow_y,
        'tool_x': tool_x,
        'tool_y': tool_y,
        'border_points': (RT_x, RT_y, LT_x, LT_y, RB_x, RB_y, LB_x, LB_y)
    }
