document.addEventListener('DOMContentLoaded', function() {
  let elems = document.querySelectorAll('select');
  let options = {}
  let instances = M.FormSelect.init(elems, options);
});

function getBMI(){
  console.log("Hola");
  //get inputs
  var height = document.getElementById("Estatura").value;
  var weight = document.getElementById("Peso").value;
  height = height / 100;

  var BMI = weight / (height * height);
  if(BMI == Number.POSITIVE_INFINITY || BMI == 0){
    document.getElementById("IMCres").value = "IMC";
  }else{
    document.getElementById("IMCres").value = BMI;
  }
}
