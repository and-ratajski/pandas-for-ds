# Pandas for Data Science (Real Python) excercises

## Set up conda environment

https://stackoverflow.com/a/58068850/16775898

### Create conda environment

```shell
conda create --prefix ./pandas-for-ds-env numpy matplotlib pandas ipykernel
```

### Change environment prompt

```shell
conda config --set env_prompt '({name})'
```

### Activate conda environment

```shell
conda activate ./pandas-for-ds-env
```

### Launch notebook from base environment

```shell
conda decativate
conda activate base
conda install nb_conda_kernels
jupyter notebook
```

