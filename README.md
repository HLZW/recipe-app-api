# recipe-app-api
Recipe API project

`docker build .`
`docker-compose build`
`docker-compose run --rm app sh -c "flake8"`

# create a django project in the current directory
` docker-compose run --rm app sh -c "django-admin startproject app ."` 

--rm will remove the container once it is finished running
app will call app service
sh -c will run shell command 


# after set up db on docker-compose.yml
`docker-compose up`
# To clear containers
`docker-compose down`
