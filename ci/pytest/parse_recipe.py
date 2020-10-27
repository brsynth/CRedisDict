from yaml   import safe_load as yaml_safe_load
from yaml   import YAMLError
from os     import path      as os_path
from shutil import copyfile

_env_file   = 'ci/pytest/_environment.yml'
env_file    = 'ci/pytest/environment.yml'
cmd_file    = 'ci/pytest/cmd.sh'
recipe_file = 'recipe/meta.yaml'
channels    = ['brsynth', 'conda-forge', 'defaults']

def parse_recipe():

    recipe = ''
    with open(recipe_file, 'r') as f:
        line = f.readline()
        while line:
            # filter all non-YAML elements
            if not line.startswith('{%') and '{{' not in line:
                recipe += line
            line = f.readline()

    requirements = []
    try:
        try: requirements += yaml_safe_load(recipe)['requirements']['host']
        except TypeError: pass
        try: requirements += yaml_safe_load(recipe)['requirements']['run']
        except TypeError: pass
        try: requirements += yaml_safe_load(recipe)['test']['requires']
        except TypeError: pass
        tests_cmd = yaml_safe_load(recipe)['test']['commands']
    except YAMLError as exc:
        print(exc)

    return requirements, tests_cmd

def write_dependencies(filename, requirements):
    with open(filename, 'w') as f:
        f.write('channels:\n')
        for c in channels:
            f.write('  - '+c+'\n')
        f.write('dependencies:\n')
        for req in requirements:
            f.write('  - '+req+'\n')

def write_commands(filename, cmd):
    with open(filename, 'w') as f:
        f.write(' ; '.join(tests_cmd))

if os_path.exists(_env_file) and os_path.getsize(_env_file) > 0:
    copyfile(_env_file, env_file)
else:
    requirements, tests_cmd = parse_recipe()
    write_dependencies(env_file, requirements)
    write_commands(cmd_file, tests_cmd)
