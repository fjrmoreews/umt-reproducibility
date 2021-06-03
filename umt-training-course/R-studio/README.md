
### running R studio from Docker

####  Linux
```
docker pull rocker/tidyverse:lastest

docker run -d -p 8787:8787 -v "`pwd`":/home/rstudio/working  -e USER=rstudio  -e PASSWORD=rstudio -e ROOT=TRUE rocker/tidyverse:latest

```

#### Windows (power shell)
```

$vol= (pwd).Path

docker run -d -p 8787:8787 -v ${vol}:/home/rstudio/working -e USER=rstudio -e PASSWORD=rstudio -e ROOT=TRUE rocker/tidyverse:latest
```


#### Access 
open the folloing URL witn a browser http://localhost:8787
 
login/password : rstudio/rstudio

see https://hub.docker.com/r/rocker/tidyverse
and https://github.com/rocker-org/rocker-versioned/blob/master/rstudio/README.md



#### Disabled authentication

```
docker run --rm   -p 8787:8787   -e DISABLE_AUTH=true   rocker/rstudio
```


