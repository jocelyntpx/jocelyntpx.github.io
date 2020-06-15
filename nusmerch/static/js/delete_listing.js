var updateBtns = document.getElementsByClassName('delete-product')

for (i=0; i<updateBtns.length;i++){
	updateBtns[i].addEventListener('click',function(){
		var productId = this.dataset.product
		var action = this.dataset.action
		console.log('productId:',productId,'Action:',action);

		console.log('USER',user);
		if(user === 'AnonymousUser'){
			console.log('Not logged in');
        }else{
            deleteProduct(productId,action)
        }
    })
}

function deleteProduct(productId,action){
    console.log('User is authenticated,sending data...');

        var url ='/delete_product/'

        fetch(url,{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
                'X-CSRFTOKEN':csrftoken,
            },
            body:JSON.stringify({'productId':productId,'action':action})
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('Data:',data)
            location.reload()

        });
}