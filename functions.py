FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
	""" Reads a text file and returns a list of todos. """
	with open(filepath, "r") as local_file:
		todos_local = local_file.readlines()
	return todos_local


def write_todos(todos, filepath=FILEPATH):
	""" Write a todo items list in a text file. """
	with open(filepath, "w") as file_local:
		file_local.writelines(todos)

if __name__ == "__main__":
	print("Hello")
	print(get_todos())

