from pymongo import MongoClient

def get_db_connection():
    """
    Connects to MongoDB Atlas cluster and returns the database instance.
    
    Returns:
        database: MongoDB database instance named 'diagnostic_system'
    """
    # Replace with your MongoDB Atlas connection string
    # Format: mongodb+srv://username:password@cluster.mongodb.net/
    connection_string = "mongodb://localhost:27017"
    
    try:
        # Create MongoDB client
        client = MongoClient(connection_string)
        
        # Get the database instance
        db = client['diagnostic_system']
        
        # Test the connection
        client.server_info()
        print("Successfully connected to MongoDB")
        
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None
