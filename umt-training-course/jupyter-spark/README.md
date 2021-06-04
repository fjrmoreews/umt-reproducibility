
##  run spark (pyspark) in jupyter 

run jupyter with pyspark

linux:

```
docker pull jupyter/pyspark-notebook

sudo chmod -R 777 ./
docker run -it --rm -p 8888:8888 -v $PWD:/home/jovyan/work jupyter/pyspark-notebook
```

windows


```
docker pull jupyter/pyspark-notebook

#sudo chmod -R 777 ./
$vol= (pwd).Path
docker run -it --rm -p 8888:8888 -v ${vol}:/home/jovyan/work jupyter/pyspark-notebook
```

 

## RDDs, Dataframes and Datasets

|                               | **RDD **                                 | **Dataframe **                           | **Dataset **                             |
| ----------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| **Data Representation**       | RDD is a distributed collection of data elements without schema. | A distributed collection organized into the named columns | Extension of Dataframe  with type-safety and object-oriented interface. |
| **Optimization**              | No in-built optimization engine for RDDs. Developers need to write the optimized code themselves. | It uses a catalyst optimizer for optimization. | Catalyst optimizer for optimization purposes. |
| **Projection of Schema**      | user defined   schema                    | discover schema using   SQL Engine.      | discover schema using   SQL              |
| **Aggregation Operations**    | slower  to perform simple operations like grouping the data. | API to perform aggregation operations.fast aggregation | Dataset is faster than RDD   slower than Datafram. |
| **Serialization**             | Java serialization. expensive            | off-heap storage in binary format        |                                          |
| **Compile- Time Type Safety** | oui                                      | non                                      | oui                                      |
| **Lazy Evaluation**           | oui                                      | oui                                      |                                          |
| **example Usage**             | low-level transformation and actions     | high level of abstraction and for unstructured data, such as media streams or streams of text. |                                          |

 