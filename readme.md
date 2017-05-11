## Creating new Docker container
docker run -it  --name intro2DL -v {Host shared folder location}:/{Container shared folder location} -p 8888:8888 -p 6006:6006 michaelkhan3/introtodeeplearning

## Restart existing docker container
This already has the ports exported and volume mounted
docker start intro2DL
docker attach intro2DL


## Starting Jupyter Notebooks
cd ..
./run_jupyter.sh --allow-root
