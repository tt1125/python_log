def greedy_activity_selection(s, f, n):
    A = [0]
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m

    return A


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
n = len(s)
selected_activities = greedy_activity_selection(s, f, n)
print(selected_activities)
