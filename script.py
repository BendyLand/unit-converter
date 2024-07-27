import test
import conversion

def main():
    args, cl_call = conversion.check_cl_args()
    if cl_call:
        conversion.convert(args)
        

if __name__ == "__main__":
    main()
