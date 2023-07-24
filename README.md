# custom_logger
Python Custom Logger - override log format using log guru and write it to a designated file
To run the project .. 
1. clone the repo
2. create and activate virtual env (
  python3 -m venv env
  source env/bin/activate
)
3. install the required plugins (pip install -r requirements.txt)
4. run project (uvicorn app.main:app)
5. everything will be logged in access.log file in the root folder
6. sample end points (
  curl --location 'http://127.0.0.1:8000/',
  curl --location 'http://127.0.0.1:8000/users/'
)
