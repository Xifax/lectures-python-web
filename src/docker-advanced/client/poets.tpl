<!DOCTYPE html>
<html>
        <head>
            <meta charset="UTF-8">
            <title>Poets of thy Yonder</title>
        </head>

        <body>
          Poets from container far away

          <hr/>

          % for poet in poets:
            <p>{{ poet }}</p>
          % end
        </body>

</html>
