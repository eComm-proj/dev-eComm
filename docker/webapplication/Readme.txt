Run "docker-compose up" in webapplication directory to run all these containers
then open localhost:5000 link to access web app
---------------------------------------------------------------------
Procedure to run/create webApp using docker image:

1.docker build -t <name_ofthe_image> <Dockerfile_path>
ex: docker build -t mynginximage .
2.To access the container created(web app)
docker run -p 5000:5000 --name=<name of the container>; here port specified in Dockerfile
ex: docker run -p 5000:5000 --name=App2 mynginximage
3.Goto localhost:5000 to access webpage