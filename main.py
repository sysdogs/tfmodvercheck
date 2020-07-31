import argparse
import json


class Module(object):
    def __init__(self, key, source, version, module_dir):
        self.key = key
        self.source = source
        self.version = version
        self.dir = module_dir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, help='path to modules.json')
    args = parser.parse_args()

    modules = []

    with open(args.path) as stream:
        input_data = json.loads(stream.read())

    for module in input_data['Modules']:
        if not all(key in module for key in ('Key', 'Source', 'Version', 'Dir')):
            continue

        modules.append(Module(module['Key'], module['Source'], module['Version'], module['Dir']))

    sources = list(set([module.source for module in modules]))
    diverged = False

    for source in sources:
        same_source_modules = [module for module in modules if module.source == source]
        uniques = list({object_.version: object_ for object_ in same_source_modules}.values())

        if len(uniques) > 1:
            diverged = True
            print('Diverged module version detected for module: {}'.format(source))
            print('Resources:')

            for res in uniques:
                print('Directory: {}, key: {}, version: {}'.format(res.dir, res.key, res.version))

    if diverged:
        exit(1)
    else:
        exit(0)


main()
