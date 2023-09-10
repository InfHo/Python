# Infho Python Cheat Sheet

### Um dinge in der Kommandozeile auszugeben:
```python
print("Dies steht jetzt in der Kommandozeile!")
```



### Datentypen
Strings (immer in Anführungszeichen), bsp: "a12 3_ä" / "Hallo" / "123" <br>
Integer (ganze Zahlen), bsp: 1 / 44123 / 34567<br>
Float (Kommazahlen, immer mit . getrennt), bsp: 8.67 / 1.2<br>
Booleans (Wahrheitswerte): True / False<br>

### kann durch type(xy) bestimmt werden
```python
type("Hallo")
type(123)
type(4.6)
type(True)
```

## Variablen
sind Platzhalter, denen ein Wert zugewiesen werden kann

### können alle Datentypen enthalten, zB Strings:
```python
text = "Dies int ein Text!"
wahrheit = True
zahl = 129
float = 7.89
```


## Namen
können Buchstaben, Zahlen, und _ enthalten
Dürfen nicht mit Zahl beginnen
```python
abc = 23
de5 = 45
_ab = 56
```

## Operatoren
### sind die operatoren, mit denen man rechnen kann.

Es gibt folgende:

Operator | Bedeutung
--- | --- 
\+ | plus
\-  | minus
\*  | mal
\** | Potenz
\/  | geteilt
\// | geteilt ohne Rest
\% | Modulo
so wendet man sie an: <br>

```python
a = 33
b = a-7
ergebnis = a + b
```
