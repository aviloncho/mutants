import time
import mutant
from tests import fixtures


def main():

    print(mutant.is_mutant(fixtures.EXAMPLE))


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
