<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8"/>
    <title>FoodPrint - Find your FoodPrint</title>
    <link href="static/style.css" rel="stylesheet"/>
    <meta name="viewport" content="initial-scale = 1.0" />
  </head>
  <body>
    <div class="content">
      <h1>Find Your FoodPrint</h1>
      <section class="form">
        <form action="/info" method="get">
        <p>
          <label for="food"></label>
          <input id="food" name="food" type="text" value="" placeholder="What are you eating today?" />
        </p>
        <input id="submit" name="submit" type="submit" value="Check Enviornmental Impact"/>
        </form>
      </section>
    </div>
  </body>
</html>
