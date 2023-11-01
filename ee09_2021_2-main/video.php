<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Video On Demand</title>
    <link rel="stylesheet" href="styl3.css">

</head>
<body>
<header>
    <section class="baner-lewy">
        <h1>Internetowa wypożyczalnia filmów</h1>
    </section>
    <section class="baner-prawy">
        <table>
            <tr>
                <th>Kryminał</th>
                <th>Horror</th>
                <th>Przygodowy</th>
            </tr>
            <tr>
                <td>20</td>
                <td>30</td>
                <td>20</td>
            </tr>
        </table>
    </section>
</header>

    <section class="lista">
        <h3>Polecamy</h3>
        <article>
        <?php 
        $servername = "localhost";
        $username= "root";
        $password="";
        $db="dane3";
        $con = mysqli_connect($servername,$username,$password,$db);
        $query1 ="SELECT 
            id, nazwa, opis, zdjecie
        FROM 
            produkty
        WHERE
            id IN (18,22,23,25);";
        $result=mysqli_query($con,$query1);

        while($row=mysqli_fetch_row($result))
        {
            echo "<div>";
            echo "<h4>",$row[0]," ",$row[1],"</h4>";
            echo "<img src='",$row[3],"' alt='film'>";
            echo "<p>", $row[2],"</p>";
            echo "</div>";
        }


            mysqli_close($con);
        ?>
        </article>
    </section>
    <section class="lista">
    <h3>Filmy fantastyczne</h3>
      <article>
        <?php 
                $servername = "localhost";
                $username= "root";
                $password="";
                $db="dane3";
                $con = mysqli_connect($servername,$username,$password,$db);
                $query2 ="SELECT 
                id, nazwa, opis, zdjecie
            FROM 
                produkty
            WHERE
                rodzaje_id = 12";
            
                $result=mysqli_query($con,$query2);
        
                while($row=mysqli_fetch_row($result))
                {
                    echo "<div>";
                    echo "<h4>",$row[0]," ",$row[1],"</h4>";
                    echo "<img src='",$row[3],"' alt='film'>";
                    echo "<p>", $row[2],"</p>";
                    echo "</div>";
                }
        
        
                    mysqli_close($con);
        ?>
      </article>
    </section>
    <footer>
    <form action="#" method="POST">
        <input type="number" name="numer">
        <button type="submit">Usuń film</button>
    </form>
    <?php
     $servername = "localhost";
     $username= "root";
     $password="";
     $db="dane3";
     $con = mysqli_connect($servername,$username,$password,$db);
     $id=$_POST['numer'];
     $query4 = "DELETE 
     FROM
         produkty
     WHERE
         id=$id;";

    $result=mysqli_query($con,$query4);

    ?>
    <a href="mailto:ja@poczta.com">Strone wykonał: 28</a>
    </footer>

   

</body>
</html>