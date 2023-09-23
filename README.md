# Moyeni.tn : a python script to calculate engineering semester 1 in tekup university
 
## How to use it

1. create a json from the template with your marks
2. use the created json filename in line 63 :
    ```python
    moy_matiere = fetch_note("student.json", module, mat)
    ```
3. execute the script :
   ```bash
   python3 main_moy.py
   ```