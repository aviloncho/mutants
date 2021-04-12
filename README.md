# mutants
Find mutants

## Install

### Preparing enviroment
> It's recommended to use Python venv to create an isolated environment.

### Creating Python venv
```bash
$ python -m venv .venv
```
### Activating Python venv

>> #### Unix systems:
>> ```bash
>> $ source .venv/bin/activate
>> ```
>
>> #### Windows:
>> ```bash
>> $ .venv\Scripts\activate
>> ```

### Installing dependencies:
```bash
$ pip install -r requirements.txt
```

## Starting web server for REST API
```bash
$ uvicorn main_api:app --reload
```
> It should be runing on http://127.0.0.1:8000