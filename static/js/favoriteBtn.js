
  $(document).ready(function(){
        $(".like").click(function(){
           $(this).toggleClass("heart");
        });
    });



var favoriteBtns = document.getElementsByClassName("like")

for(var i = 0;i < favoriteBtns.length; i++)
{
    favoriteBtns[i].addEventListener('click',function (){
        var productName = this.dataset.product
        var action = this.dataset.action
        console.log('productName:',productName,'Action:', action)

        updateUserFavorite(productName,action)

    })
}

function updateUserFavorite(productName,action)
{
    console.log('User is Connected sending data')

    var url = '/updete_favorite/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productName':productName,'action':action})
    })

    .then((response) =>{
        return response.json();
    })

    .then((data) =>{
        console.log('Data:',data)
        location.reload()
    })
}