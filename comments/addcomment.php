<?php
    $servername="localhost";
    $username="root";
    $password="";
    $db="comment_system";
    $connect=mysqli_connect($servername,$username,$password,$db);
    
    $commenter_username=htmlspecialchars($_POST["username"]);
    $comment=htmlspecialchars($_POST["comment"]);
    $safe_username = mysqli_real_escape_string($connect, $commenter_username);
    $safe_comment = mysqli_real_escape_string($connect, $comment);

    $query="INSERT INTO comments (name, comment)
    VALUES (\"{$safe_username}\", \"{$safe_comment}\");--";

    $sql = mysqli_query($connect, $query);

    header("Refresh:0; url=index.php");
?>