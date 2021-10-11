# References
# https://www.python.org/dev/peps/pep-0008/
# https://google.github.io/styleguide/pyguide.html#3164-guidelines-derived-from-guidos-recommendations
# https://github.com/hblanks/zen-of-python-by-example/blob/master/pep20_by_example.py


def even_numbers_half(nums):
    return [i/2 for i in nums if not i%2]

if(__name__ == '__main__'):
    print('Beautiful is better than ugly')
    print(even_numbers_half(range(100)))
