import subprocess
import sys


def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


def main():
    #insert here modules you want to install
    my_packages = ['absl-py==1.0.0', 'aiohttp==3.8.1', 'aiosignal==1.2.0', 'argon2-cffi-bindings==21.2.0', 'argon2-cffi==21.3.0', 'astunparse==1.6.3', 'async-generator==1.10', 'async-timeout==4.0.2', 'attrs==21.4.0', 'autopep8==1.6.0', 'backcall==0.2.0', 'bleach==4.1.0', 'cachetools==4.2.4', 'certifi==2021.10.8', 'cffi==1.15.0', 'charset-normalizer==2.0.9', 'colorama==0.4.4', 'cryptography==37.0.1', 'cycler==0.11.0', 'debugpy==1.5.1', 'decorator==5.1.0', 'defusedxml==0.7.1', 'entrypoints==0.3', 'flatbuffers==2.0', 'fonttools==4.28.5', 'frozenlist==1.3.0', 'gast==0.4.0', 'google-auth-oauthlib==0.4.6', 'google-auth==2.3.3', 'google-pasta==0.2.0', 'grpcio==1.43.0', 'h11==0.13.0', 'h5py==3.6.0', 'idna==3.3', 'importlib-metadata==4.10.0', 'ipykernel==6.6.0', 'ipython-genutils==0.2.0', 'ipython==7.30.1', 'ipywidgets==7.6.5', 'jedi==0.18.1', 'jinja2==3.0.3', 'jsonschema==4.3.2', 'jupyter-client==7.1.0', 'jupyter-console==6.4.0', 'jupyter-core==4.9.1', 'jupyter==1.0.0', 'jupyterlab-pygments==0.1.2', 'jupyterlab-widgets==1.0.2', 'keras-preprocessing==1.1.2', 'keras==2.7.0', 'kiwisolver==1.3.2', 'libclang==12.0.0', 'markdown==3.3.6', 'markupsafe==2.0.1', 'matplotlib-inline==0.1.3', 'matplotlib==3.5.1', 'mistune==0.8.4', 'multidict==6.0.2', 'nbclient==0.5.9', 'nbconvert==6.3.0', 'nbformat==5.1.3', 'nest-asyncio==1.5.4', 'notebook==6.4.6', 'numpy==1.21.5',
                   'oauthlib==3.1.1', 'opt-einsum==3.3.0', 'outcome==1.1.0', 'packaging==21.3', 'pandas==1.3.5', 'pandocfilters==1.5.0', 'parso==0.8.3', 'pickleshare==0.7.5', 'pika==1.2.1', 'pillow==8.4.0', 'pip==21.2.4', 'prometheus-client==0.12.0', 'prompt-toolkit==3.0.24', 'protobuf==3.19.1', 'pyasn1-modules==0.2.8', 'pyasn1==0.4.8', 'pycodestyle==2.8.0', 'pycparser==2.21', 'pygments==2.10.0', 'pyopenssl==22.0.0', 'pyparsing==3.0.6', 'pyrsistent==0.18.0', 'pysocks==1.7.1', 'python-dateutil==2.8.2', 'python3-anticaptcha==1.7.1', 'pytz==2021.3', 'pywin32==303', 'pywinpty==1.1.6', 'pyzmq==22.3.0', 'qtconsole==5.2.2', 'qtpy==2.0.0', 'requests-oauthlib==1.3.0', 'requests==2.26.0', 'rsa==4.8', 'selenium==4.1.3', 'send2trash==1.8.0', 'setuptools==58.1.0', 'six==1.16.0', 'sniffio==1.2.0', 'sortedcontainers==2.4.0', 'tensorboard-data-server==0.6.1', 'tensorboard-plugin-wit==1.8.0', 'tensorboard==2.7.0', 'tensorflow-estimator==2.7.0', 'tensorflow-io-gcs-filesystem==0.23.1', 'tensorflow==2.7.0', 'termcolor==1.1.0', 'terminado==0.12.1', 'testpath==0.5.0', 'toml==0.10.2', 'tornado==6.1', 'traitlets==5.1.1', 'trio-websocket==0.9.2', 'trio==0.20.0', 'typing-extensions==4.0.1', 'urllib3==1.26.7', 'wcwidth==0.2.5', 'webencodings==0.5.1', 'werkzeug==2.0.2', 'wheel==0.37.1', 'widgetsnbextension==3.5.2', 'wrapt==1.13.3', 'wsproto==1.1.0', 'yarl==1.7.2', 'zipp==3.6.0']

    for package in my_packages:
        install(package)
        print('\n')

    print('Setup Completed')


if __name__ == '__main__':
    main()
