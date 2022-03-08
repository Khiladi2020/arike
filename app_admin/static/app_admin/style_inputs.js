console.log("!! style inputs script active !!")

// get all input tags 
all_fields = document.querySelectorAll("form p")

for(let field of all_fields){
    // modify p tag
    field.className = "grid grid-cols-2 my-6"
    // field.className = "flex flex-col"

    // modify label
    field.children[0].className = "font-medium"

    // modify form input
    field.children[1].className = "bg-white rounded-md p-2"
}