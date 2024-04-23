import { proxy } from "valtio";

export const store = proxy({
  filter: "all",
  todos: [],
});

const addTodo = (description: string) => {
  store.todos.push({
    description,
    status: "pending",
    id: Date.now(),
  });
};

const removeTodo = (id: number) => {
  const index = store.todos.findIndex((todo) => todo.id === id);
  if (index >= 0) {
    store.todos.splice(index, 1);
  }
};

const toggleDone = (id: number, currentStatus: Status) => {
  const nextStatus = currentStatus === "pending" ? "completed" : "pending";
  const todo = store.todos.find((todo) => todo.id === id);
  if (todo) {
    todo.status = nextStatus;
  }
};

const setFilter = (filter: Filter) => {
  store.filter = filter;
};
