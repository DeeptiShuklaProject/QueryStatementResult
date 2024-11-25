import os
import pandas as pd
from myapp.models import MasterData

def import_excel_to_database(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Read Excel file
    excel_data = pd.read_excel(file_path, sheet_name=None)  # Read all sheets

    # Convert to JSON-like dictionary
    json_data = {sheet: df.to_dict(orient='records') for sheet, df in excel_data.items()}

    # Save to the database
    master_data = MasterData.objects.create(
        title="Employee Data",
        description="This dataset contains employee and department information.",
        data=json_data
    )

    return master_data
