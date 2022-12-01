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
    sums.sort()
    top3 = 0
    for i in range(1, 4):
      top3 += sums[-i]
    print(top3)
    

if __name__ == "__main__":
  main()