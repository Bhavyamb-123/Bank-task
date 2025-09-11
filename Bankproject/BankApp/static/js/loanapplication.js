let currentStep = 1
const totalSteps = 5

function changeStep(direction) {
  const currentStepElement = document.getElementById(`step${currentStep}`)
  const currentProgressStep = document.querySelector(`.progress-step:nth-child(${currentStep})`)

  if (direction === 1) {
    // Validate current step before proceeding
    if (!validateStep(currentStep)) {
      return
    }

    // Mark current step as completed
    currentProgressStep.classList.add("completed")
    currentProgressStep.classList.remove("active")
  }

  // Hide current step
  currentStepElement.classList.remove("active")

  // Update step number
  currentStep += direction

  // Show new step
  const newStepElement = document.getElementById(`step${currentStep}`)
  const newProgressStep = document.querySelector(`.progress-step:nth-child(${currentStep})`)

  newStepElement.classList.add("active")
  newProgressStep.classList.add("active")

  // Update navigation buttons
  updateNavigationButtons()

  // Update summary if on final step
  if (currentStep === 5) {
    updateSummary()
  }

  // Scroll to top
  window.scrollTo({ top: 0, behavior: "smooth" })
}

function validateStep(step) {
  const stepElement = document.getElementById(`step${step}`)
  const requiredFields = stepElement.querySelectorAll("[required]")
  let isValid = true

  requiredFields.forEach((field) => {
    if (!field.value.trim()) {
      field.style.borderColor = "#ef4444"
      isValid = false
    } else {
      field.style.borderColor = "#d1d5db"
    }
  })

  if (!isValid) {
    alert("Please fill in all required fields before proceeding.")
  }

  return isValid
}

function updateNavigationButtons() {
  const prevBtn = document.getElementById("prevBtn")
  const nextBtn = document.getElementById("nextBtn")
  const submitBtn = document.getElementById("submitBtn")

  // Show/hide previous button
  prevBtn.style.display = currentStep > 1 ? "block" : "none"

  // Show/hide next/submit buttons
  if (currentStep === totalSteps) {
    nextBtn.style.display = "none"
    submitBtn.style.display = "block"
  } else {
    nextBtn.style.display = "block"
    submitBtn.style.display = "none"
  }
}

function updateSummary() {
  const loanAmount = document.getElementById("loanAmount").value
  const propertyValue = document.getElementById("propertyValue").value
  const downPayment = document.getElementById("downPayment").value
  const monthlyIncome = document.getElementById("monthlyIncome").value

  document.getElementById("summaryLoanAmount").textContent = loanAmount ? `₹${formatIndianCurrency(loanAmount)}` : "-"
  document.getElementById("summaryPropertyValue").textContent = propertyValue
    ? `₹${formatIndianCurrency(propertyValue)}`
    : "-"
  document.getElementById("summaryDownPayment").textContent = downPayment
    ? `₹${formatIndianCurrency(downPayment)}`
    : "-"
  document.getElementById("summaryIncome").textContent = monthlyIncome ? `₹${formatIndianCurrency(monthlyIncome)}` : "-"
}

function formatIndianCurrency(amount) {
  return new Intl.NumberFormat("en-IN").format(amount)
}

// Form submission
document.getElementById("homeLoanForm").addEventListener("submit", (e) => {
  e.preventDefault()

  // Validate final step
  if (!validateStep(5)) {
    return
  }

  // Check terms agreement
  const agreeTerms = document.getElementById("agreeTerms").checked
  const creditCheck = document.getElementById("creditCheck").checked

  if (!agreeTerms || !creditCheck) {
    alert("Please agree to the terms and conditions to proceed.")
    return
  }

  // Simulate form submission
  alert(
    "Thank you! Your home loan application has been submitted successfully. You will receive a confirmation email shortly.",
  )

  // In a real application, you would send the form data to your server here
  console.log("Form submitted successfully")
})

// Initialize form
document.addEventListener("DOMContentLoaded", () => {
  updateNavigationButtons()
})
