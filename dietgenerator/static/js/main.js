import { MultiSelectDropDown } from './MultiSelectDropDown.js'

let dropdownInstances
const groupsUrl = document.location.origin + '/groups/'
const generateDietUrl = document.location.origin + '/generate-diet/'

document.addEventListener('DOMContentLoaded', function() {
  const getRecommendation = document.getElementById('getRecommendation')
  const height = document.getElementById('height')
  const weight = document.getElementById('weight')

  let modal = document.querySelector('.modal');
  modal = M.Modal.init(modal, {});
  
  let groupDropdowns = []
  
  fetch(groupsUrl)
  .then(res => res.json())
  .then(data => {
    const excludes = document.getElementById('excludes')
    
    for (let group of data) {
      let categories = group.categories.map(c => (
        {'value': c.id, 'label': c.name}
        ))
      groupDropdowns.push(MultiSelectDropDown(categories, group.name))
    }
    for(let group of groupDropdowns) {
      excludes.innerHTML += group
    }
    
    let elems = document.querySelectorAll('select')
    let options = {}
    dropdownInstances = M.FormSelect.init(elems, options)
  })

  getRecommendation.addEventListener('click', _ => {
    const weight = Number(document.getElementById("weight").value)
    const height = Number(document.getElementById("height").value)
    let exclude_categories = []

    for(let instance of dropdownInstances) {
      let instance_values = instance.getSelectedValues().filter(x => x !== "")
      exclude_categories = exclude_categories.concat(instance_values)
    }

    const payload = {
      weight, height, exclude_categories
    }
    const options = {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(payload)
    }
    fetch(generateDietUrl, options)
    .then(res => {
      if (res.status - 200 > 100) {
        console.log('Error del usuario')
      }
      return res.json()
    })
    .then(data => {
      let modalContent = ""
      for (let group of data) {
        modalContent += `
        <div class="mb-4">
          <h3 class="text-2xl mb-2">${group.name}</h3>
          <ul>
            ${group.categories.map(m => 
              m.foods.map(f => `<li>${Math.ceil(f.portion)}${f.portion_unit == 'g'? f.portion_unit : ' ' + f.portion_unit } ${f.name.toLowerCase()}</li>`).join("")
            )}
          </ul>
        </div>
        `
      }
      document.getElementById('modal-content').innerHTML = modalContent
      modal.open()
    })
    .catch(err => {})
  })

  document.querySelectorAll('.imc-field').forEach(el => {
    el.addEventListener('change', getBMI)
  })

  function getBMI() {
    const imc = document.getElementById("imc")
    const weight = Number(document.getElementById("weight").value)
    const height = Number(document.getElementById("height").value) / 100
    const BMI = weight / (height * height)
    
    if (!BMI || BMI === Number.POSITIVE_INFINITY) {
      imc.textContent = "IMC"
    }else {
      imc.textContent = String(BMI.toPrecision(4))
    }
  }
})
