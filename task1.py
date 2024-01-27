import heapq

cables = [1, 2, 3, 4, 3, 7, 10, 20]
heapq.heapify(cables)
total_val = 0
while len(cables) > 1:
    cable_1 = heapq.heappop(cables)
    cable_2 = heapq.heappop(cables)
    new_cable = cable_1 + cable_2

    heapq.heappush(cables, new_cable)
    total_val += new_cable
    print(f"{cable_1}+{cable_2} new_cable {new_cable} Total: {total_val}")
    print(f"{cables = }")


print(f"{total_val = }")
