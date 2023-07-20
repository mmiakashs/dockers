import yaml

with open('env_residual_prompt.yaml') as file:
    # The FullLoader parameter handles the conversion from YAML
    # scalar values to Python the dictionary format
    environment = yaml.load(file, Loader=yaml.FullLoader)

    dependencies = environment['dependencies']

    pip_packages = []

    for dependency in dependencies:
        if isinstance(dependency, str):
            # Conda packages have a simple string format
            pip_packages.append(dependency.split('=')[0])
        elif isinstance(dependency, dict) and 'pip' in dependency:
            # Pip packages are listed under 'pip' in a subdictionary
            pip_packages += dependency['pip']

    print(' \\\n'.join(pip_packages))

