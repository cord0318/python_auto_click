# AutoClick π±
νμ΄μ¬μ© μ€ν ν΄λ¦­ λΌμ΄λΈλ¬λ¦¬μλλ€.

* https://pypi.org/project/auto-click/
- https://github.com/cord0318/python_auto_click

# λ€μ΄λ‘λ π₯
**μ΄ λͺ¨λμ νμ΄μ¬ λͺ¨λ  λ²μ Όμμ μ¬μ© κ°λ₯ν©λλ€.**
μλμ°λ λ¦¬λμ€μμ λ€μκ³Ό κ°μ΄ μλ ₯ν©λλ€.
```
pip install auto-click
```
μ€λ₯κ° λλ κ²½μ°, python -m pip install --upgrade pip λ‘ pipλ₯Ό μλ°μ΄νΈ ν΄μ£ΌμΈμ.

# μ¬μ©λ² π€
```python
from autoclick import AutoClick
AutoClick(right_key="<ctrl>+v", left_key="<ctrl>+x", delay=0.03)
# Default Value: right_key="v", left_key="x", delay=0.04
```

# Tip
**μ΄μ  μ€ν ν΄λ¦­μ cmdμμ μ¬μ©κ°λ₯ν©λλ€!**
```cmd
auto --help
```
λ₯Ό μ³μ μ¬μ©κ°λ₯ν©λλ€!
