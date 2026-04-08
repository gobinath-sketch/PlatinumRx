import psycopg2
import sys
import os

import os

# Securely load environment variables from .env
if os.path.exists(".env"):
    with open(".env") as f:
        for line in f:
            if "=" in line:
                key, value = line.split("=", 1)
                os.environ[key.strip()] = value.strip().strip('"').strip("'")

# Verified Supabase Connection (Loaded from .env)
DB_URL = os.getenv("DB_URL")

def run_sql_file(filename):
    print(f"\n--- Executing {filename} ---")
    try:
        print(f"Attempting to connect to Supabase...")
        conn = psycopg2.connect(DB_URL, connect_timeout=10)
        print("Connected successfully!")
        cur = conn.cursor()
        
        with open(filename, 'r', encoding='utf-8') as f:
            sql = f.read()
            # Remove any Supabase-incompatible commands if necessary
            # Split by semicolon to run statements one by one for better error reporting
            statements = sql.split(';')
            for i, stmt in enumerate(statements):
                if stmt.strip():
                    try:
                        cur.execute(stmt)
                    except Exception as stmt_err:
                        print(f"Error in statement {i+1}: {stmt_err}")
                        print(f"Statement: {stmt.strip()[:100]}...")
                        # If it's a 'TABLE ALREADY EXISTS' or similar, we might want to continue
                        if "already exists" in str(stmt_err).lower():
                            continue
                        raise stmt_err
        
        conn.commit()
        cur.close()
        conn.close()
        print(f"Successfully finished {filename}")
    except Exception as e:
        print(f"Fatal error executing {filename}: {e}")
        # Check if it's a DNS issue and suggest fix
        if "could not translate host name" in str(e):
            print("TIP: This might be a temporary DNS issue or IPv6 related. Try running again.")

if __name__ == "__main__":
    # Ensure current working directory is the project root
    # (The user has workspace at c:\Users\gobin\OneDrive\Desktop\sys)
    
    sql_files = [
        "SQL/01_Hotel_Schema_Setup.sql",
        "SQL/03_Clinic_Schema_Setup.sql"
    ]
    
    for sql_file in sql_files:
        if os.path.exists(sql_file):
            run_sql_file(sql_file)
        else:
            print(f"File not found: {sql_file}")
