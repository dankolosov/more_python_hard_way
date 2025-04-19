import argparse

def handle_action(args):
    print('Hello Foo')

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--foo', help='foo help')
parser.add_argument('-a', '--action', help='action')
parser.set_defaults(func=handle_action)

args = parser.parse_args()
args.func(args)
# if args
print(args)