<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Vote Checker</title>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css">
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
</head>
<body>
    <div style="text-align: center; margin-top: 50px;">
        <h1>🗳️ Python Eligibility Checker</h1>
        <input type="number" id="age" placeholder="Enter age">
        <button id="check-btn" py-click="check_vote">Check Status</button>
        <div id="output" style="margin-top: 20px; font-weight: bold;"></div>
    </div>

    <script type="py">
        from pyscript import display, document

        def check_vote(event):
            age_input = document.querySelector("#age").value
            output_div = document.querySelector("#output")
            
            if not age_input:
                output_div.innerText = "Please enter an age!"
                return

            age = int(age_input)
            if age >= 18:
                output_div.innerText = "✅ You are eligible to vote!"
                output_div.style.color = "green"
            else:
                output_div.innerText = "❌ Not eligible yet."
                output_div.style.color = "red"
    </script>
</body>
</html>

