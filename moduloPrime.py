#set of primes
P = primes(10^7)
M = []
def plot_dist(n):
  for i in P:
    pmod = Mod(i,n)
    M.append(pmod)
  return M
L = plot_dist(15)
stats.TimeSeries(L).plot_histogram()
