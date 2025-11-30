import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the stress_detection database and required tables"""
    
    try:
        # Connect to MySQL without specifying a database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Radha@12345"
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database
            print("Creating database 'stress_detection'...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS stress_detection")
            cursor.execute("USE stress_detection")
            
            # Create users table
            print("Creating 'users' table...")
            create_users_table = """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_users_table)
            
            # Create stress_results table
            print("Creating 'stress_results' table...")
            create_results_table = """
            CREATE TABLE IF NOT EXISTS stress_results (
                result_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT NOT NULL,
                stress_score FLOAT NOT NULL,
                beats_per_minute INT NOT NULL,
                date_recorded DATETIME NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
            """
            cursor.execute(create_results_table)
            
            connection.commit()
            print("✓ Database 'stress_detection' and tables created successfully!")
            
    except Error as err:
        print(f"Error: {err}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
