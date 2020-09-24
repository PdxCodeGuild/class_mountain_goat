# Lab 2: Todo

## Part 1

Let's create a simple todo app. This can be done with a single model `TodoItem` which contains a CharField `description`, a DateTimeField `created_date`, a nullable DateTimeField `completed_date`. Newly created `TodoItem`s should have a `null` completed date. The index page should have a list of all the todo items (showing only the name), with completed items in a separate list (or at the bottom of the existing list) with grey color and maybe a line through them.. There should also be a text field and a button (in a form), When the clicks the button it should saves a new todo item to the database and shows the newly-added item in the list. Use one view to render the template, and another view to receive the form submission and redirect back to the first view.

## Part 2

Add `complete` and `delete` buttons next to each todo item, these can be `a` tags which link to other views which take the `id` of the todo item in the path. These views can now redirect back to the first view.

## Part 3

Add a `Priority` model with a `name` field (e.g. low, medium, high). Then add a `ForeignKeyField` to the `TodoItem` linking it to a `Priority`. The form for creating a todo item should also have a dropdown list for selecting the priority. Display the priority in the list of todo items.

