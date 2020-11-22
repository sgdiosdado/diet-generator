const MultiSelectDropDown = (options, label) => {
  const optionsHtml = options.map(option => {
    return `
    <option value="${option.value}">${option.label}</option>
    `
  })

  return `
  <div class="input-field">
    <select multiple>
      <option value="" disabled selected>Elige</option>
      ${optionsHtml}
    </select>
    <label>${label}</label>
  </div>
  `
}

export { MultiSelectDropDown }