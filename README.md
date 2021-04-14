<p align="center">
<a href="https://travis-ci.com/aviloncho/mutants" target="_blank">
    <img src="https://travis-ci.com/aviloncho/mutants.svg?branch=main" alt="build">
</a>

# mutants
Find mutants analyzing human DNA sequences.

---

## Live API

- [Live API](https://mutants-dna-api.herokuapp.com/)

- [API Documentation](https://mutants-dna-api.herokuapp.com/docs)

---

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
> It should be runing on your [localhost](http://127.0.0.1:8000).
>
> See [local documentation](http://127.0.0.1:8000/docs).