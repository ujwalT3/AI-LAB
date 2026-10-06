import heapq
import random

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(abs(i//3 - s.index(x)//3) +
               abs(i%3 - s.index(x)%3)
               for i, x in enumerate(s) if x)

def astar(start):
    pq = [(h(start), 0, start, [])]
    seen = set()

    while pq:
        f, g, s, path = heapq.heappop(pq)

        if s == GOAL:
            return path + [s]

        if s in seen:
            continue
        seen.add(s)

        z = s.index(0)
        r, c = divmod(z, 3)

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < 3 and 0 <= nc < 3:
                nz = nr * 3 + nc
                ns = list(s)
                ns[z], ns[nz] = ns[nz], ns[z]
                ns = tuple(ns)

                heapq.heappush(
                    pq, (g + 1 + h(ns), g + 1, ns, path + [s])
                )

def random_puzzle():
    s = list(GOAL)

    # Shuffle by making random valid moves.
    # This guarantees the puzzle is solvable.
    z = 8
    for _ in range(random.randint(10, 30)):
        r, c = divmod(z, 3)
        moves = []

        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                moves.append(nr * 3 + nc)

        nz = random.choice(moves)
        s[z], s[nz] = s[nz], s[z]
        z = nz

    return tuple(s)

def show(s):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x else "_" for x in s[i:i+3]))
    print()

while True:
    print("\n--- 8 PUZZLE ---")
    print("1. Generate random puzzle")
    print("2. Enter your own puzzle")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        start = random_puzzle()

    elif choice == "2":
        nums = list(map(int, input(
            "Enter 9 numbers (0 = blank): "
        ).split()))

        if sorted(nums) != list(range(9)):
            print("Invalid puzzle!")
            continue

        start = tuple(nums)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")
        continue

    print("\nStarting puzzle:")
    show(start)

    input("Press Enter to run A*...")

    solution = astar(start)

    print("\nSolution found!")
    print("Moves:", len(solution) - 1)

    for i, state in enumerate(solution):
        print("Step", i)
        show(state)
        input("Press Enter for next step...")
