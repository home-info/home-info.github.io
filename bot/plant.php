<!DOCTYPE html>
<html>
    
    
<?php
    
$names = array("001" => ["Cynoglossum officinale","Gemeine Hundszunge"], "002" => ["Hepatica nobilis","Leberblümchen"]);
$pics  = array("001" => "pics/001.jpg", "002" => "pics/002.jpg");
$var = $_GET["pID"];
    
?>    
    
    
    

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="">
  <meta name="keywords" content="">
  <meta name="generator" content="Responsive Site Designer 1.5.1419">
  <title>Botanische Datenbank</title>
  <link rel="stylesheet" href="css/coffeegrinder.min.css">
  <link rel="stylesheet" href="css/wireframe-theme.min.css">
  <script>document.createElement( "picture" );</script>
  <script src="js/picturefill.min.js" class="picturefill" async="async"></script>
  <link rel="stylesheet" href="css/main.css">
</head>

<body>
  <div class="row full-width-row header">
    <header class="coffee-span-12">
      <div class="container header-container">
        <h1 class="page-heading">Botanische Datenbank</h1>
        <p class="paragraph tagline">Fragen Sie die Einträge in der Botanische Datenbank anhand der plantID ab.<br>
        </p>
      </div>
    </header>
  </div>
  <main class="row">
    <div class="coffee-span-4 coffee-549-span-12 coffee-700-span-12">
      <div class="container nav-container">
        <h2 class="heading-1">Datenbankeinträge</h2>
        <a class="link-text nav-link" href="plant.php?pID=001">Cynoglossum officinale</a>
        <a class="link-text nav-link" href="plant.php?pID=002">Hepatica nobilis</a>
          <hr>
        </div>
      </div>
    </div>
    <article class="coffee-span-8 coffee-880-span-8 coffee-549-span-12 coffee-700-span-12">
      <h2 class="heading-1">plantID:&nbsp;<?php echo $var ?></h2>
      <p class="paragraph">
          
          <?php
                echo "Wissenschaftlicher Name: <i>".$names[$var][0] . "</i><br>";
                echo "Deutscher Name: <i>".$names[$var][1] . "</i>";
                echo "<p><img src='".$pics[$var]."' width='50%'></p>";
          ?>
          
      </p>
    </article>
  </main>
  <div class="row full-width-row footer">
    <div class="coffee-span-12">
      <footer class="subgrid">

        <div class="row">
          <div class="coffee-span-3 hidden-column"></div>
          <div class="coffee-span-9 coffee-880-span-12">
            <p class="paragraph copywright"><br>Hannes Kainz<br>Institut für Botanik und Landschaftsökologie<br>Universität Greifswald
            </p>
          </div>
        </div>
      </footer>
    </div>
  </div>
</body>

</html>