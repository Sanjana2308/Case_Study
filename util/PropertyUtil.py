class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "DESKTOP-NG62K12\\SQLEXPRESS"
        database_name = "Project1"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str