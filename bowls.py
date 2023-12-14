#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

n = 6
#TODO given n - number of rows write a function that gives the
# sum of all bowls

def sum_of_bowls_sequence(n):
    return n * (n + 1)/2

def sum_of_bowls_loop(n):
    return sum([x for x in range(1, n+1)])


print('Sum using sequences: {}'.format(sum_of_bowls_sequence(n)))
print('Sum using loop: {}'.format(sum_of_bowls_loop(n)))
