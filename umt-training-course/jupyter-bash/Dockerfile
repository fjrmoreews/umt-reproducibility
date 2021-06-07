

FROM jupyter/pyspark-notebook
USER root

 
RUN pip install bash_kernel && python -m bash_kernel.install

# Allow using 'su -' 
RUN chpasswd <<<"root:root" && sed -Ei 's/(.*pam_deny.so)/# \1/' /etc/pam.d/su
RUN apt-get update
RUN  apt-get -y install mlocate 
 
USER $NB_UID
EXPOSE 8888
