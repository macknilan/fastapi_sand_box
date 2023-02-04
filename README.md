Instalar las dependencias en carpeta `lib`, dentro del directorio para después crear el archivo `.zip`

```bash
# -t, --target <dir>
pip install -t lib -r requirements.txt
```

Crear el archivo `.zip` de la carpeta creada `lib`

```bash
(cd lib; zip -r9 ../lambda_function.zip .)
```

Agregar el archivo `main.py` al archivo `.zip`

```bash
# -u, update
zip lambda_function.zip -u main.py
```

Agregar el archivo `books.json` al archivo `.zip`

```bash
# -u, update
zip lambda_function.zip -u books.json
```

En caso de que se requiera matar el proceso `uvicorn api.main:app --reload`

```bash
lsof -i :8000
```

```bash
kill -9 <PID>
```


```bash
```

```bash
```

```bash
```
