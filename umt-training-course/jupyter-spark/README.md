
## run spark (pyspark) in jupyter 

run jupyter with R kernel

```
docker pull jupyter/pyspark-notebook

sudo chmod -R 777 ./
docker run -it --rm -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/pyspark-notebook
```
  

 

```
 
```



 
