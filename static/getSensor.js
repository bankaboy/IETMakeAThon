function getSensor(){
  $.ajax({
    url:"/getSensor",
    success: function(data){
      console.log(data);
      document.getElementById('moisture2').innerHTML = data['moisture']+"%";
      document.getElementById('temp2').innerHTML = data['temp'];
      document.getElementById('ph2').innerHTML = data['ph']; 
    }
  })
}
setInterval(getSensor, 1000);
