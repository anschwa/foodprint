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
        <h1>Sorry,</h1>
        <p>
          We don't have enough information about that food yet.
        </p>
        <form action="/info" method="get">
          <select name="food">
            <option value="">Can't find what you're looking for?</option>
            % for c in choices:
            <option value="{{c[0]}}">{{c[0]}}</option>
            % end
          </select>
          <input id="submit" name="submit" type="submit" value="Try Another Search"/>
        </form>
      </section>
    </div>
  </body>
</html>
