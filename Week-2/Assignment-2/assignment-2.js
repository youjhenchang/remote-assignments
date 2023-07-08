// Request 1: Click to Change Text.
// When user clicks on "Welcome Message" block, change text to "Have a Good Time!".

const element = document.querySelector('.welcome-message');
    element.addEventListener("click",()=>{
        element.innerHTML = "<h1>Have a Good Time!</h1>";
        }
    )
// Request 2: Click to Show More Content Boxes.
// There are some more content boxes waiting to show. When user clicks the Call-to-Action
// button, show those hidden content boxes.
const btn = document.querySelector('.button');
const grid2 = document.querySelectorAll('.content-grid-2');
    btn.addEventListener("click",()=>{
        for (let grid of grid2) {
            if (grid.style.display == "none"){
                grid.style.display = "flex";
            } else{
                grid.style.display = "none";
              }
        }
    })