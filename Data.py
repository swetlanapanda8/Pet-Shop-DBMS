# TASK 1

# class Data:
#     def __init__(self, database):
#         print("Connecting to database")

#     def begin_tran(self):
#         print("Beginning a transaction")

#     def commit(self):
#         print("Committing transaction")

#     def rollback(self):
#         print("Rolling back transaction")

#     def insert(self, table, obj):
#         print(f"Inserting {obj.get_name()} into table {table}")


# TASK 2

class Data:
    def __init__(self, database):
        print("Connecting to database")

    def begin_tran(self):
        print("Beginning a transaction")

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def insert(self, table, obj):
        print(f"Inserting {obj.get_name()} into table {table}")
