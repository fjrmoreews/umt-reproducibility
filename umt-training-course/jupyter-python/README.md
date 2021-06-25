## run jupyter

run jupyter

```
docker pull jupyter/scipy-notebook
docker run -it --rm -p 8888:8888 -v "${pwd}:/home/jovyan/work" jupyter/scipy-notebook
```
