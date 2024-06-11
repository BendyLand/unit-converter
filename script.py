import test
import conversion

def main():
    args, ok = conversion.check_cl_args()
    if ok:
        conversion.convert(args)
        return
    test.test_temperature()
    test.test_distance()
    test.test_mass()
    test.test_my_time()
    print()


if __name__ == "__main__":
    main()
