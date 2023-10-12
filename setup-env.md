- Setup conda command in terminal vscode

```js
Ctrl + shift + P -> python: select interpreter -> choose the one has conda.exe
==> Reset terminal
```

- Create environemtn:

```js
  conda create --name <environment-name> <package-name> (package in anaconda navigator)

conda create --name myDjangoEnv django

conda create --name myDjangoEnv python=3.11.5 =>install a specific ver of python into myDjangoEnv
```

- activate / deactivate environemtn:

```js
conda activate <environemtn-name>

or

source activate <environemtn-name>

conda deactivate
```

- List all environments:

```js
conda info --envs
```

- update anaconda

```js
// Run anaconda cmd as administrator

conda update -n base -c defaults conda

```

- check version django

```js
django-admin --version
```
