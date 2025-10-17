# Ex.05 Design a Website for Server Side Processing

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :

```
math.html

<!DOCTYPE html>
<html>
<head>
  <title>Server Side Processing</title>
  <style>
    body {
      background-image: url('https://png.pngtree.com/thumb_back/fw800/background/20250827/pngtree-animated-light-bulb-image_16715938.jpg');
      background-size: cover; 
      background-repeat: no-repeat; 
      background-position: center center; 
      background-attachment: fixed;
      color: black;
      text-align: center;
      padding: 50px;
      font-family: Arial;
      text-align: center;
      margin-top: 50px;
    }
    input {
      padding: 8px;
      margin: 5px;
      width: 150px;
    }
    button {
      padding: 8px 15px;
      background-color: #0078D7;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
    button:hover {
      background-color: #005fa3;
    }
    h2 {
      margin-top: 20px;
    }
  </style>
</head>
<body>

  <h1>Power Calculator (P = I² × R)</h1>

  <label>Enter Current (I) in Amperes:</label><br>
  <input type="number" id="current" placeholder="e.g. 2"><br>

  <label>Enter Resistance (R) in Ohms:</label><br>
  <input type="number" id="resistance" placeholder="e.g. 5"><br>

  <button onclick="calculatePower()">Calculate Power</button>

  <h2 id="result"></h2>

  <script>
    function calculatePower() {
      let current = parseFloat(document.getElementById("current").value);
      let resistance = parseFloat(document.getElementById("resistance").value);

      if (isNaN(current) || isNaN(resistance)) {
        document.getElementById("result").innerHTML = "⚠️ Please enter valid numbers!";
        return;
      }

      let power = (current * current) * resistance;
      document.getElementById("result").innerHTML = 
        `Power = ${power.toFixed(2)} watts (W)`;
    }
  </script>

</body>
</html>

```
```
views.py

from django.shortcuts import render

def rectarea(request):
    context = {}
    context['area'] = "0"
    context['l'] = "0"
    context['b'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')
        print('request=', request)
        print('Length=', l)
        print('Breadth=', b)
        area = int(l) * int(b)
        context['area'] = area
        context['l'] = l
        context['b'] = b
        print('Area=', area)
    return render(request, 'mathapp/math.html', context)

```
```
urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofrectangle/', views.rectarea, name="areaofrectangle"),
    path('', views.rectarea, name="areaofrectangleroot")
]

```
## SERVER SIDE PROCESSING:
<img width="1919" height="1155" alt="terminalss" src="https://github.com/user-attachments/assets/88f3f6e6-a4ae-474c-a64c-bc8032eb8803" />


## HOMEPAGE:
<img width="1919" height="1161" alt="webpagepower" src="https://github.com/user-attachments/assets/68456445-680c-4217-8984-f5072cda09ac" />


## RESULT:
The program for performing server side processing is completed successfully.
