import sys
import platform

def check_environment():
    print("="*30)
    print("Physical AI Book - Environment Check")
    print("="*30)
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Platform: {platform.platform()}")
    
    # Check ROS 2
    try:
        import rclpy
        print("✅ ROS 2 (rclpy): DETECTED")
        print(f"   Version: {rclpy.__version__ if hasattr(rclpy, '__version__') else 'Unknown'}")
    except ImportError:
        print("❌ ROS 2 (rclpy): NOT DETECTED")
        print("   (Ensure you are in the devcontainer or have sourced setup.bash)")

    # Check Isaac Sim SDK (simplified check)
    try:
        import isaacsim
        print("✅ Isaac Sim SDK: DETECTED")
    except ImportError:
        print("⚠️  Isaac Sim SDK: NOT DETECTED (Expected if running locally without Isaac)")

    # Check OpenAI
    try:
        import openai
        print("✅ OpenAI: DETECTED")
    except ImportError:
        print("❌ OpenAI: NOT DETECTED (Install via pip install openai)")

if __name__ == "__main__":
    check_environment()
