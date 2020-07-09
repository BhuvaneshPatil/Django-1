var updateBtn=document.getElementsByClassName('update-cart')
console.log(csrftoken);
// for (var i = 0; i < updateBtn.length; i++) {
//     updateBtn[i].addEventListener('click',function(){
//         var productID=this.dataset.product
//         var action=this.dataset.action
//         console.log("Product ID " , productID ," Action ",action)

//         console.log("USer ",user);
//         if(user==='AnonymousUser'){
//             console.log("Not Logged In");
//         }
//         else{
//             console.log("Successfully Logged in");
//         }
//     })

    
// }

for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click',function(){
        var productID=this.dataset.product
        var action=this.dataset.action
        console.log("Product ID " , productID ," Action ",action)

        console.log("USer ",user);
        if(user==='AnonymousUser'){
            console.log("Not Logged In");
        }
        else{
            updateUserOrder(productID,action)
        }
    })

    
}

function updateUserOrder(productID,action){
    console.log("User Is logged in, Sending data..");
    url='/update-item/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({
            'productID':productID,
            'action':action
        })
    })

    .then(response => response.json())
    .then(data => {
        console.log('data ',data)
        location.reload()} )

}