New feature: Product categories

We will use SBERT to sort each newly added product into categories, which we will show in the product details page( /produs/<int:produs_id> in the backend or /pagina/cauta in the frontend)
they will not be shown in the entire list of products

Add a categories table, which has an id as primary key, and a name as text unique
link it with the products table using a junction table. This will be the table we use to give categories to each product

Using SBERT, we will generate the embedding of each product, category(and input as well). We will put this in our tables, which will all contain a field(not the junction list, though)
Upon adding a new product, we run its name through a semantic search, which is compared with the categories, and we select the top 3 and assign them through the junction list.

Following this, it will be viewable in the product details page, which will contain new divs to show a certain product's categories.

Do not add any other features

Remember to keep the code as modularised as possible, do not overload a file with functions it does not need. Feel free to create new folders/files if needed.

Keep in mind my pre-existing code architecture and style

