day2_puzzle = '2157315-2351307,9277418835-9277548385,4316210399-4316270469,5108-10166,872858020-872881548,537939-575851,712-1001,326613-416466,53866-90153,907856-1011878,145-267,806649-874324,6161532344-6161720341,1-19,543444404-543597493,35316486-35418695,20-38,84775309-84908167,197736-309460,112892-187377,336-552,4789179-4964962,726183-793532,595834-656619,1838-3473,3529-5102,48-84,92914229-92940627,65847714-65945664,64090783-64286175,419838-474093,85-113,34939-52753,14849-303'

day2_list = day2_puzzle.split(',')

def invalid_checker_2(x):
  val = str(x)
  n = len(val)

  for i in range(1, (n // 2) + 1):

    # check i if it divides numbers evenly
    if n % i != 0:
      continue

    list_breakdown = [val[j : j+i] for j in range(0, n, i)]
    if len(set(list_breakdown)) == 1:
      return x
  return 0

def create_range(x):
  start, end = x.split('-')
  return list(range(int(start), int(end) + 1))

def main_day2p2(text):
  invalid_sum = 0

  if text:
    for i in text:
      for j in create_range(i):
        invalid_sum += invalid_checker_2(j)
  return invalid_sum


if __name__ == '__main__':
    print(main_day2p2(day2_list))