FROM cannin/jupyter-r

RUN R -e "install.packages('ggplot2',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('pastecs',dependencies=TRUE, repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('sjmisc',dependencies=TRUE, repos='http://cran.rstudio.com/')"

