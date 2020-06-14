## Getting Started

1. First, you'll need to activate a virtual environment 
with the name venv/ in this project directory. `$ virtualenv venv`

2. From there, activate the virtual environment with
`$ source venv/bin/activate`

3. Once activated, install the necessary requirements.
`$ pip install -r requirements.txt`

4. Now you're all set! To run the file, the format is as follows:
`$ python summarize <column_name>`. This will create a summary 
statistics output based on the given `column_name`. For example,
`$ python summarize Artist` will print out summary statics
partitioning the data based on the Artist column. 

5. Boom