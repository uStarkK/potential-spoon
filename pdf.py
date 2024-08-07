import pandas as pd
import numpy as np

generate_csv(file_name)

    data = {
        'Name': [f'Name_{i}' for i in range(20)],
        'Age': np.random.randint(18, 70, size=20),
        'Email': [f'user{i}@example.com' for i in range(20)],
        'Phone': [f'(123) 456-{str(i).zfill(4)}' for i in range(20)],
        'Address': [f'{i} Main St, City, Country' for i in range(20)],
        'Occupation': np.random.choice(['Engineer', 'Doctor', 'Artist', 'Teacher', 'Scientist'], size=20),
        'Salary': np.random.randint(30000, 120000, size=20),
        'Department': np.random.choice(['HR', 'IT', 'Sales', 'Marketing', 'Finance'], size=20),
        'Join Date': pd.date_range(start='2020-01-01', periods=20, freq='M').strftime('%Y-%m-%d').tolist(),
        'Status': np.random.choice(['Active', 'Inactive', 'On Leave'], size=20),
    }

    df = pd.DataFrame(data)
    
    df.to_csv(file_name, index=False)  # 
    print(f'{file_name} has been created.')

for i in range(1, 4):
    generate_cvs(f'sample_data_{i}.csv') 