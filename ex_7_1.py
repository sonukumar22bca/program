print("EXCEPTION HANDLING")

try:
    num1, num2 = map(float, input("Enter two numbers (comma-separated): ").split(","))
    print("Result:", num1 / num2)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("*** End of program ***")
