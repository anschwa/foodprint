<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>FoodPrint</title>
    <link href="static/style.css" rel="stylesheet"/>
    <meta name="viewport" content="initial-scale = 1.0" />
  </head>
  <body>
    <div class="content">
      <section>
        <h1>The FoodPrint for <span class="food">{{impact["food"]}}</span> is&hellip;</h1>
        <div class="info">
          <div class="stats">
            <div class="center">
            <p>CO<sub>2</sub> Equivalence: 
              <span class="carbon">{{impact["carbon"]}}</span>&nbsp;(Kg)</p>
            <p>Water Consumption:
              <span class="water">{{impact["water"]}}</span>&nbsp;(L/Kg)</p>
            </div>
          </div>
          <div class="color">
            <span class="global">
              <h3>Overall Enviornmental Impact</h3>
              <div id="global-impact" class="stoplight">
                <div class="red"></div>
                <div class="yellow"></div>
                <div class="green"></div>
              </div>
            </span>
            <span class="local">
              <h3>Compared to Other <span class="category">{{impact["type"]}}</span> Products</h3>
              <div id="local-impact" class="stoplight">
                <div class="red"></div>
                <div class="yellow"></div>
                <div class="green"></div>
              </div>
            </span>
          </div>
          <input id="localColor" type="hidden" value="{{impact["local"]}}"/>
          <input id="globalColor" type="hidden" value="{{impact["global"]}}"/>
        </div>
      </section>
      <a href="/">Try another Food</a>
    </div>
    <script>
     window.addEventListener("DOMContentLoaded", function() {
         const localColor = document.getElementById("localColor").value;
         const globalColor = document.getElementById("globalColor").value;

         const local = document.getElementById("local-impact");
         const global = document.getElementById("global-impact");

         local.getElementsByClassName(localColor)[0].classList.add("impact");
         global.getElementsByClassName(globalColor)[0].classList.add("impact");
     });
    </script>
  </body>
</html>
