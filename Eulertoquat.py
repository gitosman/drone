import numpy as np

# Roll, pitch, and yaw angles in degrees

def euler_to_quat(pitch):
    roll_degrees = 0
    pitch_degrees = pitch
    yaw_degrees = 0

    # Convert degrees to radians
    roll_radians = np.radians(roll_degrees)
    pitch_radians = np.radians(pitch_degrees)
    yaw_radians = np.radians(yaw_degrees)

    # Calculate trigonometric functions
    c1 = np.cos(roll_radians / 2.0)
    s1 = np.sin(roll_radians / 2.0)
    c2 = np.cos(pitch_radians / 2.0)
    s2 = np.sin(pitch_radians / 2.0)
    c3 = np.cos(yaw_radians / 2.0)
    s3 = np.sin(yaw_radians / 2.0)

    # Calculate quaternion elements
    w = c1*c2*c3 - s1*s2*s3
    x = s1*c2*c3 + c1*s2*s3
    y = c1*s2*c3 - s1*c2*s3
    z = c1*c2*s3 + s1*s2*c3

    # Normalize quaternion
    q = np.array([w, x, y, z])
    q /= np.linalg.norm(q)
    print(q)
