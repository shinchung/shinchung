import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", required=True, help="name of file")
parser.add_argument("-v", "--value", required=True)
args = parser.parse_args()


print(f'Hi {args.name}, welcome')
print(args.value)


####################################################################
# 