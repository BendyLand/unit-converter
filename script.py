import test
import conversion

def main():
    args, cl_call = conversion.check_cl_args()
    if cl_call:
        conversion.convert(args)
    else:
        test.test_temperature()
        test.test_distance()
        test.test_mass()
        test.test_my_time()
        print()


if __name__ == "__main__":
    main()
