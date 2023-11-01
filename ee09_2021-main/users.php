<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Panel administratora</title>
    <link rel="stylesheet" href="styl4.css">
</head>
<body>
    
    <header>
        <h3>Portal Społecznościowy - panel administratora</h3>
    </header>
    <main>
        <section>
            <h4>Użytkownicy</h4>
            <?php 
            $servername="localhost";
            $username="root";
            $db="dane4";
            $password="";

            $con=mysqli_connect($servername,$username,$password,$db);
            $query1="SELECT 
                id, imie, nazwisko, rok_urodzenia, zdjecie
            FROM 
                osoby
            LIMIT 
                30;";
            $result=mysqli_query($con,$query1);
            while($row=mysqli_fetch_row($result))
            {
                $wiek = 2023 - $row[3];
                echo $row[0]," ",$row[1]," ",$row[2]," ",$wiek, "<br>";

            }

            ?>
            <a href="settings.html"> Inne ustawienia </a>
        </section>
        <section>
            <h4>Podaj id użytkownika</h4>
            <form action="" method="POST">
                <input type=number name="numer">
                <button type="submit">Zobacz</button>
            </form>
            <hr>
            <?php
            $servername="localhost";
            $username="root";
            $db="dane4";
            $password="";

            $con=mysqli_connect($servername,$username,$password,$db);
            $id=$_POST["numer"];
            $query2="SELECT 
                imie, nazwisko, rok_urodzenia, opis ,zdjecie , nazwa
            FROM 
                osoby
            JOIN 
                hobby ON osoby.Hobby_id = hobby.id
            WHERE 
                osoby.id=$id;";
            $result=mysqli_query($con,$query2);
            while($row=mysqli_fetch_row($result))
            {
                echo "<h2>",$id," ",$row[0]," ",$row[1],"</h2>";
                echo "<img src='",$row[4],"'"," alt='",$id,"'","<br>";
                echo "<p>","Rok urodzenia:",$row[2],"</p>";
                echo "<p>","Opis:",$row[3],"</p>";
                echo "<p>","Hobby:",$row[5],"</p>";

                
    
            }
            ?>
        </section>
    </main>
    <footer>
        Strone wykonał: 28
    </footer>
</body>
</html>