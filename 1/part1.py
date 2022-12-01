def main():
  with open('input.txt', 'r') as f:
    nums = f.readlines()
    sums = []
    sum = 0
    for num in nums:
      if num != '\n':
        sum += int(num)
      else:
        sums.append(sum)
        sum = 0
    print(max(sums))

if __name__ == "__main__":
  main()