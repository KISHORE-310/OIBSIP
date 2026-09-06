# OIBSIP Run Guide

1. Open PowerShell inside the `OIBSIP` folder.
2. `python -m venv .venv`
3. `.venv\Scripts\Activate.ps1`
4. `pip install -r requirements.txt`
5. `python download_datasets.py`
6. `jupyter notebook`
7. Run each notebook with **Restart & Run All**.
8. Save the executed notebooks.
9. Push the complete folder to GitHub repository `OIBSIP`.
10. Submit the required repository link and task files through the official Oasis form.

If PowerShell blocks activation for the current session, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` and activate again.
