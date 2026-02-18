def calculator():
    try:
        n = input("Enter value (example: 10+5): ")

        if "//" in n:
            nums = list(map(float, n.split("//")))
            result = nums[0]
            for i in nums[1:]:
                result //= i
            print("Result =", result)

        elif "+" in n:
            nums = list(map(float, n.split("+")))
            print("Result =", sum(nums))

        elif "-" in n:
            nums = list(map(float, n.split("-")))
            result = nums[0]
            for i in nums[1:]:
                result -= i
            print("Result =", result)

        elif "*" in n:
            nums = list(map(float, n.split("*")))
            result = 1
            for i in nums:
                result *= i
            print("Result =", result)

        elif "/" in n:
            nums = list(map(float, n.split("/")))
            result = nums[0]
            for i in nums[1:]:
                result /= i
            print("Result =", result)

        elif "%" in n:
            nums = list(map(float, n.split("%")))
            result = nums[0]
            for i in nums[1:]:
                result %= i
            print("Result =", result)

        else:
            print("Invalid operator")

    except ValueError:
        print(" Enter only numbers and operators (+ - * / // %)")
        calculator()

    except ZeroDivisionError:
        print(" Zero cannot be used as denominator")
        calculator()


calculator()
