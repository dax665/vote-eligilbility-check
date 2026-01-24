from pyscript import document

def check_vote(event):
    
    age_input = document.querySelector("#age").value
    output_div = document.querySelector("#output")
    
    if not age_input:
        output_div.innerText = "⚠️ Please enter an age!"
        output_div.style.color = "orange"
        return

    try:
        age = int(age_input)
        if age >= 18:
            output_div.innerText = "✅ You are eligible to vote!"
            output_div.style.color = "green"
        elif age < 0:
            output_div.innerText = "❌ Age cannot be negative."
            output_div.style.color = "red"
        else:
            output_div.innerText = "⏳ Not eligible yet. Keep growing!"
            output_div.style.color = "blue"
    except ValueError:
        output_div.innerText = "❌ Please enter a valid number."
        output_div.style.color = "red"
