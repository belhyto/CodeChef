def is_subset_sum_recursive(nums, n, target_sum, subset=[]):
    if target_sum == 0:
        print("Subset with the given sum:", subset)
        return True

    if n == 0 or target_sum < 0:
        return False

    include = is_subset_sum_recursive(nums, n - 1, target_sum - nums[n - 1], subset + [nums[n - 1]])

    exclude = is_subset_sum_recursive(nums, n - 1, target_sum, subset)

    return include or exclude

def is_subset_sum(nums, target_sum):
    n = len(nums)
    if is_subset_sum_recursive(nums, n, target_sum, []):
        print("Subset with the given sum exists.")
    else:
        print("No subset with the given sum exists.")

if __name__ == "__main__":
    nums = [1, 3, 5, 7, 9]
    target_sum = int(input("Enter the target sum: "))
    is_subset_sum(nums, target_sum)
