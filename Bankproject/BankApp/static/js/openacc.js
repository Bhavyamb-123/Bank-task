// Authentication state management
let isLoggedIn = false
let currentUser = null

function showLogin() {
  // Simulate login process
  const email = prompt("Enter your email:")
  if (email) {
    login(email)
  }
}

function showSignUp() {
  // Simulate signup process
  const email = prompt("Enter your email to sign up:")
  if (email) {
    login(email)
  }
}

function login(email) {
  isLoggedIn = true
  currentUser = email
  updateAuthDisplay()
}

function logout() {
  isLoggedIn = false
  currentUser = null
  updateAuthDisplay()
}

function updateAuthDisplay() {
  const authButtons = document.getElementById("auth-buttons")
  const userInfo = document.getElementById("user-info")
  const usernameDisplay = document.getElementById("username-display")

  if (isLoggedIn && currentUser) {
    authButtons.style.display = "none"
    userInfo.style.display = "flex"
    usernameDisplay.textContent = `Hi, ${currentUser}`
  } else {
    authButtons.style.display = "flex"
    userInfo.style.display = "none"
  }
}

// Form management
function showAccountForm() {
  document.getElementById("account-form").style.display = "flex"
  document.body.style.overflow = "hidden"
}

function hideAccountForm() {
  document.getElementById("account-form").style.display = "none"
  document.body.style.overflow = "auto"
}

// Initialize page when DOM is loaded
document.addEventListener("DOMContentLoaded", () => {
  // Form submission
  document.getElementById("accountOpeningForm").addEventListener("submit", async function (e) {
    e.preventDefault()

    // Basic form validation
    const requiredFields = this.querySelectorAll("[required]")
    let isValid = true

    requiredFields.forEach((field) => {
      if (!field.value.trim()) {
        isValid = false
        field.style.borderColor = "#ef4444"
      } else {
        field.style.borderColor = "#d1d5db"
      }
    })

    if (!isValid) {
      alert("Please fill in all required fields.")
      return
    }

    let formData = new FormData(this)

    try {
      const response = await fetch("/open-account/", {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": getCSRFToken(),          // ✅ Needed for Django CSRF
          "X-Requested-With": "XMLHttpRequest"   // ✅ So Django knows it's AJAX
        },
      })

      const result = await response.json()

      if (result.success) {
        alert(result.message)
        hideAccountForm()
        this.reset()
      } else {
        alert("Error: " + result.message)
      }
    } catch (error) {
      alert("Something went wrong. Please try again.")
      console.error(error)
    }
  })

  // File upload handling
  document.getElementById("documentUpload").addEventListener("change", (e) => {
    const file = e.target.files[0]
    if (file) {
      const uploadPlaceholder = document.querySelector(".upload-placeholder")
      uploadPlaceholder.innerHTML = `
                <div class="upload-icon">✅</div>
                <p>Document uploaded: ${file.name}</p>
                <button type="button" class="btn-secondary" onclick="document.getElementById('documentUpload').click();">Change File</button>
            `
    }
  })

  // Close form when clicking outside
  document.getElementById("account-form").addEventListener("click", function (e) {
    if (e.target === this) {
      hideAccountForm()
    }
  })

  // Initialize authentication display
  updateAuthDisplay()
})

// CSRF token extractor
function getCSRFToken() {
  let csrfToken = null
  const cookies = document.cookie.split(";")
  for (let cookie of cookies) {
    let c = cookie.trim()
    if (c.startsWith("csrftoken=")) {
      csrfToken = c.substring("csrftoken=".length, c.length)
      break
    }
  }
  return csrfToken
}